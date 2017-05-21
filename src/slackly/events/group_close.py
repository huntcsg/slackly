from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_close')
class GroupClose(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "group_close",
                "user": "U024BE7LH",
                "channel": "G024BE91L"
            }


    For more information see https://api.slack.com/events/group_close
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'channel': types.Channel.Id,
        }
