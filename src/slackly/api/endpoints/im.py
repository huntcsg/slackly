from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Im(BaseAPIDispatch):
    pass


@Im.register('close')
class ImClose(BaseAPIEndpoint):
    """This method closes a direct message channel.


    .. code-block:: json

        {
            "ok": true
        }

    If the channel was already closed the response will include a no_op
    property:

    .. code-block:: json

        {
            "ok": true,
            "no_op": true,
            "already_closed": true
        }


    For more information see https://api.slack.com/methods/close
    """
    endpoint = 'im.close'
    required_args = {
        'channel',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'im:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Close a direct message channel.

        :param channel: Required. Direct message channel to close. e.g. D1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Im.register('history')
class ImHistory(BaseAPIEndpoint):
    """This method returns a portion of messages/events from the specified direct message channel.
    To read the entire history for a direct message channel, call the method with no latest or
    oldest arguments, and then continue paging using the instructions below.


    .. code-block:: json

        {
            "ok": true,
            "latest": "1358547726.000003",
            "messages": [
                {
                    "type": "message",
                    "ts": "1358546515.000008",
                    "user": "U2147483896",
                    "text": "Hello"
                },
                {
                    "type": "message",
                    "ts": "1358546515.000007",
                    "user": "U2147483896",
                    "text": "World",
                    "is_starred": true,
                },
                {
                    "type": "something_else",
                    "ts": "1358546515.000007",
                    "wibblr": true
                }
            ],
            "has_more": false
        }

    The messages array up to 100 messages between latest and oldest. If
    there were more than 100 messages between those two points, then has_more
    will be true.
    If a message has the same timestamp as latest or oldest it will not be
    included in the list, unless inclusive is true. This allows a client to
    fetch all messages in a hole in channel history, by calling channels.history
    with latest set to the oldest message they have after the hole, and oldest
    to the latest message they have before the hole. If the response includes
    has_more then the client can make another call, using the ts value of the
    final messages as the latest param to get the next page of messages.
    If there are more than 100 messages between the two timestamps then the
    messages returned are the ones closest to latest. In most cases an
    application will want the most recent messages and will page backward from
    there. If oldest is provided but not latest then the messages returned are
    those closest to oldest, allowing you to page forward through history if
    desired.
    Messages of type "message" are user-entered text messages sent to the direct message channel, while other types
    are events that happened within the direct message channel. All messages have both a type and a sortable
    ts, but the other fields depend on the type. For a list of all possible events,
    see the channel messages documentation.
    If a message has been starred by the calling user, the is_starred property will be present and
    true. This property is only added for starred items, so is not present in the majority of messages.
    The is_limited boolean property is only included for free teams that have
    reached the free message limit. If true, there are messages before the current
    result set, but they are beyond the message limit.

    For more information see https://api.slack.com/methods/history
    """
    endpoint = 'im.history'
    required_args = {
        'channel',
    }
    optional_args = {
        'count',
        'inclusive',
        'latest',
        'oldest',
        'unreads',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'im:history',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 count=None,
                 inclusive=None,
                 latest=None,
                 oldest=None,
                 unreads=None,
                 ):
        """Fetches history of messages and events from direct message channel.

        :param channel: Required. Direct message channel to fetch history for. e.g. D1234567890
        :param count: Optional, default=100. Number of messages to return, between 1 and 1000. e.g. 100
        :param inclusive: Optional, default=0. Include messages with latest or oldest timestamp in results. e.g. true
        :param latest: Optional, default=now. End of time range of messages to include in results. e.g. 1234567890.123456
        :param oldest: Optional, default=0. Start of time range of messages to include in results. e.g. 1234567890.123456
        :param unreads: Optional, default=0. Include unread_count_display in the output? e.g. true
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if inclusive is not None:
            optional_kwargs['inclusive'] = inclusive
        if latest is not None:
            optional_kwargs['latest'] = latest
        if oldest is not None:
            optional_kwargs['oldest'] = oldest
        if unreads is not None:
            optional_kwargs['unreads'] = unreads

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Im.register('list')
class ImList(BaseAPIEndpoint):
    """This method returns a list of all im channels that the user has.

    Returns a list of IM objects:

    .. code-block:: json

        {
            "ok": true,
            "ims": [
                {
                   "id": "D024BFF1M",
                   "is_im": true,
                   "user": "USLACKBOT",
                   "created": 1372105335,
                   "is_user_deleted": false
                },
                {
                   "id": "D024BE7RE",
                   "is_im": true,
                   "user": "U024BE7LH",
                   "created": 1356250715,
                   "is_user_deleted": false
                },
                …
            ]
        }


    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'im.list'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'im:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Lists direct message channels for the calling user.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Im.register('mark')
class ImMark(BaseAPIEndpoint):
    """This method moves the read cursor in a direct message channel.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call, the mark is saved to the database and broadcast via the message server to
    all open connections for the calling user.
    Clients should try to avoid making this call too often. When needing to mark a read position, a client
    should set a timer before making the call. In this way, any further updates needed during the timeout
    will not generate extra calls (just one per channel). This is useful for when reading scroll-back history,
    or following a busy live channel. A timeout of 5 seconds is a good starting point. Be sure to flush these
    calls on shutdown/logout.

    For more information see https://api.slack.com/methods/mark
    """
    endpoint = 'im.mark'
    required_args = {
        'channel',
        'ts',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'im:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ts,
                 ):
        """Sets the read cursor in a direct message channel.

        :param channel: Required. Direct message channel to set reading cursor in. e.g. D1234567890
        :param ts: Required. Timestamp of the most recently seen message. e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        ts=ts,
                                        **optional_kwargs
                                        )


@Im.register('open')
class ImOpen(BaseAPIEndpoint):
    """This method opens a direct message channel with another member of your Slack team.


    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "D024BFF1M"
            }
        }

    If the channel was already open the response will include no_op and
    already_open properties:

    .. code-block:: json

        {
            "ok": true,
            "no_op": true,
            "already_open": true,
            "channel": {
                "id": "D024BFF1M"
            }
        }

    In either case, if the return_im argument was passed, the channel object will contain the full channel definition:

    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id":"D024BE91L",
                "is_im":true,
                "user":"U024BE7LH",
                "created":1434412652,
                "last_read":"1442525627.000002",
                "latest":{
                    "type":"message",
                    "user":"U024BE7LH",
                    "text":"hello",
                    "ts":"1442525627.000002"
                },
                "unread_count":0,
                "unread_count_display":0,
                "is_open":true
            }
        }


    For more information see https://api.slack.com/methods/open
    """
    endpoint = 'im.open'
    required_args = {
        'user',
    }
    optional_args = {
        'return_im',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'im:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 user,
                 return_im=None,
                 ):
        """Opens a direct message channel.

        :param user: Required. User to open a direct message channel with. e.g. U1234567890
        :param return_im: Optional. Boolean, indicates you want the full IM channel definition in the response. e.g. true
        """
        optional_kwargs = {}
        if return_im is not None:
            optional_kwargs['return_im'] = return_im

        return BaseAPIEndpoint.__call__(self,
                                        user=user,
                                        **optional_kwargs
                                        )


@Im.register('replies')
class ImReplies(BaseAPIEndpoint):
    """This method returns an entire thread (a message plus all the messages in reply to it).


    .. code-block:: json

        {
            "ok": true,
            "messages": [
                {
                    "type": "message",
                    "ts": "1358546515.000008",
                    "user": "U2147483896",
                    "text": "Hello"
                },
                {
                    "type": "message",
                    "ts": "1358546515.000007",
                    "user": "U2147483896",
                    "text": "World",
                    "is_starred": true,
                },
                {
                    "type": "something_else",
                    "ts": "1358546515.000007",
                    "wibblr": true
                }
            ],
            "thread_info": [
                "complete": true,
                "count": 3,
            ]
        }


    For more information see https://api.slack.com/methods/replies
    """
    endpoint = 'im.replies'
    required_args = {
        'channel',
        'thread_ts',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'im:history',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 thread_ts,
                 ):
        """Retrieve a thread of messages posted to a direct message conversation

        :param channel: Required. Direct message channel to fetch thread from e.g. C1234567890
        :param thread_ts: Required. Unique identifier of a thread's parent message e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        thread_ts=thread_ts,
                                        **optional_kwargs
                                        )
