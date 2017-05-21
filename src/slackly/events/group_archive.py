from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_archive')
class GroupArchive(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "group_archive",
                "channel": "G024BE91L"
            }


    For more information see https://api.slack.com/events/group_archive
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
        }
