from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('pong')
class Pong(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                'type': 'pong'
            }


    This event type is returned after doing the special ping message
    """

    @property
    def schema(self):
        return {
            'type': types.String,
        }

    @property
    def _repr_fields(self):
        return ['type']
