from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('thread_marked')
class ThreadMarked(BaseEvent):
    """

    This event type is under development
    """
    pass
