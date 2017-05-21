import pkg_resources
import platform
import requests
import sys
from .response_factory import SlackAPIDictResponse
from .rtm_client import SlackRTMClient
import json

class SlackClient(object):

    def __init__(self,
                 token,
                 base_url="https://slack.com/api",
                 user_agent=None,
                 response_factory=SlackAPIDictResponse
                 ):

        self.token = token
        self.base_url = base_url
        self._user_agent = user_agent
        self.response_factory = response_factory

    def api_call(self, endpoint, options, **kwargs):
        if options.get('include_token', False):
            kwargs['token'] = self.token

        headers = {
            'user-agent': self.user_agent,
            # 'content-type': 'application/json;charset=utf-8',
        }

        for key in kwargs:
            if not isinstance(kwargs[key], str):
                kwargs[key] = json.dumps(kwargs[key])

        response = requests.post(self.url(endpoint), data=kwargs, headers=headers)



        if endpoint in {'rtm.start', 'rtm.connect'}:
            return SlackRTMClient.from_response(endpoint=endpoint, token=self.token, response=response.json())

        return self.response_factory(endpoint, response)

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

