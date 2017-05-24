from unittest import TestCase

class TestSlackAPI(TestCase):

    def setUp(self):
        import slackly
        self.api = slackly.SlackAPI()

    def test_not_bound(self):
        self.assertFalse(self.api.bound)
        self.assertIsNone(self.api.bind)

    def test_bound(self):
        self.api.bind = 'Foo'
        self.assertTrue(self.api.bound)
        self.assertEqual(self.api.bind, 'Foo')

    def test_repr_unbound(self):
        slackapi_repr = 'SlackAPI(bind=None)'
        self.assertEqual(repr(self.api), slackapi_repr)

    def test_repr_bound(self):
        self.api.bind = 'Foo'
        slackapi_repr = "SlackAPI(bind='Foo')"
        self.assertEqual(repr(self.api), slackapi_repr)
