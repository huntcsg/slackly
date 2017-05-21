from ._base import BaseEvent
from . import register_event
from ..schema import types


@register_event('reaction_added')
class ReactionAdded(BaseEvent):
    """

        .. code-block:: none
            :caption: Example json response

            {
                "type": "reaction_added",
                "user": "U024BE7LH",
                "reaction": "thumbsup",
                "item_user": "U0G9QF9C6",
                "item": {
                    ...
                },
                "event_ts": "1360782804.083113"
            }


    For more information see https://api.slack.com/events/reaction_added
    """

    @property
    def schema(self):
        return {
            'type': types.String,
            'user': types.User.Id,
            'reaction': types.Reaction.String,
            'item': types.Item,
            'item_user': types.User.Id,
            'event_ts': types.SlackTimestamp,
        }
