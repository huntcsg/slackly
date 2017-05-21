from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_joined')
class GroupJoined(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "group_joined",
                "channel": {
                     ...
                }
            }


    For more information see https://api.slack.com/events/group_joined
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel,
        }
