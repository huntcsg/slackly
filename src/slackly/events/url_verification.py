from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('url_verification')
class UrlVerification(BaseEvent):
    """

        .. code-block:: json
            :caption: Example json response

            {
                "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
                "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
                "type": "url_verification"
            }


    For more information see https://api.slack.com/events/url_verification
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'challenge': types.String,
            'token': types.String,
        }
