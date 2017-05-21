from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('subteam_updated')
class SubteamUpdated(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "subteam_updated",
                "subteam": {
                   "id": "S0614TZR7",
                   "team_id": "T060RNRCH",
                   "is_usergroup": true,
                   "name": "Team Admins",
                   "description": "A group of all Administrators on your team.",
                   "handle": "admins",
                   "is_external": false,
                   "date_create": 1446598059,
                   "date_update": 1446670362,
                   "date_delete": 0,
                   "auto_type": "admin",
                   "created_by": "USLACKBOT",
                   "updated_by": "U060RNRCZ",
                   "deleted_by": null,
                   "prefs": {
                       "channels": [
    
                       ],
                       "groups": [
    
                       ]
                   },
                   "users": [
                       "U060RNRCZ",
                       "U060ULRC0",
                       "U06129G2V",
                       "U061309JM"
                   ],
                   "user_count": "4"
                }
            }


    For more information see https://api.slack.com/events/subteam_updated
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'subteam': types.SubTeam,
        }
