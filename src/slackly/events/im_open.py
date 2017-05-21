from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('im_open')
class ImOpen(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "im_open",
                "user": "U024BE7LH",
                "channel": "D024BE91L"
            }


    For more information see https://api.slack.com/events/im_open
    """
    @property
    def schema(self):
        schema = {
            'type': types.String,
            'user': types.User.Id,
            'channel': types.Channel.Id,
        }

        return schema
