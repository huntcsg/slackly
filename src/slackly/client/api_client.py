import json
import pkg_resources
import platform
import requests
import sys

from ..api import SlackAPI
from .response_factory import SlackAPIDictResponse
from .rtm_client import SlackRTMClient


class SlackClient(object):
    """The web client"""
    def __init__(self,
                 token=None,
                 base_url="https://slack.com/api",
                 user_agent=None,
                 response_factory=SlackAPIDictResponse,
                 include_api=True,
                 raise_for_status=True
                 ):
        """
        
        :param token: Required. A :class:`str` slack token
        :param base_url: Optional. A :class:`str` base url for slack
        :param user_agent: Optional. A user agent string. leave this blank unless you know what you are doing
        :param response_factory: A response factory (gets __call__'ed on every response)
        :param raise_for_status: Indicates whether a non 200 http status code cause a python exception
        """

        self.token = token
        self.base_url = base_url
        self._user_agent = user_agent
        self.response_factory = response_factory

        self.raise_for_status = raise_for_status
        if include_api:
            self.api = SlackAPI(bind=self)
        else:
            self.api = None

        # Fill the registry if this needs to happen
        self.response_factory.initialize()

    def api_call(self, endpoint, options, **kwargs):
        if options.get('include_token', False):
            kwargs['token'] = self.token

        headers = {
            'user-agent': self.user_agent,
        }

        for key in kwargs:
            if isinstance(kwargs[key], bool):
                value = kwargs[key]
                kwargs[key] = 0 if not value else 1
            elif not isinstance(kwargs[key], str):
                kwargs[key] = json.dumps(kwargs[key])

        response = requests.post(self.url(endpoint), data=kwargs, headers=headers)

        if endpoint in {'rtm.start', 'rtm.connect'}:
            return SlackRTMClient.from_response(endpoint=endpoint, token=self.token, response=response.json())

        if self.raise_for_status:
            response.raise_for_status()

        data = response.json()

        return self.response_factory(endpoint, data)

    def make_call(self, call):
        """Given a prepared call, execute it.
        
        :param call: A :class:`slackly.api.endpoints._base.SlackAPICall` instance
        :return: The result of making the egiven api call
        """
        return call(self)

    def url(self, endpoint):
        return "{}/{}".format(self.base_url, endpoint)

    @property
    def user_agent(self):
        if self._user_agent is None:
            dist = pkg_resources.get_distribution('slackly')

            self._user_agent = {
                "client": "{0}/{1}".format(dist.project_name, dist.version),
                "python": "Python/{v.major}.{v.minor}.{v.micro}".format(v=sys.version_info),
                "system": "{0}/{1}".format(platform.system(), platform.release())
            }

        return ''.join(self._user_agent.values())

    def __repr__(self):
        token = '...' + self.token[-5:]
        return "{0.__class__.__name__}(base_url='{0.base_url}', token='{1}', response_factory={0.response_factory})".format(self, token)
