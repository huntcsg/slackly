from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_pref_change')
class TeamPrefChange(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "team_pref_change",
                "name": "slackbot_responses_only_admins",
                "value": true
            }


    For more information see https://api.slack.com/events/team_pref_change
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'name': types.String,
            'value': types.String,
        }
