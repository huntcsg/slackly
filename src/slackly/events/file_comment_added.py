from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('file_comment_added')
class FileCommentAdded(BaseEvent):
    """
        .. code-block:: none
            :caption: Example json response

            {
                "type": "file_comment_added",
                "file": {  ...  },
                "comment": {  ...  }
            }


    For more information see https://api.slack.com/events/file_comment_added
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'file': types.File,
            'comment': types.FileComment,
        }
