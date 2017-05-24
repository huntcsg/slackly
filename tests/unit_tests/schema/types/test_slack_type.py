from unittest import TestCase

class TestSlackType(TestCase):

    def callFUT(self, *args, **kwargs):
        from slackly.schema.types._base import SlackType
        return SlackType(*args, **kwargs)

    def setUp(self):
        data = {'foo': 1}
        slack_type = self.callFUT(data)
        self.data = data
        self.slack_type = slack_type
        self.as_dict = {'foo': 1}
        self.slack_type_repr = 'SlackType()'
        self.slack_type_repr_key = "SlackType(foo=1)"

    def test_as_dict(self):
        self.assertEqual(self.slack_type.as_dict, self.as_dict)
        self.assertFalse(self.slack_type.as_dict is self.data)

    def test_as_json(self):
        import json
        self.assertEqual(json.dumps(self.data), self.slack_type.as_json)

    def test_repr(self):
        self.assertEqual(repr(self.slack_type), self.slack_type_repr)

    def test_repr_with_included_key(self):
        self.slack_type._repr_keys.add('foo')
        self.assertEqual(repr(self.slack_type), self.slack_type_repr_key)

class TestSlackTypeNotDict(TestSlackType):

    def setUp(self):
        data = 'bar'
        slack_type = self.callFUT(data)
        self.data = {'value': data}
        self.slack_type = slack_type
        self.as_dict = {'value': 'bar'}
        self.slack_type_repr = "SlackType(value='bar')"
        self.slack_type_repr_key = "SlackType(foo=None, value='bar')"
