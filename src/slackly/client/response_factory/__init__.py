import json
from functools import partial


class SlackAPIDictResponse(object):

    def __init__(self, endpoint, data):

        self.endpoint = endpoint
        self.data = data

        self.successful = self.data['ok']
        self.warnings = self.data.get('response_metadata', {}).get('warnings', [])
        self.error = self.data.get('error', None)

    def __repr__(self):
        return json.dumps(self.data)

    @classmethod
    def initialize(cls):
        pass


class SlackAPIObjectResponse(object):
    _registry = {}

    def __new__(cls, endpoint, data):

        response_factory = cls.get_response_factory(endpoint)

        return response_factory(data)

    @classmethod
    def register(cls, endpoint, key=None, func=None):
        if key is not None:
            def func(x):
                return x[key]
        else:
            if func is None:
                def func(x):
                    return x

        def decorator(object_factory):
            cls._registry[endpoint] = {
                'factory': object_factory,
                'preprocessor': func,
            }
            return object_factory

        return decorator

    @classmethod
    def get_response_factory(cls, endpoint):

        response_factory_spec = cls._registry.get(endpoint)

        if response_factory_spec is None:
            return partial(SlackAPIDictResponse, endpoint)

        factory = response_factory_spec['factory']
        preprocessor = response_factory_spec.get('preprocessor', lambda x: x)

        return lambda response: factory(preprocessor(response.json()))

    @classmethod
    def initialize(cls):
        import slackly.schema.endpoints
