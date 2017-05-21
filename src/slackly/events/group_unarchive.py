from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_unarchive')
class GroupUnarchive(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "group_unarchive",
                "channel": "G024BE91L"
            }


    For more information see https://api.slack.com/events/group_unarchive
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
        }
