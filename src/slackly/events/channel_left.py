from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('channel_left')
class ChannelLeft(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "channel_left",
                "channel": "C024BE91L"
            }


    For more information see https://api.slack.com/events/channel_left
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
        }
