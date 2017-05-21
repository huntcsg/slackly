from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('subteam_self_removed')
class SubteamSelfRemoved(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "subteam_self_removed",
                "subteam_id": "S0615G0KT"
            }


    For more information see https://api.slack.com/events/subteam_self_removed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'subteam_id': types.SubTeam.Id,
        }
