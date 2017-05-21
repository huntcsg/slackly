from ...events import event_registry

def SlackEventDict(event):
    event_type = event.get('type')
    return event_registry[event_type](event)


def SlackEventParsed(event):
    event_type = event.get('type')
    return event_registry[event_type].parse(event)
