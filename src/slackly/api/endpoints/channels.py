from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Channels(BaseAPIDispatch):
    pass


@Channels.register('archive')
class ChannelsArchive(BaseAPIEndpoint):
    """This method archives a channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/archive
    """
    endpoint = 'channels.archive'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Archives a channel.

        :param channel: Required. Channel to archive e.g. C1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Channels.register('create')
class ChannelsCreate(BaseAPIEndpoint):
    """This method is used to create a channel.



    To create a private channel, use groups.create.

    If successful, the command returns a channel object, including state information:

    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "C024BE91L",
                "name": "fun",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "is_member": true,
                "is_general": false,
                "last_read": "0000000000.000000",
                "latest": null,
                "unread_count": 0,
                "unread_count_display": 0,
                "members": [ ... ],
                "topic": { ... },
                "purpose": { ... }
            }
        }


    For more information see https://api.slack.com/methods/create
    """
    endpoint = 'channels.create'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name,
                 validate=None,
                 ):
        """Creates a channel.

        :param name: Required. Name of channel to create e.g. mychannel
        :param validate: Optional. Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria. e.g. true
        """
        optional_kwargs = {}
        if validate is not None:
            optional_kwargs['validate'] = validate

        return BaseAPIEndpoint.__call__(self,
                                        name=name,
                                        **optional_kwargs
                                        )


@Channels.register('history')
class ChannelsHistory(BaseAPIEndpoint):
    """This method returns a portion of message events from the specified public channel.



    To read the entire history for a channel, call the method with no latest or
    oldest arguments, and then continue paging using the instructions below.



    To retrieve a single message, specify its ts value as latest, set inclusive to true, and dial your count down to 1.


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
                    "reactions": [
                        {
                            "name": "space_invader",
                            "count": 3,
                            "users": [ "U1", "U2", "U3" ]
                        },
                        {
                            "name": "sweet_potato",
                            "count": 5,
                            "users": [ "U1", "U2", "U3", "U4", "U5" ]
                        }
                    ]
                            },
                {
                    "type": "something_else",
                    "ts": "1358546515.000007",
                    "wibblr": true
                }
            ],
            "has_more": false
        }


    Navigating through collections of messages
    The messages array contains up to 100 messages between latest and oldest. If
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

    Retrieving a single message
    channels.history can also be used to pluck a single message from the archive.
    You'll need a message's ts value, uniquely identifying it within a channel.  You'll also need that channel's ID.
    Provide another message's ts value as the latest parameter. Specify true for the inclusive parameter and set the count to 1. If it exists, you'll receive the queried message in return.
    GET /api/channels.history?token=TOKEN_WITH_CHANNELS_HISTORY_SCOPE&channel=C2EB2QT8A&latest=1476909142.000007&inclusive=true&count=1


    Message types
    Messages of type "message" are user-entered text messages sent to the channel, while other types are events that happened within the channel. All messages have both a type and a sortable ts, but the other fields depend on the type. For a list of all possible events, see the channel messages documentation.
    Messages that have been reacted to by team members will have a reactions array delightfully included.
    If a message has been starred by the calling user, the is_starred property will be present and true. This property is only added for starred items, so is not present in the majority of messages.
    The is_limited boolean property is only included for free teams that have
    reached the free message limit. If true, there are messages before the current
    result set, but they are beyond the message limit.

    For more information see https://api.slack.com/methods/history
    """
    endpoint = 'channels.history'
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
            'channels:history',
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
        """Fetches history of messages and events from a channel.

        :param channel: Required. Channel to fetch history for. e.g. C1234567890
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

        return BaseAPIEndpoint.savecall(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Channels.register('info')
class ChannelsInfo(BaseAPIEndpoint):
    """This method returns information about a team channel.



    To retrieve information on a private channel, use groups.info.

    Returns a channel object:

    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "C024BE91L",
                "name": "fun",

                "created": 1360782804,
                "creator": "U024BE7LH",

                "is_archived": false,
                "is_general": false,
                "is_member": true,
                "is_starred": true,

                "members": [ ... ],

                "topic": { ... },
                "purpose": { ... },

                "last_read": "1401383885.000061",
                "latest": { ... },
                "unread_count": 0,
                "unread_count_display": 0
            }
        }

    An is_org_shared attribute may appear set to true when the channel is part of a shared channel between multiple teams of an Enterprise Grid. You'll also find the team's enterprise_id. See the Enterprise Grid shared channels documentation for more detail.

    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'channels.info'
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
            'channels:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Gets information about a channel.

        :param channel: Required. Channel to get info on e.g. C1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.savecall(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Channels.register('invite')
class ChannelsInvite(BaseAPIEndpoint):
    """This method is used to invite a user to a channel. The calling user must be a member of the channel.


    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "C024BE91L",
                "name": "fun",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "is_member": true,
                "is_general": false,
                "last_read": "1401383885.000061",
                "latest": { … },
                "unread_count": 0,
                "unread_count_display": 0,
                "members": [ … ],
                "topic": {
                    "value": "Fun times",
                    "creator": "U024BE7LV",
                    "last_set": 1369677212
                },
                "purpose": {
                    "value": "This channel is for fun",
                    "creator": "U024BE7LH",
                    "last_set": 1360782804
                }
            }
        }


    For more information see https://api.slack.com/methods/invite
    """
    endpoint = 'channels.invite'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 user,
                 ):
        """Invites a user to a channel.

        :param channel: Required. Channel to invite user to. e.g. C1234567890
        :param user: Required. User to invite to channel. e.g. U1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        user=user,
                                        **optional_kwargs
                                        )


@Channels.register('join')
class ChannelsJoin(BaseAPIEndpoint):
    """This method is used to join a channel. If the channel does not exist, it is
    created.

    If successful, the command returns a channel object, including state information:

    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "C024BE91L",
                "name": "fun",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "is_member": true,
                "is_general": false,
                "last_read": "1401383885.000061",
                "latest": { … },
                "unread_count": 0,
                "unread_count_display": 0,
                "members": [ … ],
                "topic": {
                    "value": "Fun times",
                    "creator": "U024BE7LV",
                    "last_set": 1369677212
                },
                "purpose": {
                    "value": "This channel is for fun",
                    "creator": "U024BE7LH",
                    "last_set": 1360782804
                }
            }
        }

    If you are already in the channel, the response is slightly different.
    already_in_channel will be true, and a limited channel object will be
    returned. This allows a client to see that the request to join GeNERaL is
    the same as the channel #general that the user is already in:

    .. code-block:: json

        {
            "ok": true,
            "already_in_channel": true,
            "channel": {
                "id": "C024BE91L",
                "name": "fun",
                "created": 1360782804,
                "creator": "U024BE7LH",
                "is_archived": false,
                "is_general": false
            }
        }


    For more information see https://api.slack.com/methods/join
    """
    endpoint = 'channels.join'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name,
                 validate=None,
                 ):
        """Joins a channel, creating it if needed.

        :param name: Required. Name of channel to join e.g. C1234567890
        :param validate: Optional. Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria. e.g. true
        """
        optional_kwargs = {}
        if validate is not None:
            optional_kwargs['validate'] = validate

        return BaseAPIEndpoint.__call__(self,
                                        name=name,
                                        **optional_kwargs
                                        )


@Channels.register('kick')
class ChannelsKick(BaseAPIEndpoint):
    """This method allows a user to remove another member from a team channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/kick
    """
    endpoint = 'channels.kick'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 user,
                 ):
        """Removes a user from a channel.

        :param channel: Required. Channel to remove user from. e.g. C1234567890
        :param user: Required. User to remove from channel. e.g. U1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        user=user,
                                        **optional_kwargs
                                        )


@Channels.register('leave')
class ChannelsLeave(BaseAPIEndpoint):
    """This method is used to leave a channel.


    .. code-block:: json

        {
            "ok": true
        }

    This method will not return an error if the user was not in the channel before
    it was called. Instead the response will include a not_in_channel property:

    .. code-block:: json

        {
            "ok": true,
            "not_in_channel": true
        }


    For more information see https://api.slack.com/methods/leave
    """
    endpoint = 'channels.leave'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Leaves a channel.

        :param channel: Required. Channel to leave e.g. C1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Channels.register('list')
class ChannelsList(BaseAPIEndpoint):
    """This method returns a list of all channels in the team. This includes channels the caller is in, channels they are not currently in, and archived channels but does not include private channels. The number of (non-deactivated) members in each channel is also returned.



    To retrieve a list of private channels, use groups.list.



    Having trouble getting a HTTP 200 response from this method? Try excluding the members list from each channel object using the exclude_members parameter.

    Returns a list of limited channel objects:

    .. code-block:: json

        {
            "ok": true,
            "channels": [
                {
                    "id": "C024BE91L",
                    "name": "fun",
                    "created": 1360782804,
                    "creator": "U024BE7LH",
                    "is_archived": false,
                    "is_member": false,
                    "num_members": 6,
                    "topic": {
                        "value": "Fun times",
                        "creator": "U024BE7LV",
                        "last_set": 1369677212
                    },
                    "purpose": {
                        "value": "This channel is for fun",
                        "creator": "U024BE7LH",
                        "last_set": 1360782804
                    }
                },
                ....
            ]
        }

    To get a full channel object, call the channels.info method.
    Use the exclude_members parameter to exclude the members collection from each listed channel. This improves performance, especially with larger teams. Use channels.info to retrieve members on a channel-by-channel basis instead.
    An is_org_shared attribute may appear set to true on channels that are shared channel between multiple teams of an enterprise grid. See the enterprise grid shared channels documentation for more detail.

    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'channels.list'
    required_args = {}
    optional_args = {
        'exclude_archived',
        'exclude_members',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'channels:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 exclude_archived=None,
                 exclude_members=None,
                 ):
        """Lists all channels in a Slack team.

        :param exclude_archived: Optional, default=false. Exclude archived channels from the list e.g. true
        :param exclude_members: Optional, default=false. Exclude the members collection from each channel e.g. true
        """
        optional_kwargs = {}
        if exclude_archived is not None:
            optional_kwargs['exclude_archived'] = exclude_archived
        if exclude_members is not None:
            optional_kwargs['exclude_members'] = exclude_members

        return BaseAPIEndpoint.savecall(self,
                                        **optional_kwargs
                                        )


@Channels.register('mark')
class ChannelsMark(BaseAPIEndpoint):
    """This method moves the read cursor in a channel.


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
    endpoint = 'channels.mark'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ts,
                 ):
        """Sets the read cursor in a channel.

        :param channel: Required. Channel to set reading cursor in. e.g. C1234567890
        :param ts: Required. Timestamp of the most recently seen message. e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        ts=ts,
                                        **optional_kwargs
                                        )


@Channels.register('rename')
class ChannelsRename(BaseAPIEndpoint):
    """This method renames a team channel.



    The only people who can rename a channel are Team Admins, or the person that
    originally created the channel. Others will receive a "not_authorized" error.


    .. code-block:: json

        {
            "ok": true,
            "channel": {
                "id": "C024BE91L",
                "is_channel": true,
                "name": "new_name",
                "created": 1360782804
            }
        }

    Returns the channel ID, name and date created (as a unix timestamp).

    For more information see https://api.slack.com/methods/rename
    """
    endpoint = 'channels.rename'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 name,
                 validate=None,
                 ):
        """Renames a channel.

        :param channel: Required. Channel to rename e.g. C1234567890
        :param name: Required. New name for channel. e.g.
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


@Channels.register('replies')
class ChannelsReplies(BaseAPIEndpoint):
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
    endpoint = 'channels.replies'
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
            'channels:history',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 thread_ts,
                 ):
        """Retrieve a thread of messages posted to a channel

        :param channel: Required. Channel to fetch thread from e.g. C1234567890
        :param thread_ts: Required. Unique identifier of a thread's parent message e.g. 1234567890.123456
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        thread_ts=thread_ts,
                                        **optional_kwargs
                                        )


@Channels.register('setPurpose')
class ChannelsSetPurpose(BaseAPIEndpoint):
    """This method is used to change the purpose of a channel. The calling user must be a member of the channel.


    .. code-block:: json

        {
            "ok": true,
            "purpose": "This is the new purpose!"
        }


    For more information see https://api.slack.com/methods/setPurpose
    """
    endpoint = 'channels.setPurpose'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 purpose,
                 ):
        """Sets the purpose for a channel.

        :param channel: Required. Channel to set the purpose of e.g. C1234567890
        :param purpose: Required. The new purpose e.g. My Purpose
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        purpose=purpose,
                                        **optional_kwargs
                                        )


@Channels.register('setTopic')
class ChannelsSetTopic(BaseAPIEndpoint):
    """This method is used to change the topic of a channel. The calling user must be a member of the channel.


    .. code-block:: json

        {
            "ok": true,
            "topic": "This is the new topic!"
        }


    For more information see https://api.slack.com/methods/setTopic
    """
    endpoint = 'channels.setTopic'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 topic,
                 ):
        """Sets the topic for a channel.

        :param channel: Required. Channel to set the topic of e.g. C1234567890
        :param topic: Required. The new topic e.g. My Topic
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        topic=topic,
                                        **optional_kwargs
                                        )


@Channels.register('unarchive')
class ChannelsUnarchive(BaseAPIEndpoint):
    """This method unarchives a channel. The calling user is added to the channel.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/unarchive
    """
    endpoint = 'channels.unarchive'
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
            'channels:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Unarchives a channel.

        :param channel: Required. Channel to unarchive e.g. C1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )
