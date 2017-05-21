from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('manual_presence_change')
class ManualPresenceChange(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "manual_presence_change",
                "presence": "away"
            }


    For more information see https://api.slack.com/events/manual_presence_change
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'presence': types.Presence.String,
        }
