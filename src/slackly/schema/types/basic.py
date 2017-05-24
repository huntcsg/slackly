import datetime
import six

from ._base import SlackType


def Epoch(value):
    """A Function to take an epoch and return a datetime.datetime object. Also defaults that 0 is None
    
    :param value: An epoch
    :return: a :class:`datetime.datetime` or None
    """
    if value == 0:
        return None
    elif value is None:
        return None
    return datetime.datetime.fromtimestamp(int(value))


def String(value):
    """A function to convert a value into a string
    
    :param value: any stringifyable value
    :return: a :class:`str` or None
    """
    if value is None:
        return None
    return six.text_type(value)


def Integer(value):
    """A function to convert a value into a string
    
    :param value: any intable value
    :return: a :class:`int` or None
    """
    if value is None:
        return None
    return int(value)


def Bool(value):
    """A function to convert a value into a Boolean
    
    :param value: any value that can be passed to bool
    :return: a :class:`bool` or None
    """
    if value is None:
        return None
    return bool(value)


class SlackTimestamp(SlackType):
    """A type to wrap slack timestamps. These represent actual times, but also can be considered uuids in
    the context of a team.
    """
    def __init__(self, timestamp):
        """
        
        :param timestamp: A :class:`str` representing a timestamp
        """
        self._timestamp = timestamp

    @property
    def uuid(self):
        """

        :return: A :class:`str` representing a a timestampe
        """
        return self._timestamp

    @property
    def dt(self):
        """Returns the :class:`SlackTimeStamp` as a :class:`datetime.datetime`
        
        :return: A :class:`datetime.datetime`
        """
        return datetime.datetime.fromtimestamp(float(self._timestamp))

    def __repr__(self):
        return '{0.__class__.__name__}("{0._timestamp}")'.format(self)


class Timestamp(SlackType):
    """An actual timestamp (not necessarily a uuid"""
    pass


class List(SlackType):
    """A collection. It gets instantiated with a type factory, and when it's called, it iterates through its
    argument and returns a :class:`list` of whatever type it was instantiated with.
    
    """
    def __init__(self, slack_type):
        """
        
        :param slack_type: A :class:`SlackType`
        """
        self.slack_type = slack_type

    def __call__(self, content):
        if content is None:
            return []
        return [self.slack_type(item) for item in content]
