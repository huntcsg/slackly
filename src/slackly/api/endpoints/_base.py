import collections
import os

from ...compat import lru_cache


class BaseAPIDispatch(object):

    __registry = collections.defaultdict(dict)

    def __init__(self, bind=None):
        self._bind = lambda: bind

        for api_name, api_class in self.registry.items():
            setattr(self.__class__, api_name, getattr(self.__class__, api_name, api_class()))

    @property
    def bind(self):
        """Returns the current bound client for this api endpoint. `self._bind` is a function that returns the
        currently bound client.

        :return: A :class:`slackly.SlackClient` or :class:`NoneType`
        """
        return self._bind()

    @bind.setter
    def bind(self, bind):
        self._bind = lambda: bind

    def __get__(self, instance, owner):
        if instance.bound:
            self._bind = lambda: instance.bind
        else:
            self._bind = lambda: None

        return self

    @classmethod
    def register(cls, name):
        def decorator(api_class):
            cls.__registry["{}.{}".format(cls.__module__, cls.__name__)][name] = api_class
            return api_class

        return decorator

    @property
    def registry(self):
        return self.__registry["{}.{}".format(self.__class__.__module__, self.__class__.__name__)]

    @property
    def bound(self):
        return self.bind is not None


class BaseAPIEndpoint(object):

    def __init__(self, bind=None):
        self._bind = lambda: bind

    @property
    def bind(self):
        """Returns the current bound client for this api endpoint. `self._bind` is a function that returns the
        currently bound client.

        :return: A :class:`SlackClient` or :class:`NoneType`
        """
        return self._bind()

    @bind.setter
    def bind(self, bind):
        self._bind = lambda: bind

    def __get__(self, instance, owner):
        if instance.bound:
            self._bind = lambda: instance.bind
        else:
            self._bind = lambda: None

        return self

    @property
    def bound(self):
        return self.bind is not None

    def get_scopes(self, bot=True):
        all = self.scopes['all'].copy()
        if bot:
            all.update(self.scopes['bot'])
        else:
            all.update(self.scopes['user'])

        return all

    def __call__(self, **kwargs):
        if self.bound:
            return self.bind.api_call(self.endpoint, self.options, **kwargs)
        else:
            return SlackAPICall(self.endpoint, self.options, lambda: self.bind, **kwargs)

    def __repr__(self):
        return "{0.__class__.__name__}(bound: {0.bound} | endpoint: {0.endpoint})".format(self)

    # I named it this so I could auto generate code more easily. So...sue me.
    # It should be cache_call or some such thing but it's not
    def savecall(self, *args, **kwargs):
        return BaseAPIEndpoint.__call__(self, *args, **kwargs)

    # Make the calls to this function be cached if configured to do so
    from ...config import get_config_value
    if get_config_value('ENDPOINT_CACHE_ENABLED'):
        savecall = lru_cache(get_config_value('ENDPOINT_CACHE_SIZE'), typed=True)(savecall)


class SlackAPICall(object):

    def __init__(self, endpoint, options, client_factory=None, **kwargs):
        self.endpoint = endpoint
        self.options = options
        self.kwargs = kwargs
        self.client_factory = client_factory

    def __call__(self, client=None, **kwargs):
        if client is None:
            client = self.client_factory()
            if client is None:
                raise TypeError("Invalid Client. Pass client to the call, or bind the original api object with a client")
        self.kwargs.update(kwargs)
        return client.api_call(self.endpoint, self.options, **self.kwargs)
