from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('channel_unarchive')
class ChannelUnarchive(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "channel_unarchive",
                "channel": "C024BE91L",
                "user": "U024BE7LH"
            }


    For more information see https://api.slack.com/events/channel_unarchive
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
            'user': types.User.Id,
        }
