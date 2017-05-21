from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_created')
class FileCreated(BaseEvent):
    """
        .. code-block:: none
            :caption: Example json response

            {
                "type": "file_created",
                "file": {  ...  }
            }


    For more information see https://api.slack.com/events/file_created
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file': types.File,
        }
