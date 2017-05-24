from unittest import TestCase
import os
import json

class TestResponseObjectFactory(TestCase):

    def setUp(self):
        from slackly import SlackAPIDictResponse, SlackAPIObjectResponse
        from slackly.schema.types import List
        self.list = List
        self.dict_response = SlackAPIDictResponse
        self.object_response = SlackAPIObjectResponse

    def callFUT(self, endpoint, data):
        from slackly import SlackAPIObjectResponse
        return SlackAPIObjectResponse(endpoint, data)

    def get_registered_type(self, endpoint):
        factory = self.object_response._registry.get(endpoint)['factory']

        if isinstance(factory, self.list):
            return factory.slack_type
        else:
            return factory

    def endpoint_is_registered(self, endpoint):
        return endpoint in self.object_response._registry

    endpoints_data_dir = 'tests/data/endpoints'
    for endpoint in os.listdir(endpoints_data_dir):
        endpoint_dir = os.path.join(endpoints_data_dir, endpoint)
        for file in os.listdir(endpoint_dir):
            def test_func(self, endpoint_dir=endpoint_dir, file=file, endpoint=endpoint):
                with open(os.path.join(endpoint_dir, file), 'rb') as f:
                    response_data = json.loads(f.read().decode('utf-8'))
                    result = self.callFUT(endpoint, response_data)

                    if self.endpoint_is_registered(endpoint):
                        if isinstance(result, list) and result:
                            self.assertIsInstance(result[0], self.get_registered_type(endpoint))
                    else:
                        self.assertIsInstance(result, self.dict_response)

            case_name = file.replace('.json', '')

            locals()['test_{}_{}'.format(endpoint.replace('.', '_'), case_name)] = test_func


class TestResponseDictFactory(TestCase):

    def setUp(self):
        from slackly import SlackAPIDictResponse, SlackAPIObjectResponse, SlackType
        self.dict_response = SlackAPIDictResponse
        self.object_response = SlackAPIObjectResponse
        self.slack_type = SlackType

    def callFUT(self, endpoint, data):
        from slackly import SlackAPIDictResponse
        return SlackAPIDictResponse(endpoint, data)

    def get_registered_type(self, endpoint):
        return self.object_response._registry.get(endpoint)

    def endpoint_is_registered(self, endpoint):
        return endpoint in self.object_response._registry

    endpoints_data_dir = 'tests/data/endpoints'
    for endpoint in os.listdir(endpoints_data_dir):
        endpoint_dir = os.path.join(endpoints_data_dir, endpoint)
        for file in os.listdir(endpoint_dir):
            def test_func(self, endpoint_dir=endpoint_dir, file=file, endpoint=endpoint):
                with open(os.path.join(endpoint_dir, file), 'rb') as f:
                    response_data = json.loads(f.read().decode('utf-8'))
                    result = self.callFUT(endpoint, response_data)

                    if self.endpoint_is_registered(endpoint):
                        if isinstance(result, list):
                            test_object = result[0]
                        else:
                            test_object = result
                        self.assertIsInstance(test_object, self.dict_response)
                    else:
                        self.assertIsInstance(result, self.dict_response)
                        self.assertIs(result, result.data)

            case_name = file.replace('.json', '')

            locals()['test_{}_{}'.format(endpoint.replace('.','_'), case_name)] = test_func
