from ._base import BaseEvent
from . import register_event


@register_event('thread_marked')
class ThreadMarked(BaseEvent):
    """

    This event type is under development
    """
    pass
