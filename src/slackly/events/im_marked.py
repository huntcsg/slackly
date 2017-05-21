from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('im_marked')
class ImMarked(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "im_marked",
                "channel": "D024BE91L",
                "ts": "1401383885.000061"
            }


    For more information see https://api.slack.com/events/im_marked
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
            'ts': types.SlackTimestamp,
        }
