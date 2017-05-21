from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('pin_added')
class PinAdded(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "pin_added",
                "user": "U024BE7LH",
                "channel_id": "C02ELGNBH",
                "item": {
                     ...
                },
                "event_ts": "1360782804.083113"
            }


    For more information see https://api.slack.com/events/pin_added
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'channel_id': types.Channel.Id,
            'item': types.Item,
            'event_ts': types.SlackTimestamp,
        }
