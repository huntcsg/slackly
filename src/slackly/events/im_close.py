from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('im_close')
class ImClose(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "im_close",
                "user": "U024BE7LH",
                "channel": "D024BE91L"
            }


    For more information see https://api.slack.com/events/im_close
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'channel': types.Channel.Id,
        }
