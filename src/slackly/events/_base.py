event_registry = {}


def register_event(event_type):
    def decorator(event_class):
        event_registry[event_type] = event_class
        return event_class
    return decorator


class BaseEvent(dict):

    @classmethod
    def parse(cls, event):
        if hasattr(cls, 'schema'):
            new_klass = cls()
            schema = new_klass.schema
            for key in event:
                new_klass[key] = schema.get(key, lambda x: x)(event[key])
        else:
            new_klass = cls(event)

        return new_klass
