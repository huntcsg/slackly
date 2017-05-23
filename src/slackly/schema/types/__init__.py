"""This package defines every type that Slackly defines. They are defined in a variety of sub modules for
ease of discoverability and collaboration, but all types should be exposed in this top level package.
"""
from ._base import HasIDMixin, SlackType
from .basic import (
    Epoch, String, Integer, Bool, Timestamp, SlackTimestamp, List
)
from .message import (
    Message,

    PostedMessage,
    PostedMeMessage,
    UpdatedMessage,
)
from .channel import (
    Channel,
    ChannelPurpose,
    ChannelTopic,
    ChannelType,
    CreatedChannel,

    MPIM,
    IM,
)
from .user import (
    User,
)


class DNDStatus(SlackType):
    """A Do Not Disturb Status"""
    pass


class File(HasIDMixin, SlackType):
    """A File"""
    pass


class FileComment(HasIDMixin, SlackType):
    """A File Comment"""
    pass


class Reaction(SlackType):
    """A Reaction"""

    @classmethod
    def String(cls, value):  # flake8: noqa F811
        """A Method for creating a Reaction from a String
        
        :param value: The reaction string representation
        :return: a :class:`reaction`
        """
        return cls({'value': value})


class Team(SlackType):
    """A team"""
    pass


class SubTeam(SlackType):
    """A Subteam"""

    @classmethod
    def Id(cls, id):
        """A method for creating a subteam from a team id (vs. a dictionary of attributes)
        
        :param id: a Subteam ID, e.g. T1NASNDSP
        :return: a :class:`SlackType` subclass
        """
        return cls({'id': id})


class Profile(SlackType):
    """A Profile"""
    pass


class Subscription(SlackType):
    """A Subscription"""
    pass


class Presence(SlackType):

    @classmethod
    def String(cls, value):  # flake8: noqa F811
        return cls({'value': value})


class Preference(SlackType):
    pass


class TeamProfile(SlackType):
    pass


class Item(SlackType):
    @classmethod
    def items(cls):
        return {
            'message': Message,
        }

    def __new__(cls, kwargs):
        if kwargs is None:
            return None
        slack_type = kwargs['type']

        default_item = SlackType.__new__

        return cls.items().get(slack_type, default_item)(kwargs)


class Bot(SlackType):
    pass


class TeamPlan(SlackType):
    pass
