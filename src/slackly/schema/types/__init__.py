import json
from copy import deepcopy
import datetime
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

    MPIM,
    IM,
)


class User(HasIDMixin, SlackType):
    @property
    def schema(self):
        return {
            'id': String,
            'color': String,
            'deleted': Bool,
            'is_admin': Bool,
            'is_bot': Bool,
            'is_owner': Bool,
            'is_primary_owner': Bool,
            'is_restricted': Bool,
            'is_ultra_restricted': Bool,
            'name': String,
            'profile': Profile,
            'real_name': String,
            'status': String,
            'team_id': String,
            'tz': String,
            'tz_label': String,
            'tz_offset': Integer,
        }

    def __repr__(self):
        return "User(id='{0.id}', name='{0.name}')".format(self)

class DNDStatus(SlackType):
    pass



class File(HasIDMixin, SlackType):
    pass


class FileComment(HasIDMixin, SlackType):
    pass


class Reaction(SlackType):
    pass


class Team(SlackType):
    pass


class SubTeam(SlackType):
    pass


class Profile(SlackType):
    pass


class Subscription(SlackType):
    pass


class Presence(SlackType):
    pass


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
        return cls.items()[slack_type](kwargs)
