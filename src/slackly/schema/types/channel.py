from ._base import HasIDMixin, SlackType


class Channel(HasIDMixin, SlackType):
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


class ChannelTopic(SlackType):
    @property
    def schema(self):
        from . import User, Epoch, String
        return {
            'creator': User.Id,
            'last_set': Epoch,
            'value': String,
        }


class ChannelPurpose(SlackType):
    @property
    def schema(self):
        from . import User, Epoch, String
        return {
            'creator': User.Id,
            'last_set': Epoch,
            'value': String,
        }

class MPIM(SlackType):
    pass


class IM(SlackType):
    pass
