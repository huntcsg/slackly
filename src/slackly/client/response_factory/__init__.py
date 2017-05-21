import json


class SlackAPIDictResponse(object):

    def __init__(self, endpoint, response, raise_for_status=False):
        # Thanks Slacker for the inspiration
        if raise_for_status:
            response.raise_for_status()

        self.endpoint = endpoint
        self.data = response.json()

        self.successful = self.data['ok']
        self.warnings = self.data.get('response_metadata', {}).get('warnings', [])
        self.error = self.data.get('error', None)

    def __repr__(self):
        return json.dumps(self.data)

class SlackAPIObjectResponse(object):
    _registry = {}

    def __new__(cls, endpoint, response, raise_for_status=False):
        if raise_for_status:
            response.raise_for_status()

        response_factory_spec = cls._registry.get(endpoint)

        if response_factory_spec is None:
            return SlackAPIDictResponse(endpoint, response)

        factory = response_factory_spec['factory']
        preprocessor = response_factory_spec.get('preprocessor', lambda x: x)

        return factory(preprocessor(response.json()))

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
