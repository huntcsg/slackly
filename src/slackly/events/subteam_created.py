from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('subteam_created')
class SubteamCreated(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "subteam_created",
                "subteam": {
                    "id": "S0615G0KT",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Marketing Team",
                    "description": "Marketing gurus, PR experts and product advocates.",
                    "handle": "marketing-team",
                    "is_external": false,
                    "date_create": 1446746793,
                    "date_update": 1446746793,
                    "date_delete": 0,
                    "auto_type": null,
                    "created_by": "U060RNRCZ",
                    "updated_by": "U060RNRCZ",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [
    
                        ],
                        "groups": [
    
                        ]
                    },
                    "user_count": "0"
                    }
            }


    For more information see https://api.slack.com/events/subteam_created
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'subteam': types.SubTeam,
        }
