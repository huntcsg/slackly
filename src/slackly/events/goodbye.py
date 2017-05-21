from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('goodbye')
class Goodbye(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "goodbye"
            }


    For more information see https://api.slack.com/events/goodbye
    """
    @property
    def schema(self):
        return {
            'type': types.String,
        }
