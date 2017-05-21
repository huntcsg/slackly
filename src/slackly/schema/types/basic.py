import datetime
from ._base import SlackType


def Epoch(value):
    if value == 0:
        return None
    elif value is None:
        return None
    return datetime.datetime.fromtimestamp(int(value))


def String(value):
    if value is None:
        return None
    return str(value)


def Integer(value):
    if value is None:
        return None
    return int(value)


def Bool(value):
    if value is None:
        return None
    return bool(value)


class SlackTimestamp(SlackType):
    def __init__(self, timestamp):
        self._timestamp = timestamp

    @property
    def uuid(self):
        return self._timestamp

    @property
    def dt(self):
        return datetime.datetime.fromtimestamp(float(self._timestamp))

    def __repr__(self):
        return '{0.__class__.__name__}("{0._timestamp}")'.format(self)


class Timestamp(SlackType):
    pass


class List(SlackType):
    def __init__(self, slack_type):
        self.slack_type = slack_type

    def __call__(self, content):
        if content is None:
            return []
        return [self.slack_type(item) for item in content]
