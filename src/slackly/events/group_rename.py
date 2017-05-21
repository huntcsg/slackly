from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_rename')
class GroupRename(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "group_rename",
                "channel": {
                    "id":"G02ELGNBH",
                    "name":"new_name",
                    "created":1360782804
                }
            }


    For more information see https://api.slack.com/events/group_rename
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel
        }
