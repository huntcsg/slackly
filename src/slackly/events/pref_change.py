from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('pref_change')
class PrefChange(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "pref_change",
                "name": "messages_theme",
                "value": "dense"
            }


    For more information see https://api.slack.com/events/pref_change
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'name': types.String,
            'value': types.String,
        }
