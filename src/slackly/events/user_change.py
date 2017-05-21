from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('user_change')
class UserChange(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "user_change",
                "user": {
                    ...
                }
            }


    For more information see https://api.slack.com/events/user_change
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User,
        }
