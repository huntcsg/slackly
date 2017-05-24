from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Stars(BaseAPIDispatch):
    pass


@Stars.register('add')
class StarsAdd(BaseAPIEndpoint):
    """This method adds a star to an item (message, file, file comment, channel, private group, or DM) on behalf of the authenticated user.
    One of file, file_comment, channel, or the combination of channel and timestamp must be specified.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call, the item will be starred and a star_added event is broadcast through the RTM API for the calling user.

    For more information see https://api.slack.com/methods/add
    """
    endpoint = 'stars.add'
    required_args = {}
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
            'stars:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel=None,
                 file=None,
                 file_comment=None,
                 timestamp=None,
                 ):
        """Adds a star to an item.

        :param channel: Optional. Channel to add star to, or channel where the message to add star to was posted (used with timestamp). e.g. C1234567890
        :param file: Optional. File to add star to. e.g. F1234567890
        :param file_comment: Optional. File comment to add star to. e.g. Fc1234567890
        :param timestamp: Optional. Timestamp of the message to add star to. e.g. 1234567890.123456
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
                                        **optional_kwargs
                                        )


@Stars.register('list')
class StarsList(BaseAPIEndpoint):
    """This method lists the items starred by the authed user.

    The response contains a list of starred items followed by pagination
    information.

    .. code-block:: json

        {
            "ok": true,
            "items": [
                {
                    "type": "message",
                    "channel": "C2147483705",
                    "message": {...}
                },
                {
                    "type": "file",
                    "file": { ... }
                }
                {
                    "type": "file_comment",
                    "file": { ... },
                    "comment": { ... }
                }
                {
                    "type": "channel",
                    "channel": "C2147483705"
                },

            ],
            "paging": {
                "count": 100,
                "total": 4,
                "page": 1,
                "pages": 1
            }
        }

    Different item types can be starred. Every item in the list has a type property, the
    other property depend on the type of item. The possible types are:

    message: the item will have a message property containing a message object
    file: this item will have a file property containing a file object.
    file_comment: the item will have a file property containing the file object and a comment property containing the file comment.
    channel: the item will have a channel property containing the channel ID.
    im: the item will have a channel property containing the channel ID for this direct message.
    group: the item will have a group property containing the channel ID for the private group.

    The paging information contains the count of files returned, the total
    number of items starred, the page of results returned in this response and
    the total number of pages available. Please note that the max count value is 1000 and the max page value is 100.

    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'stars.list'
    required_args = {}
    optional_args = {
        'count',
        'page',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'stars:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 count=None,
                 page=None,
                 ):
        """Lists stars for a user.

        :param count: Optional, default=100. Number of items to return per page. e.g. 20
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if page is not None:
            optional_kwargs['page'] = page

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Stars.register('remove')
class StarsRemove(BaseAPIEndpoint):
    """This method removes a star from an item (message, file, file comment, channel, private group, or DM) on behalf of the authenticated user.
    One of file, file_comment, channel, or the combination of channel and timestamp must be specified.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call, the item will be unstarred and a star_removed event is broadcast through the RTM API for the calling user.

    For more information see https://api.slack.com/methods/remove
    """
    endpoint = 'stars.remove'
    required_args = {}
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
            'stars:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel=None,
                 file=None,
                 file_comment=None,
                 timestamp=None,
                 ):
        """Removes a star from an item.

        :param channel: Optional. Channel to remove star from, or channel where the message to remove star from was posted (used with timestamp). e.g. C1234567890
        :param file: Optional. File to remove star from. e.g. F1234567890
        :param file_comment: Optional. File comment to remove star from. e.g. Fc1234567890
        :param timestamp: Optional. Timestamp of the message to remove star from. e.g. 1234567890.123456
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
                                        **optional_kwargs
                                        )
