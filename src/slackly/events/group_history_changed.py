from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('group_history_changed')
class GroupHistoryChanged(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "type": "group_history_changed",
                "latest": "1358877455.000010",
                "ts": "1361482916.000003",
                "event_ts": "1361482916.000004"
            }


    For more information see https://api.slack.com/events/group_history_changed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'latest': types.SlackTimestamp,
            'ts': types.SlackTimestamp,
            'event_ts': types.SlackTimestamp,
        }
