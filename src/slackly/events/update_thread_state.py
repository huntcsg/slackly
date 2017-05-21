from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('update_thread_state')
class UpdateThreadState(BaseEvent):
    """

    This event type is under development
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'has_unreads': types.Bool,
            'mention_count': types.Integer,
            'timestamp': types.SlackTimestamp,
            'event_ts': types.SlackTimestamp,
        }
