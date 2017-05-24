from unittest import TestCase


class TestSlackTimestamp(TestCase):

    def callFUT(self, *args, **kwargs):
        from slackly.schema.types import SlackTimestamp
        return SlackTimestamp(*args, **kwargs)

    def setUp(self):
        import datetime
        self.ts = '1495616018.733983'
        self.repr = 'SlackTimestamp("1495616018.733983")'
        self.uuid = '1495616018.733983'
        self.dt = datetime.datetime.fromtimestamp(float(self.ts))

    def test_uuid(self):
        ts = self.callFUT(self.ts)
        self.assertEqual(ts.uuid, self.uuid)

    def test_dt(self):
        ts = self.callFUT(self.ts)
        self.assertEqual(ts.dt, self.dt)

    def test_repr(self):
        ts = self.callFUT(self.ts)
        self.assertEqual(repr(ts), self.repr)


class TestSlackTimestampNoDecimal(TestSlackTimestamp):

    def setUp(self):
        import datetime
        self.ts = '1495616018'
        self.repr = 'SlackTimestamp("1495616018")'
        self.uuid = '1495616018'
        self.dt = datetime.datetime.fromtimestamp(float(self.ts))
