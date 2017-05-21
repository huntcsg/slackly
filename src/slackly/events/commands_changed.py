from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('commands_changed')
class CommandsChanged(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "commands_changed",
                "event_ts" : "1361482916.000004"
            }


    For more information see https://api.slack.com/events/commands_changed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'event_ts': types.SlackTimestamp,
        }
