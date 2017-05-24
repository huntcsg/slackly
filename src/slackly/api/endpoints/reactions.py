from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Reactions(BaseAPIDispatch):
    pass


@Reactions.register('add')
class ReactionsAdd(BaseAPIEndpoint):
    """This method adds a reaction (emoji) to an item (file, file comment, channel message, group message, or direct message).
    One of file, file_comment, or the combination of channel and timestamp must be specified.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call, the reaction is saved and a reaction_added event is broadcast through the RTM API for the calling user.

    For more information see https://api.slack.com/methods/add
    """
    endpoint = 'reactions.add'
    required_args = {
        'name',
    }
    optional_args = {
        'channel',
        'file',
        'file_comment',
        'timestamp',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reactions:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name,
                 channel=None,
                 file=None,
                 file_comment=None,
                 timestamp=None,
                 ):
        """Adds a reaction to an item.

        :param name: Required. Reaction (emoji) name. e.g. thumbsup
        :param channel: Optional. Channel where the message to add reaction to was posted. e.g. C1234567890
        :param file: Optional. File to add reaction to. e.g. F1234567890
        :param file_comment: Optional. File comment to add reaction to. e.g. Fc1234567890
        :param timestamp: Optional. Timestamp of the message to add reaction to. e.g. 1234567890.123456
        """
        optional_kwargs = {}
        if channel is not None:
            optional_kwargs['channel'] = channel
        if file is not None:
            optional_kwargs['file'] = file
        if file_comment is not None:
            optional_kwargs['file_comment'] = file_comment
        if timestamp is not None:
            optional_kwargs['timestamp'] = timestamp

        return BaseAPIEndpoint.__call__(self,
                                        name=name,
                                        **optional_kwargs
                                        )


@Reactions.register('get')
class ReactionsGet(BaseAPIEndpoint):
    """This method returns a list of all reactions for a single item (file, file comment, channel message, group message, or direct message).

    The response contains the item with reactions.

    .. code-block:: json

        {
            "type": "message",
            "channel": "C2147483705",
            "message": {
                ...
                "reactions": [
                    {
                        "name": "astonished",
                        "count": 3,
                        "users": [ "U1", "U2", "U3" ]
                    },
                    {
                        "name": "clock1"
                        "count": 2,
                        "users": [ "U1", "U2", "U3" ]
                    }
                ]
            },
        },

    Different item types can be reacted to. The item returned has a type property, the
    other properties depend on the type of item. The possible types are:

    message: the item will have a message property containing a message object and a channel property containing the channel ID for the message.
    file: this item will have a file property containing a file object.
    file_comment: the item will have a file property containing the file object and a comment property containing the file comment.

    The users array in the reactions property might not always contain all users that have reacted (we limit it to X users, and X might change), however count will always represent the count of all
    users who made that reaction (i.e. it may be greater than users.length). If the authenticated user has a given reaction then they are guaranteed to appear in the users array, regardless of
    whether count is greater than users.length or not. If the complete list of users is required they can still be obtained by specifying the full argument.

    For more information see https://api.slack.com/methods/get
    """
    endpoint = 'reactions.get'
    required_args = {}
    optional_args = {
        'channel',
        'file',
        'file_comment',
        'full',
        'timestamp',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reactions:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel=None,
                 file=None,
                 file_comment=None,
                 full=None,
                 timestamp=None,
                 ):
        """Gets reactions for an item.

        :param channel: Optional. Channel where the message to get reactions for was posted. e.g. C1234567890
        :param file: Optional. File to get reactions for. e.g. F1234567890
        :param file_comment: Optional. File comment to get reactions for. e.g. Fc1234567890
        :param full: Optional. If true always return the complete reaction list. e.g. true
        :param timestamp: Optional. Timestamp of the message to get reactions for. e.g. 1234567890.123456
        """
        optional_kwargs = {}
        if channel is not None:
            optional_kwargs['channel'] = channel
        if file is not None:
            optional_kwargs['file'] = file
        if file_comment is not None:
            optional_kwargs['file_comment'] = file_comment
        if full is not None:
            optional_kwargs['full'] = full
        if timestamp is not None:
            optional_kwargs['timestamp'] = timestamp

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Reactions.register('list')
class ReactionsList(BaseAPIEndpoint):
    """This method returns a list of all items (file, file comment, channel message, group message, or direct message) reacted to by a user.

    The response contains a list of items with reactions followed by pagination
    information.

    .. code-block:: json

        {
            "ok": true,
            "items": [
                {
                    "type": "message",
                    "channel": "C2147483705",
                    "message": {
                        ...
                        "reactions": [
                            {
                                "name": "astonished",
                                "count": 3,
                                "users": [ "U1", "U2", "U3" ]
                            },
                            {
                                "name": "clock1"
                                "count": 2,
                                "users": [ "U1", "U2", "U3" ]
                            }
                        ]
                    },
                },
                {
                    "type": "file",
                    "file": { ... },
                    "reactions": [
                        {
                            "name": "thumbsup",
                            "count": 1,
                            "users": [ "U1" ]
                        }
                    ]
                }
                {
                    "type": "file_comment",
                    "file": { ... },
                    "comment": { ... },
                    "reactions": [
                        {
                            "name": "facepalm",
                            "count": 1034,
                            "users": [ "U1", "U2", "U3", "U4", "U5" ]
                        }
                    ]
                }
            ],
            "paging": {
                "count": 100,
                "total": 4,
                "page": 1,
                "pages": 1
            }
        }

    Different item types can be reacted to. Every item in the list has a type property, the
    other properties depend on the type of item. The possible types are:

    message: the item will have a message property containing a message object and a channel property containing the channel ID for the message.
    file: this item will have a file property containing a file object.
    file_comment: the item will have a file property containing the file object and a comment property containing the file comment.

    The users array in the reactions property might not always contain all users that have reacted (we limit it to X users, and X might change), however count will always represent the count of all
    users who made that reaction (i.e. it may be greater than users.length). If the authenticated user has a given reaction then they are guaranteed to appear in the users array, regardless of
    whether count is greater than users.length or not. If the complete list of users is required they can still be obtained by specifying the full argument.
    The paging information contains the count of items returned, the total
    number of items reacted to, the page of results returned in this response and
    the total number of pages available. Please note that the max count value is 1000 and the max page value is 100.

    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'reactions.list'
    required_args = {}
    optional_args = {
        'count',
        'full',
        'page',
        'user',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reactions:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 count=None,
                 full=None,
                 page=None,
                 user=None,
                 ):
        """Lists reactions made by a user.

        :param count: Optional, default=100. Number of items to return per page. e.g. 20
        :param full: Optional. If true always return the complete reaction list. e.g. true
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        :param user: Optional. Show reactions made by this user. Defaults to the authed user. e.g. U1234567890
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if full is not None:
            optional_kwargs['full'] = full
        if page is not None:
            optional_kwargs['page'] = page
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Reactions.register('remove')
class ReactionsRemove(BaseAPIEndpoint):
    """This method removes a reaction (emoji) from an item (file, file comment, channel message, group message, or direct message).
    One of file, file_comment, or the combination of channel and timestamp must be specified.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call, the reaction is removed and a reaction_removed event is broadcast through the RTM API for the calling user.

    For more information see https://api.slack.com/methods/remove
    """
    endpoint = 'reactions.remove'
    required_args = {
        'name',
    }
    optional_args = {
        'channel',
        'file',
        'file_comment',
        'timestamp',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reactions:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name,
                 channel=None,
                 file=None,
                 file_comment=None,
                 timestamp=None,
                 ):
        """Removes a reaction from an item.

        :param name: Required. Reaction (emoji) name. e.g. thumbsup
        :param channel: Optional. Channel where the message to remove reaction from was posted. e.g. C1234567890
        :param file: Optional. File to remove reaction from. e.g. F1234567890
        :param file_comment: Optional. File comment to remove reaction from. e.g. Fc1234567890
        :param timestamp: Optional. Timestamp of the message to remove reaction from. e.g. 1234567890.123456
        """
        optional_kwargs = {}
        if channel is not None:
            optional_kwargs['channel'] = channel
        if file is not None:
            optional_kwargs['file'] = file
        if file_comment is not None:
            optional_kwargs['file_comment'] = file_comment
        if timestamp is not None:
            optional_kwargs['timestamp'] = timestamp

        return BaseAPIEndpoint.__call__(self,
                                        name=name,
                                        **optional_kwargs
                                        )
