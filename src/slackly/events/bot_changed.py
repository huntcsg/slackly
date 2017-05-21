from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('bot_changed')
class BotChanged(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "bot_changed",
                "bot": {
                    "id": "B024BE7LH",
                    "app_id": "A4H1JB4AZ",
                    "name": "hugbot",
                    "icons": {
                        "image_48": "https:\/\/slack.com\/path\/to\/hugbot_48.png"
                    }
                }
            }


    For more information see https://api.slack.com/events/bot_changed
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'bot': types.Bot
        }
