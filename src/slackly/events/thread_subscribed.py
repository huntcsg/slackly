from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('thread_subscribed')
class ThreadSubscribed(BaseEvent):
    """



    This event type is under development
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'event_ts': types.SlackTimestamp,
            'subscription': types.Subscription,
        }
