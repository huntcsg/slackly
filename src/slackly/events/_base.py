event_registry = {}


def register_event(event_type):
    """This registered an event in the global event registry
    
    :param event_type: A :class:`str` representing an event type
    :return: A callable that will register an event class as the given event type
    """
    def decorator(event_class):
        event_registry[event_type] = event_class
        return event_class
    return decorator


class BaseEvent(dict):
    """The base event"""

    @classmethod
    def parse(cls, event):
        """Given an event dictionary, gets the event schema and applies it to the dictionary, otherwise
        just returns the :class:`BaseEvent` from the dict.
        
        :param event: A :class:`dict` representing an event
        :return: A :class:`BaseEvent` subclass
        """
        if hasattr(cls, 'schema'):
            new_klass = cls()
            schema = new_klass.schema
            for key in event:
                new_klass[key] = schema.get(key, lambda x: x)(event[key])
        else:
            new_klass = cls(event)

        return new_klass
