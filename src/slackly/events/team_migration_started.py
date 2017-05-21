from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('team_migration_started')
class TeamMigrationStarted(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "team_migration_started",
            }


    For more information see https://api.slack.com/events/team_migration_started
    """
    @property
    def schema(self):
        return {
            'type': types.String,
        }
