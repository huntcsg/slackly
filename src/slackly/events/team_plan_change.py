from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_plan_change')
class TeamPlanChange(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "team_plan_change",
                "plan": "std"
            }


    For more information see https://api.slack.com/events/team_plan_change
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'plan': types.TeamPlan,
        }
