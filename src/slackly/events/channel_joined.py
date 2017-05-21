from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('channel_joined')
class ChannelJoined(BaseEvent):
    """
        .. code-block:: none
            :caption: Example json response

            {
                "type": "channel_joined",
                "channel": {
                     ...
                }
            }


    For more information see https://api.slack.com/events/channel_joined
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel,
        }
