from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('star_removed')
class StarRemoved(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "star_removed",
                "user": "U024BE7LH",
                "item": {
                     ...
                },
                "event_ts": "1360782804.083113"
            }


    For more information see https://api.slack.com/events/star_removed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'item': types.Item,
            'event_ts': types.SlackTimestamp,
        }
