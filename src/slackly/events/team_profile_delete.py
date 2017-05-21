from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_profile_delete')
class TeamProfileDelete(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "team_profile_delete",
                "profile": {
                    "fields": [
                        "Xf06054AAA",
                        ...
                    ]
                }
            }


    For more information see https://api.slack.com/events/team_profile_delete
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'profile': types.TeamProfile,
        }
