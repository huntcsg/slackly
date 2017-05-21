from ._base import SlackType


class Message(SlackType):
    def __repr__(self):
        if not hasattr(self, 'ts'):
            self.ts = None
        if not hasattr(self, 'subtype'):
            self.subtype = None
        return "{0.__class__.__name__}(ts='{0.ts}', subtype='{0.subtype}')".format(self)


class PostedMessage(SlackType):
    @property
    def schema(self):
        from . import Channel, SlackTimestamp
        return {
            'channel': Channel.Id,
            'message': Message,
            'ts': SlackTimestamp,
        }

    def __repr__(self):
        return "{0.__class__.__name__}(channel={0.channel}, ts={0.ts})".format(self)


class PostedMeMessage(SlackType):
    @property
    def schema(self):
        from . import Channel, SlackTimestamp
        return {
            'channel': Channel.Id,
            'ts': SlackTimestamp,
        }

    def __repr__(self):
        return "{0.__class__.__name__}(channel={0.channel}, ts={0.ts})".format(self)


class UpdatedMessage(SlackType):
    @property
    def schema(self):
        from . import Channel, SlackTimestamp, String
        return {
            'channel': Channel.Id,
            'ts': SlackTimestamp,
            'text': String,
            'message': Message,
        }

    def __repr__(self):
        return "{0.__class__.__name__}(channel={0.channel}, ts={0.ts})".format(self)
