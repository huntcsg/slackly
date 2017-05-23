from ._base import HasIDMixin, SlackType


class Channel(HasIDMixin, SlackType):
    """A Channel"""

    @property
    def schema(self):
        from . import String, Epoch, User, Bool, Integer, SlackTimestamp, Item, List
        return {
            'id': String,
            'created': Epoch,
            'creator': User.Id,
            'is_archived': Bool,
            'is_channel': Bool,
            'is_general': Bool,
            'is_member': Bool,
            'is_org_shared': Bool,
            'is_shared': Bool,
            'name': String,
            'name_normalized': String,
            'num_members': Integer,
            'last_read': SlackTimestamp,
            'latest': Item,
            'members': List(User.Id),
            'previous_names': List(String),
            'purpose': ChannelPurpose,
            'topic': ChannelTopic,
        }

    def __repr__(self):
        return "{0.__class__.__name__}(id='{0.id}', name='{0.name}')".format(self)


class ChannelTopic(SlackType):
    """A Channel Topic"""

    @property
    def schema(self):
        from . import User, Epoch, String
        return {
            'creator': User.Id,
            'last_set': Epoch,
            'value': String,
        }


class ChannelPurpose(SlackType):
    """A Channel Purpose"""

    @property
    def schema(self):
        from . import User, Epoch, String
        return {
            'creator': User.Id,
            'last_set': Epoch,
            'value': String,
        }


class CreatedChannel(SlackType):
    """A Created Channel"""

    @property
    def schema(self):
        from . import Team
        return {
            'channel': Channel,
            'original_team': Team,
        }


class MPIM(SlackType):
    """An Multi-Person Direct Message Channel"""
    pass


class IM(SlackType):
    """An Single Person Direct Message Channel"""
    pass


class ChannelType(SlackType):
    """A Channel Type"""
    pass
