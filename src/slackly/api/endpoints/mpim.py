from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Mpim(BaseAPIDispatch):
    pass


@Mpim.register('close')
class MpimClose(BaseAPIEndpoint):
    """This method closes a multiparty direct message channel.


    .. code-block:: json

        {
            "ok": true
        }

    If the mpim was already closed the response will include no_op and
    already_closed properties:

    .. code-block:: json

        {
            "ok": true,
            "no_op": true,
            "already_closed": true
        }


    For more information see https://api.slack.com/methods/close
    """
    endpoint = 'mpim.close'
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
            'mpim:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Closes a multiparty direct message channel.

        :param channel: Required. MPIM to close. e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Mpim.register('history')
class MpimHistory(BaseAPIEndpoint):
    """This method returns a portion of messages/events from the specified multiparty direct message channel.
    To read the entire history for a multiparty direct message, call the method with no latest or
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
    Messages of type "message" are user-entered text messages sent to the multiparty direct message channel, while other types
    are events that happened within the multiparty direct message channel. All messages have both a type and a sortable
    ts, but the other fields depend on the type. For a list of all possible events,
    see the channel messages documentation.
    If a message has been starred by the calling user, the is_starred property will be present and
    true. This property is only added for starred items, so is not present in the majority of messages.
    The is_limited boolean property is only included for free teams that have
    reached the free message limit. If true, there are messages before the current
    result set, but they are beyond the message limit.

    For more information see https://api.slack.com/methods/history
    """
    endpoint = 'mpim.history'
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
            'mpim:history',
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
        """Fetches history of messages and events from a multiparty direct message.

        :param channel: Required. Multiparty direct message to fetch history for. e.g. G1234567890
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


@Mpim.register('list')
class MpimList(BaseAPIEndpoint):
    """This method returns a list of all multiparty direct message channels that the user has.

    Returns a list of group objects:

    .. code-block:: json

        {
            "ok": true,
            "groups": [
                {
                    "id": "G024BE91L",
                    "name": "dm-messaging-user-1",
                    "created": 1360782804,
                    "creator": "U024BE7LH",
                    "is_archived": false,
                    "is_mpim": true
                    "members": [
                        "U024BE7LH",
                        "U1234567890",
                        "U2345678901",
                        "U3456789012"
                    ],
                    "topic": {
                        "value": "Group messaging.",
                        "creator": "U024BE7LH",
                        "last_set": 1360782804
                    },
                    "purpose": {
                        "value": "Group messaging with: @user @user_a @user_b @user_c",
                        "creator": "U024BE7LH",
                        "last_set": 1360782804
                    }
                },
                ....
            ]
        }


    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'mpim.list'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'mpim:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Lists multiparty direct message channels for the calling user.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Mpim.register('mark')
class MpimMark(BaseAPIEndpoint):
    """This method moves the read cursor in a multiparty direct message channel.


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
    endpoint = 'mpim.mark'
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
            'mpim:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ts,
                 ):
        """Sets the read cursor in a multiparty direct message channel.

        :param channel: Required. multiparty direct message channel to set reading cursor in. e.g. G1234567890
        :param ts: Required. Timestamp of the most recently seen message. e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        ts=ts,
                                        **optional_kwargs
                                        )


@Mpim.register('open')
class MpimOpen(BaseAPIEndpoint):
    """This method opens a multiparty direct message.



    Opening a multiparty direct message takes a list of up-to 8 encoded user ids.  If there is no MPIM already created that
    includes that exact set of members, a new MPIM will be created.  Subsequent calls to mpim.open with the same set of
    users will return the already existing MPIM conversation.

    If successful, the command returns a mpim object, including state information:

    .. code-block:: json

        {
            "ok": true,
            "group": {
                "id": "G024BE91L",
                "name": "mpdm-user--user_a--user_b--user_c-1",
                "is_group": "true",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "is_open": false,
                "is_mpim": true,
                "last_read": "0000000000.000000",
                "latest": null,
                "unread_count": 0,
                "unread_count_display": 0,
                "members": [
                    "U024BE7LH",
                    "U1234567890",
                    "U2345678901",
                    "U3456789012"
                ],
                "topic": {
                    "value": "Group messaging.",
                    "creator": "U024BE7LH",
                    "last_set": 1360782804
                },
                "purpose": {
                    "value": "Group messaging with: @user @user_a @user_b @user_c",
                    "creator": "U024BE7LH",
                    "last_set": 1360782804
                }
            }
        }


    For more information see https://api.slack.com/methods/open
    """
    endpoint = 'mpim.open'
    required_args = {
        'users',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'mpim:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 users,
                 ):
        """This method opens a multiparty direct message.

        :param users: Required. Comma separated lists of users.  The ordering of the users is preserved whenever a MPIM group is returned. e.g. U1234567890,U2345678901,U3456789012
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        users=users,
                                        **optional_kwargs
                                        )


@Mpim.register('replies')
class MpimReplies(BaseAPIEndpoint):
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
    endpoint = 'mpim.replies'
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
            'mpim:history',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 thread_ts,
                 ):
        """Retrieve a thread of messages posted to a direct message conversation from a multiparty direct message.

        :param channel: Required. Multiparty direct message channel to fetch thread from. e.g. C1234567890
        :param thread_ts: Required. Unique identifier of a thread's parent message. e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        thread_ts=thread_ts,
                                        **optional_kwargs
                                        )
