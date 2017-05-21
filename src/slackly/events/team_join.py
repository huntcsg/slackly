from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_join')
class TeamJoin(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "team_join",
                "user": {
                     ...
                }
            }


    For more information see https://api.slack.com/events/team_join
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User,
        }
