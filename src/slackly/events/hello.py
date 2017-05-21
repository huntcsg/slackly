from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('hello')
class Hello(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "hello"
            }


    For more information see https://api.slack.com/events/hello
    """
    @property
    def schema(self):
        return {
            'type': types.String,
        }
