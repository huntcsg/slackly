from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('channel_created')
class ChannelCreated(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "channel_created",
                "channel": {
                    "id": "C024BE91L",
                    "name": "fun",
                    "created": 1360782804,
                    "creator": "U024BE7LH"
                }
            }


    For more information see https://api.slack.com/events/channel_created
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel,
        }
