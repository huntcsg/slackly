from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_shared')
class FileShared(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "file_shared",
                "file": {  ...  }
            }


    For more information see https://api.slack.com/events/file_shared
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file': types.File,
        }
