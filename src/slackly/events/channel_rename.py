from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('channel_rename')
class ChannelRename(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "channel_rename",
                "channel": {
                    "id":"C02ELGNBH",
                    "name":"new_name",
                    "created":1360782804
                }
            }


    For more information see https://api.slack.com/events/channel_rename
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel,
        }
