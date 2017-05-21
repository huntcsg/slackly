from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('dnd_updated')
class DndUpdated(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "dnd_updated",
                "user": "U1234",
                "dnd_status": {
                    "dnd_enabled": true,
                    "next_dnd_start_ts": 1450387800,
                    "next_dnd_end_ts": 1450423800,
                    "snooze_enabled": true,
                    "snooze_endtime": 1450373897
                }
            }


    For more information see https://api.slack.com/events/dnd_updated
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'dnd_status': types.DNDStatus
        }
