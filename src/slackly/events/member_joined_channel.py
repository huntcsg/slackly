from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('member_joined_channel')
class MemberJoinedChannel(BaseEvent):
    """
        .. code-block:: json
            :caption: Example json response

            {
                "type": "member_joined_channel",
                "user": "W06GH7XHN",
                "channel": "C0698JE0H",
                "channel_type": "C",
                "inviter": "U123456789"
            }


    For more information see https://api.slack.com/events/member_joined_channel
    """
    @property
    def schema(self):
        return {
            'type': types.String,
            'channel': types.Channel.Id,
            'user': types.User.Id,
            'channel_type': types.ChannelType,
            'event_ts': types.SlackTimestamp,
            'ts': types.SlackTimestamp,
        }
