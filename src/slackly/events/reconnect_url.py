from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('reconnect_url')
class ReconnectUrl(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "reconnect_url",
                "url": "wss://mpmulti-0m6f.slack-msgs.com/websocket/...."
            }


    For more information see https://api.slack.com/events/reconnect_url
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'url': types.String,
        }
