from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('desktop_notification')
class DesktopNotification(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "desktop_notification",
                "title": "FoolishBotDev",
                "subtitle": "#new_channel",
                "msg": "1489584201.102512",
                "content": "hunter: hi @basebot",
                "channel": "C1QCTSZAM",
                "launchUri": "slack://channel?id=C1QCTSZAM&message=1489584201102512&team=T1NASNDSP",
                "avatarImage": "https://secure.gravatar.com/avatar/13affcd29fcf0d3e861f5ca2c8eedc44.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2F7fa9%2Fimg%2Favatars%2Fava_0019-192.png",
                "ssbFilename": "knock_brush.mp3",
                "imageUri": null,
                "is_shared": false,
                "event_ts": "1489584201.895898"
            }

    This event tye is undocumented

    """  # noqa

    @property
    def schema(self):
        return {
            'type': types.String,
            'title': types.String,
            'subtitle': types.String,
            'msg': types.SlackTimestamp,
            'content': types.String,
            'channel': types.Channel.Id,
            'launchUri': types.String,
            'avatarImage': types.String,
            'ssbFilename': types.String,
            'imageUri': types.String,
            'is_shared': types.Bool,
            'event_ts': types.SlackTimestamp,
        }
