from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_left')
class GroupLeft(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "group_left",
                "channel": "G02ELGNBH"
            }


    For more information see https://api.slack.com/events/group_left
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
        }
