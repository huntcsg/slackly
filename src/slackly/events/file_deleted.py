from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_deleted')
class FileDeleted(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "file_deleted",
                "file_id": "F2147483862",
                "event_ts": "1361482916.000004"
            }


    For more information see https://api.slack.com/events/file_deleted
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file_id': types.File.Id,
            'event_ts': types.SlackTimestamp,
        }
