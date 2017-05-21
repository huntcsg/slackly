from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('accounts_changed')
class AccountsChanged(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "accounts_changed"
            }


    For more information see https://api.slack.com/events/accounts_changed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
        }
