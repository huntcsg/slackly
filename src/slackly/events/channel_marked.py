from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('channel_marked')
class ChannelMarked(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "channel_marked",
                "channel": "C024BE91L",
                "ts": "1401383885.000061"
            }


    For more information see https://api.slack.com/events/channel_marked
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
            'ts': types.SlackTimestamp,
        }
