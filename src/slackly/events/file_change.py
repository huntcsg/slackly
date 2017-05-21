from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_change')
class FileChange(BaseEvent):
    """
        .. code-block:: none
            :caption: Example json response

            {
                "type": "file_change",
                "file": {  ...  }
            }


    For more information see https://api.slack.com/events/file_change
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file': types.File,
        }
