from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Groups(BaseAPIDispatch):
    pass


@Groups.register('archive')
class GroupsArchive(BaseAPIEndpoint):
    """This method archives a private channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/archive
    """
    endpoint = 'groups.archive'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Archives a private channel.

        :param channel: Required. Private channel to archive e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Groups.register('close')
class GroupsClose(BaseAPIEndpoint):
    """This method closes a private channel.


    .. code-block:: json

        {
            "ok": true
        }

    If the private channel was already closed the response will include no_op and
    already_closed properties:

    .. code-block:: json

        {
            "ok": true,
            "no_op": true,
            "already_closed": true
        }


    For more information see https://api.slack.com/methods/close
    """
    endpoint = 'groups.close'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Closes a private channel.

        :param channel: Required. Private channel to close. e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Groups.register('create')
class GroupsCreate(BaseAPIEndpoint):
    """This method creates a private channel.

    If successful, the command returns a group object, including state information:

    .. code-block:: json

        {
            "ok": true,
            "group": {
                "id": "G024BE91L",
                "name": "secretplans",
                "is_group": "true",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "is_open": true,
                "last_read": "0000000000.000000",
                "latest": null,
                "unread_count": 0,
                "unread_count_display": 0,
                "members": [
                    "U024BE7LH"
                ],
                "topic": {
                    "value": "Secret plans on hold",
                    "creator": "U024BE7LV",
                    "last_set": 1369677212
                },
                "purpose": {
                    "value": "Discuss secret plans that no-one else should know",
                    "creator": "U024BE7LH",
                    "last_set": 1360782804
                }
            }
        }


    For more information see https://api.slack.com/methods/create
    """
    endpoint = 'groups.create'
    required_args = {
        'name',
    }
    optional_args = {
        'validate',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name,
                 validate=None,
                 ):
        """Creates a private channel.

        :param name: Required. Name of private channel to create e.g.
        :param validate: Optional. Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria. e.g. true
        """
        optional_kwargs = {}
        if validate is not None:
            optional_kwargs['validate'] = validate

        return BaseAPIEndpoint.__call__(self,
                                        name=name,
                                        **optional_kwargs
                                        )


@Groups.register('createChild')
class GroupsCreateChild(BaseAPIEndpoint):
    """This method takes an existing private channel and performs the following steps:



    <ul>
    <li>Renames the existing private channel (from "example" to "example-archived").</li>
    <li>Archives the existing private channel.</li>
    <li>Creates a new private channel with the name of the existing private channel.</li>
    <li>Adds all members of the existing private channel to the new private channel.</li>
    </ul>



    This is useful when inviting a new member to an existing private channel while hiding
    all previous chat history from them. In this scenario you can call
    groups.createChild followed by groups.invite.



    The new private channel will have a special parent_group property pointing to the
    original archived private channel. This will only be returned for members of both
    private channels, so will not be visible to any newly invited members.

    If successful, the command returns the new group object:

    .. code-block:: json

        {
            "ok": true,
            "group": {
                "id": "G024BE91L",
                "name": "secretplans",
                "is_group": "true",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "members": [
                    "U024BE7LH"
                ],
                …
            }
        }


    For more information see https://api.slack.com/methods/createChild
    """
    endpoint = 'groups.createChild'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Clones and archives a private channel.

        :param channel: Required. Private channel to clone and archive. e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Groups.register('history')
class GroupsHistory(BaseAPIEndpoint):
    """This method returns a portion of messages/events from the specified private channel.
    To read the entire history for a private channel, call the method with no latest or
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
    Messages of type "message" are user-entered text messages sent to the group, while other types
    are events that happened within the group. All messages have both a type and a sortable
    ts, but the other fields depend on the type. For a list of all possible events,
    see the channel messages documentation.
    If a message has been starred by the calling user, the is_starred property will be present and
    true. This property is only added for starred items, so is not present in the majority of messages.
    The is_limited boolean property is only included for free teams that have
    reached the free message limit. If true, there are messages before the current
    result set, but they are beyond the message limit.

    For more information see https://api.slack.com/methods/history
    """
    endpoint = 'groups.history'
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
            'groups:history',
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
        """Fetches history of messages and events from a private channel.

        :param channel: Required. Private channel to fetch history for. e.g. G1234567890
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


@Groups.register('info')
class GroupsInfo(BaseAPIEndpoint):
    """This method returns information about a private channel.

    Returns a group object:

    .. code-block:: json

        {
            "ok": true,
            "group": {
                "id": "G024BE91L",
                "name": "secretplans",
                "is_group": "true",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "members": [
                    "U024BE7LH"
                ],

                "topic": { … },
                "purpose": { … },

                "last_read": "1401383885.000061",
                "latest": { … }
                "unread_count": 0,
                "unread_count_display": 0

            },
        }


    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'groups.info'
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
            'groups:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Gets information about a private channel.

        :param channel: Required. Private channel to get info on e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Groups.register('invite')
class GroupsInvite(BaseAPIEndpoint):
    """This method is used to invite a user to a private channel. The calling user must be a member of the private channel.



    To invite a new member to a private channel without giving them access to the archives
    of the private channel, call the groups.createChild method
    before inviting.

    If successful, the API response includes a group object:

    .. code-block:: json

        {
            "ok": true,
            "group": {
                …
            },
        }

    If the invited user is already in the private channel, the response will include an
    already_in_group property:

    .. code-block:: json

        {
            "ok": true,
            "already_in_group": true,
            "group": {
                …
            },
        }


    For more information see https://api.slack.com/methods/invite
    """
    endpoint = 'groups.invite'
    required_args = {
        'channel',
        'user',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 user,
                 ):
        """Invites a user to a private channel.

        :param channel: Required. Private channel to invite user to. e.g. G1234567890
        :param user: Required. User to invite. e.g. U1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        user=user,
                                        **optional_kwargs
                                        )


@Groups.register('kick')
class GroupsKick(BaseAPIEndpoint):
    """This method allows a user to remove another member from a private channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/kick
    """
    endpoint = 'groups.kick'
    required_args = {
        'channel',
        'user',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 user,
                 ):
        """Removes a user from a private channel.

        :param channel: Required. Private channel to remove user from. e.g. G1234567890
        :param user: Required. User to remove from private channel. e.g. U1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        user=user,
                                        **optional_kwargs
                                        )


@Groups.register('leave')
class GroupsLeave(BaseAPIEndpoint):
    """This method is used to leave a private channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/leave
    """
    endpoint = 'groups.leave'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Leaves a private channel.

        :param channel: Required. Private channel to leave e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Groups.register('list')
class GroupsList(BaseAPIEndpoint):
    """This method returns a list of private channels in the team that the caller is in and archived groups that the caller was in.
    The list of (non-deactivated) members in each private channel is also returned.

    Returns a list of group objects (also known as "private channel objects"):

    .. code-block:: json

        {
            "ok": true,
            "groups": [
                {
                    "id": "G024BE91L",
                    "name": "secretplans",
                    "created": 1360782804,
                    "creator": "U024BE7LH",
                    "is_archived": false,
                    "members": [
                        "U024BE7LH"
                    ],
                    "topic": {
                        "value": "Secret plans on hold",
                        "creator": "U024BE7LV",
                        "last_set": 1369677212
                    },
                    "purpose": {
                        "value": "Discuss secret plans that no-one else should know",
                        "creator": "U024BE7LH",
                        "last_set": 1360782804
                    }
                },
                ....
            ]
        }


    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'groups.list'
    required_args = {}
    optional_args = {
        'exclude_archived',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 exclude_archived=None,
                 ):
        """Lists private channels that the calling user has access to.

        :param exclude_archived: Optional, default=0. Don't return archived private channels. e.g. true
        """
        optional_kwargs = {}
        if exclude_archived is not None:
            optional_kwargs['exclude_archived'] = exclude_archived

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Groups.register('mark')
class GroupsMark(BaseAPIEndpoint):
    """This method moves the read cursor in a private channel.


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
    endpoint = 'groups.mark'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ts,
                 ):
        """Sets the read cursor in a private channel.

        :param channel: Required. Private channel to set reading cursor in. e.g. G1234567890
        :param ts: Required. Timestamp of the most recently seen message. e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        ts=ts,
                                        **optional_kwargs
                                        )


@Groups.register('open')
class GroupsOpen(BaseAPIEndpoint):
    """This method opens a private channel.


    .. code-block:: json

        {
            "ok": true
        }

    If the private channel was already open the response will include no_op and
    already_open properties:

    .. code-block:: json

        {
            "ok": true,
            "no_op": true,
            "already_open": true
        }


    For more information see https://api.slack.com/methods/open
    """
    endpoint = 'groups.open'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Opens a private channel.

        :param channel: Required. Private channel to open. e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Groups.register('rename')
class GroupsRename(BaseAPIEndpoint):
    """This method renames a private channel.


    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "C024BE91L",
                "is_group": true,
                "name": "new_name",
                "created": 1360782804
            }
        }

    Returns the channel ID, name and date created (as a unix timestamp).

    For more information see https://api.slack.com/methods/rename
    """
    endpoint = 'groups.rename'
    required_args = {
        'channel',
        'name',
    }
    optional_args = {
        'validate',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 name,
                 validate=None,
                 ):
        """Renames a private channel.

        :param channel: Required. Private channel to rename e.g. G1234567890
        :param name: Required. New name for private channel. e.g.
        :param validate: Optional. Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria. e.g. true
        """
        optional_kwargs = {}
        if validate is not None:
            optional_kwargs['validate'] = validate

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        name=name,
                                        **optional_kwargs
                                        )


@Groups.register('replies')
class GroupsReplies(BaseAPIEndpoint):
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
    endpoint = 'groups.replies'
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
            'groups:history',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 thread_ts,
                 ):
        """Retrieve a thread of messages posted to a private channel

        :param channel: Required. Private channel to fetch thread from e.g. C1234567890
        :param thread_ts: Required. Unique identifier of a thread's parent message e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        thread_ts=thread_ts,
                                        **optional_kwargs
                                        )


@Groups.register('setPurpose')
class GroupsSetPurpose(BaseAPIEndpoint):
    """This method is used to change the purpose of a private channel. The calling user must be a member of the private channel.


    .. code-block:: json

        {
            "ok": true,
            "purpose": "This is the new purpose!"
        }


    For more information see https://api.slack.com/methods/setPurpose
    """
    endpoint = 'groups.setPurpose'
    required_args = {
        'channel',
        'purpose',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 purpose,
                 ):
        """Sets the purpose for a private channel.

        :param channel: Required. Private channel to set the purpose of e.g. G1234567890
        :param purpose: Required. The new purpose e.g. My Purpose
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        purpose=purpose,
                                        **optional_kwargs
                                        )


@Groups.register('setTopic')
class GroupsSetTopic(BaseAPIEndpoint):
    """This method is used to change the topic of a private channel. The calling user must be a member of the private channel.


    .. code-block:: json

        {
            "ok": true,
            "topic": "This is the new topic!"
        }


    For more information see https://api.slack.com/methods/setTopic
    """
    endpoint = 'groups.setTopic'
    required_args = {
        'channel',
        'topic',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 topic,
                 ):
        """Sets the topic for a private channel.

        :param channel: Required. Private channel to set the topic of e.g. G1234567890
        :param topic: Required. The new topic e.g. My Topic
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        topic=topic,
                                        **optional_kwargs
                                        )


@Groups.register('unarchive')
class GroupsUnarchive(BaseAPIEndpoint):
    """This method unarchives a private channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/unarchive
    """
    endpoint = 'groups.unarchive'
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
            'groups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Unarchives a private channel.

        :param channel: Required. Private channel to unarchive e.g. G1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )
