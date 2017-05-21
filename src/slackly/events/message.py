from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('message')
class Message(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "message",
                "channel": "C2147483705",
                "user": "U2147483697",
                "text": "Hello world",
                "ts": "1355517523.000005"
            }


    For more information see https://api.slack.com/events/message
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
            'user': types.User.Id,
            'text': types.String,
            'ts': types.SlackTimestamp,
        }
