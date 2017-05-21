from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_public')
class FilePublic(BaseEvent):
    """
        .. code-block:: none
            :caption: Example json response

            {
                "type": "file_public",
                "file_id": "F4LDY26EL",
                "user_id": "USLACKBOT",
                "file": {  ...  }
                "event_ts": "1490062255.798583",
            }


    For more information see https://api.slack.com/events/file_public
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file': types.File,
            'file_id': types.String,
            'user_id': types.User.Id,
            'event_ts': types.SlackTimestamp,
        }
