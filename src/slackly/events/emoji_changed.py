from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('emoji_changed')
class EmojiChanged(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "emoji_changed",
                "subtype": "remove",
                "names": ["picard_facepalm"],
                "event_ts" : "1361482916.000004"
            }


    For more information see https://api.slack.com/events/emoji_changed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'subtype': types.String,
            'names': types.List(types.String),
            'event_ts': types.SlackTimestamp,
        }
