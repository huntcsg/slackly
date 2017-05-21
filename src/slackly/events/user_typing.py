from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('user_typing')
class UserTyping(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "user_typing",
                "channel": "C02ELGNBH",
                "user": "U024BE7LH"
            }


    For more information see https://api.slack.com/events/user_typing
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
            'user': types.User.Id,
        }
