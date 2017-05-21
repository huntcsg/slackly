from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_unshared')
class FileUnshared(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "file_unshared",
                "file": {  ...  }
            }


    For more information see https://api.slack.com/events/file_unshared
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file': types.File,
        }
