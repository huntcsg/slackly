from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('subteam_self_added')
class SubteamSelfAdded(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "subteam_self_added",
                "subteam_id": "S0615G0KT"
            }


    For more information see https://api.slack.com/events/subteam_self_added
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'subteam_id': types.SubTeam.Id,
        }
