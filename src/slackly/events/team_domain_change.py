from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_domain_change')
class TeamDomainChange(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "team_domain_change",
                "url": "https://my.slack.com",
                "domain": "my"
            }


    For more information see https://api.slack.com/events/team_domain_change
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'url': types.String,
            'domain': types.String,
        }
