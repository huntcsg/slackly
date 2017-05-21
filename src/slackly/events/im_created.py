from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('im_created')
class ImCreated(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "im_created",
                "user": "U024BE7LH",
                "channel": {...}
            }


    For more information see https://api.slack.com/events/im_created
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'channel': types.Channel,
        }
