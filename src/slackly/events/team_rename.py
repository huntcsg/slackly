from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_rename')
class TeamRename(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "team_rename",
                "name": "New Team Name Inc."
            }


    For more information see https://api.slack.com/events/team_rename
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'name': types.String,
        }
