from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Chat(BaseAPIDispatch):
    pass


@Chat.register('delete')
class ChatDelete(BaseAPIEndpoint):
    """This method deletes a message from a channel.


    .. code-block:: json

        {
            "ok": true,
            "channel": "C024BE91L",
            "ts": "1401383885.000061"
        }

    The response includes the channel and timestamp properties of the deleted
    message.

    For more information see https://api.slack.com/methods/delete
    """
    endpoint = 'chat.delete'
    required_args = {
        'channel',
        'ts',
    }
    optional_args = {
        'as_user',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': {
            'chat:write:bot',
        },
        'user': {
            'chat:write:user',
        },
    }

    def __call__(self,
                 channel,
                 ts,
                 as_user=None,
                 ):
        """Deletes a message.

        :param channel: Required. Channel containing the message to be deleted. e.g. C1234567890
        :param ts: Required. Timestamp of the message to be deleted. e.g. 1405894322.002768
        :param as_user: Optional. Pass true to delete the message as the authed user. Bot users in this context are considered authed users. e.g. true
        """
        optional_kwargs = {}
        if as_user is not None:
            optional_kwargs['as_user'] = as_user

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        ts=ts,
                                        **optional_kwargs
                                        )


@Chat.register('meMessage')
class ChatMeMessage(BaseAPIEndpoint):
    """This method sends a me message to a channel from the calling user.


    .. code-block:: json

        {
            "ok": true,
            "channel": "C024BE7LR",
            "ts": "1417671948.000006"
        }


    For more information see https://api.slack.com/methods/meMessage
    """
    endpoint = 'chat.meMessage'
    required_args = {
        'channel',
        'text',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'chat:write:user',
        },
    }

    def __call__(self,
                 channel,
                 text,
                 ):
        """Share a me message into a channel.

        :param channel: Required. Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name. e.g. C1234567890
        :param text: Required. Text of the message to send. e.g. Hello world
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        text=text,
                                        **optional_kwargs
                                        )


@Chat.register('postMessage')
class ChatPostMessage(BaseAPIEndpoint):
    """This method posts a message to a public channel, private channel, or direct message/IM channel.


    .. code-block:: json

        {
            "ok": true,
            "ts": "1405895017.000506",
            "channel": "C024BE91L",
            "message": {
                ...
            }
        }

    The response includes the timestamp (ts) and channel for the posted message. It also
    includes the complete message object, as it was parsed by our servers. This
    may differ from the provided arguments as our servers sanitize links,
    attachments and other properties.

    For more information see https://api.slack.com/methods/postMessage
    """
    endpoint = 'chat.postMessage'
    required_args = {
        'channel',
        'text',
    }
    optional_args = {
        'as_user',
        'attachments',
        'icon_emoji',
        'icon_url',
        'link_names',
        'parse',
        'reply_broadcast',
        'thread_ts',
        'unfurl_links',
        'unfurl_media',
        'username',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': {
            'chat:write:bot',
        },
        'user': {
            'chat:write:user',
        },
    }

    def __call__(self,
                 channel,
                 text,
                 as_user=None,
                 attachments=None,
                 icon_emoji=None,
                 icon_url=None,
                 link_names=None,
                 parse=None,
                 reply_broadcast=None,
                 thread_ts=None,
                 unfurl_links=None,
                 unfurl_media=None,
                 username=None,
                 ):
        """Sends a message to a channel.

        :param channel: Required. Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See below for more details. e.g. C1234567890
        :param text: Required. Text of the message to send. See below for an explanation of formatting. This field is usually required, unless you're providing only attachments instead. e.g. Hello world
        :param as_user: Optional. Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See authorship below. e.g. true
        :param attachments: Optional. Structured message attachments. e.g. [{"pretext": "pre-hello", "text": "text-world"}]
        :param icon_emoji: Optional. Emoji to use as the icon for this message. Overrides icon_url. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below. e.g. :chart_with_upwards_trend:
        :param icon_url: Optional. URL to an image to use as the icon for this message. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below. e.g. http://lorempixel.com/48/48
        :param link_names: Optional. Find and link channel names and usernames. e.g. true
        :param parse: Optional. Change how messages are treated. Defaults to none. See below. e.g. full
        :param reply_broadcast: Optional. Used in conjunction with thread_ts and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to false. e.g. true
        :param thread_ts: Optional. Provide another message's ts value to make this message a reply. Avoid using a reply's ts value; use its parent instead. e.g. 1234567890.123456
        :param unfurl_links: Optional. Pass true to enable unfurling of primarily text-based content. e.g. true
        :param unfurl_media: Optional. Pass false to disable unfurling of media content. e.g. false
        :param username: Optional. Set your bot's user name. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below. e.g. My Bot
        """
        optional_kwargs = {}
        if as_user is not None:
            optional_kwargs['as_user'] = as_user
        if attachments is not None:
            optional_kwargs['attachments'] = attachments
        if icon_emoji is not None:
            optional_kwargs['icon_emoji'] = icon_emoji
        if icon_url is not None:
            optional_kwargs['icon_url'] = icon_url
        if link_names is not None:
            optional_kwargs['link_names'] = link_names
        if parse is not None:
            optional_kwargs['parse'] = parse
        if reply_broadcast is not None:
            optional_kwargs['reply_broadcast'] = reply_broadcast
        if thread_ts is not None:
            optional_kwargs['thread_ts'] = thread_ts
        if unfurl_links is not None:
            optional_kwargs['unfurl_links'] = unfurl_links
        if unfurl_media is not None:
            optional_kwargs['unfurl_media'] = unfurl_media
        if username is not None:
            optional_kwargs['username'] = username

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        text=text,
                                        **optional_kwargs
                                        )


@Chat.register('unfurl')
class ChatUnfurl(BaseAPIEndpoint):
    """This method attaches Slack app unfurl behavior to a specified and relevant message. A user token is required as this method does not support bot user tokens.



    The first time this method is executed with a particular ts and channel combination, the valid unfurls attachments you provide will be attached to the message. Subsequent attempts with the same ts and channel values will modify the same attachments, rather than adding more.


    .. code-block:: json

        {
            "ok": true
        }

    As you can see, we provide a minimal positive response when your unfurl attempt is successful. When it is not, you'll receive one of the errors below and ok will not be false.

    For more information see https://api.slack.com/methods/unfurl
    """
    endpoint = 'chat.unfurl'
    required_args = {
        'channel',
        'ts',
        'unfurls',
    }
    optional_args = {
        'user_auth_required',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'links:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel,
                 ts,
                 unfurls,
                 user_auth_required=None,
                 ):
        """Unfurl a URL that a user posted

        :param channel: Required. Channel ID of the message e.g. C1234567890
        :param ts: Required. Timestamp of the message to add unfurl behavior to e.g.
        :param unfurls: Required. JSON mapping a set of URLs from the message to their unfurl attachments e.g.
        :param user_auth_required: Optional, default=0. Set to true or 1 to indicate the user must install your Slack app to trigger unfurls for this domain e.g. true
        """
        optional_kwargs = {}
        if user_auth_required is not None:
            optional_kwargs['user_auth_required'] = user_auth_required

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        ts=ts,
                                        unfurls=unfurls,
                                        **optional_kwargs
                                        )


@Chat.register('update')
class ChatUpdate(BaseAPIEndpoint):
    """This method updates a message in a channel. Though related to chat.postMessage, some parameters of chat.update are handled differently.


    .. code-block:: json

        {
                "ok": true,
                "channel": "C024BE91L",
                "ts": "1401383885.000061",
                "text": "Updated Text"
            }
    The response includes the text, channel and timestamp properties of the
    updated message so clients can keep their local copies of the message in sync.

    Bot users
    To use chat.update with a bot user token, you'll need to think of your bot user as a user, and pass as_user set to true while editing a message created by that same bot user.

    Interactive messages with buttons
    If you're posting message with buttons, you may use chat.update to continue updating ongoing state changes around a message. Provide the ts field the message you're updating and follow the bot user instructions above to update message text, remove or add attachments and actions.

    For more information see https://api.slack.com/methods/update
    """
    endpoint = 'chat.update'
    required_args = {
        'channel',
        'text',
        'ts',
    }
    optional_args = {
        'as_user',
        'attachments',
        'link_names',
        'parse',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': {
            'chat:write:bot',
        },
        'user': {
            'chat:write:user',
        },
    }

    def __call__(self,
                 channel,
                 text,
                 ts,
                 as_user=None,
                 attachments=None,
                 link_names=None,
                 parse=None,
                 ):
        """Updates a message.

        :param channel: Required. Channel containing the message to be updated. e.g. C1234567890
        :param text: Required. New text for the message, using the default formatting rules. e.g. Hello world
        :param ts: Required. Timestamp of the message to be updated. e.g. 1405894322.002768
        :param as_user: Optional. Pass true to update the message as the authed user. Bot users in this context are considered authed users. e.g. true
        :param attachments: Optional. Structured message attachments. e.g. [{"pretext": "pre-hello", "text": "text-world"}]
        :param link_names: Optional. Find and link channel names and usernames. Defaults to none. This parameter should be used in conjunction with parse. To set link_names to 1, specify a parse mode of full. e.g. true
        :param parse: Optional. Change how messages are treated. Defaults to client, unlike chat.postMessage. See below. e.g. none
        """
        optional_kwargs = {}
        if as_user is not None:
            optional_kwargs['as_user'] = as_user
        if attachments is not None:
            optional_kwargs['attachments'] = attachments
        if link_names is not None:
            optional_kwargs['link_names'] = link_names
        if parse is not None:
            optional_kwargs['parse'] = parse

        return BaseAPIEndpoint.__call__(self,
                                        channel=channel,
                                        text=text,
                                        ts=ts,
                                        **optional_kwargs
                                        )
