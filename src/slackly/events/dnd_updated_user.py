from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('dnd_updated_user')
class DndUpdatedUser(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "dnd_updated_user",
                "user": "U1234",
                "dnd_status": {
                    "dnd_enabled": true,
                    "next_dnd_start_ts": 1450387800,
                    "next_dnd_end_ts": 1450423800
                }
            }


    For more information see https://api.slack.com/events/dnd_updated_user
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'dnd_status': types.DNDStatus,
        }
