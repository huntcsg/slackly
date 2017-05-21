from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('email_domain_changed')
class EmailDomainChanged(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "email_domain_changed",
                "email_domain":"example.com",
                "event_ts": "1360782804.083113"
            }


    For more information see https://api.slack.com/events/email_domain_changed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'email_domain': types.String,
            'event_ts': types.SlackTimestamp,
        }
