from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_profile_reorder')
class TeamProfileReorder(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "team_profile_reorder",
                "profile": {
                    "fields": [
                        {
                            "id": "Xf06054AAA",
                            "ordering": 0,
                        },
                        ...
                    ]
                }
            }


    For more information see https://api.slack.com/events/team_profile_reorder
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'profile': types.TeamProfile,
        }
