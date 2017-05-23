from ...events import event_registry
from ...events._base import BaseEvent


def SlackEventDict(event):
    event_type = event.get('type')
    return event_registry.get(event_type, BaseEvent)(event)


def SlackEventParsed(event):
    event_type = event.get('type')
    return event_registry.get(event_type, BaseEvent).parse(event)
