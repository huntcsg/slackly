from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('presence_change')
class PresenceChange(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "presence_change",
                "user": "U024BE7LH",
                "presence": "away"
            }


    For more information see https://api.slack.com/events/presence_change
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'presence': types.Presence.String,
        }

    @property
    def _repr_fields(self):
        return ['type', 'presence']
