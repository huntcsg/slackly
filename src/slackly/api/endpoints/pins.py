from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Pins(BaseAPIDispatch):
    pass


@Pins.register('add')
class PinsAdd(BaseAPIEndpoint):
    """This method pins an item (file, file comment, channel message, or group message) to a particular channel.
    The channel argument is required and one of file, file_comment, or timestamp must also be specified.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call the pin is saved to the database and a pin_added event is broadcast via the RTM API.

    For more information see https://api.slack.com/methods/add
    """
    endpoint = 'pins.add'
    required_args = {
        'channel',
    }
    optional_args = {
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
            'pins:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 file=None,
                 file_comment=None,
                 timestamp=None,
                 ):
        """Pins an item to a channel.

        :param channel: Required. Channel to pin the item in. e.g. C1234567890
        :param file: Optional. File to pin. e.g. F1234567890
        :param file_comment: Optional. File comment to pin. e.g. Fc1234567890
        :param timestamp: Optional. Timestamp of the message to pin. e.g. 1234567890.123456
        """
        optional_kwargs = {}
        if file is not None:
            optional_kwargs['file'] = file
        if file_comment is not None:
            optional_kwargs['file_comment'] = file_comment
        if timestamp is not None:
            optional_kwargs['timestamp'] = timestamp

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Pins.register('list')
class PinsList(BaseAPIEndpoint):
    """This method lists the items pinned to a channel.

    The response contains a list of pinned items in a channel.

    .. code-block:: json

        {
            "ok": true,
            "items": [
                {
                    "type": "message",
                    "channel": "C2147483705",
                    "message": {...},
                    "created": 1456335673,
                    "created_by": "U07BVMD97"
                },
                {
                    "type": "file",
                    "file": { ... },
                    "created": 1456335673,
                    "created_by": "U07BVMD97"
                },
                {
                    "type": "file_comment",
                    "file": { ... },
                    "comment": { ... },
                    "created": 1456335673,
                    "created_by": "U07BVMD97"
                }
            ]
        }

    Different item types can be pinned. Every item in the list has a type property, and the other properties depend on the type of item. The possible types are:

    message: the item will have a message property containing a message object and a channel property containing the channel ID for the message.
    file: this item will have a file property containing a file object.
    file_comment: the item will have a file property containing the file object and a comment property containing the file comment.

    The created property on each item is a unix timestamp representing when the item was pinned.
    The created_by property on each item is a string representing the encoded user id of the user who pinned the item.

    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'pins.list'
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
            'pins:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ):
        """Lists items pinned to a channel.

        :param channel: Required. Channel to get pinned items for. e.g. C1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )


@Pins.register('remove')
class PinsRemove(BaseAPIEndpoint):
    """This method un-pins an item (file, file comment, channel message, or group message) from a channel.
    The channel argument is required and one of file, file_comment, or timestamp must also be specified.


    .. code-block:: json

        {
            "ok": true
        }

    After making this call the pin is removed from the database and a pin_removed event is broadcast via the RTM API.

    For more information see https://api.slack.com/methods/remove
    """
    endpoint = 'pins.remove'
    required_args = {
        'channel',
    }
    optional_args = {
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
            'pins:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 file=None,
                 file_comment=None,
                 timestamp=None,
                 ):
        """Un-pins an item from a channel.

        :param channel: Required. Channel where the item is pinned to. e.g. C1234567890
        :param file: Optional. File to un-pin. e.g. F1234567890
        :param file_comment: Optional. File comment to un-pin. e.g. Fc1234567890
        :param timestamp: Optional. Timestamp of the message to un-pin. e.g. 1234567890.123456
        """
        optional_kwargs = {}
        if file is not None:
            optional_kwargs['file'] = file
        if file_comment is not None:
            optional_kwargs['file_comment'] = file_comment
        if timestamp is not None:
            optional_kwargs['timestamp'] = timestamp

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        **optional_kwargs
                                        )
