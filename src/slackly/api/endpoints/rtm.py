from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Rtm(BaseAPIDispatch):
    pass


@Rtm.register('connect')
class RtmConnect(BaseAPIEndpoint):
    """This method begins a Real Time Messaging API session and reserves your application a specific URL with which to connect via websocket.



    Unlike rtm.start, this method is focused only on connecting to the RTM API.



    Use this method in conjunction with other Web API methods like channels.list, users.list, and team.info to build a full picture of the team or workspace you're connecting on behalf of.



    Please consult the RTM API documentation for full details on using the RTM API.

    This method returns a WebSocket Message Server URL and limited information about the team:

    .. code-block:: json

        {
            "ok": true,
            "url": "wss:\/\/ms9.slack-msgs.com\/websocket\/2I5yBpcvk",
            "team": {
                "id": "T654321",
                "name": "Librarian Society of Soledad",
                "domain": "libsocos",
                "enterprise_id": "E234567",
                "enterprise_name": "Intercontinental Librarian Society"
            },
            "self": {
                "id": "W123456",
                "name": "brautigan"
            }
        }

    The url property contains a WebSocket Message Server URL. Connecting to this
    URL will initiate a Real Time Messaging session. These URLs are only valid for
    30 seconds, so connect quickly!
    The self property contains a small amount of information concerning the connecting user &mdash; an id and their name.
    The team attribute also houses brief information about the team, including its id, name, domain, and if it's part of an Enterprise Grid, the corresponding enteprise_id.

    For more information see https://api.slack.com/methods/connect
    """
    endpoint = 'rtm.connect'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Starts a Real Time Messaging session.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Rtm.register('start')
class RtmStart(BaseAPIEndpoint):
    """This method begins a Real Time Messaging API session and reserves your application a specific URL with which to connect via websocket.



    It's user-centric and team-centric: your app connects as a specific user or bot user on a specific team. Many apps will find the Events API's subscription model more scalable when working against multiple teams.



    This method also returns a smorgasbord of data about the team, its channels, and members. Some times more information than can be provided in a timely or helpful manner.



    Please use rtm.connect instead, especially when connecting on behalf of an Enterprise Grid customer.



    Consult the RTM API documentation for full details on using the RTM API. You'll also find our changelog entry useful.

    This method returns lots of data about the current state of a team, along
    with a WebSocket Message Server URL:

    .. code-block:: json

        {
            "ok": true,
            "url": "wss:\/\/ms9.slack-msgs.com\/websocket\/7I5yBpcvk",

            "self": {
                "id": "U023BECGF",
                "name": "bobby",
                "prefs": {
                    ...
                },
                "created": 1402463766,
                "manual_presence": "active"
            },
            "team": {
                "id": "T024BE7LD",
                "name": "Example Team",
                "email_domain": "",
                "domain": "example",
                "icon": {
                    ...
                },
                "msg_edit_window_mins": -1,
                "over_storage_limit": false
                "prefs": {
                    ...
                },
                "plan": "std"
            },
            "users": [ ... ],

            "channels": [ ... ],
            "groups": [ ... ],
            "mpims": [ ... ],
            "ims": [ ... ],

            "bots": [ ... ],
        }

    The url property contains a WebSocket Message Server URL. Connecting to this
    URL will initiate a Real Time Messaging session. These URLs are only valid for
    30 seconds, so connect quickly!
    The self property contains details on the authenticated user.
    The team property contains details on the authenticated user's team. If a team has
    not yet set a custom icon, the value of team.icon.image_default will be true.
    The users property contains a list of user objects, one for every
    member of the team.
    The channels property is a list of channel objects, one
    for every channel visible to the authenticated user. For regular or
    administrator accounts this list will include every team channel. The
    is_member property indicates if the user is a member of this channel. If
    true then the channel object will also include the topic, purpose, member
    list and read-state related information. The latest attribute is deprecated and will soon be removed from this method's response. See this changelog entry.
    The groups property is a list of group objects, one for
    every group the authenticated user is in.
    The mpims property is a list of mpims objects, one for
    every group the authenticated user is in.  MPIMs are only returned to the client
    if mpim_aware is set when calling rtm.start.  Otherwise, mpims are emulated
    using the groups API.
    The ims property is a list of
    IM objects, one for every direct message channel visible to the
    authenticated user.
    The bots property gives details of the integrations set up on this team.

    For more information see https://api.slack.com/methods/start
    """
    endpoint = 'rtm.start'
    required_args = {}
    optional_args = {
        'mpim_aware',
        'no_latest',
        'no_unreads',
        'simple_latest',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 mpim_aware=None,
                 no_latest=None,
                 no_unreads=None,
                 simple_latest=None,
                 ):
        """Starts a Real Time Messaging session.

        :param mpim_aware: Optional. Returns MPIMs to the client in the API response. e.g. true
        :param no_latest: Optional, default=0. Exclude latest timestamps for channels, groups, mpims, and ims. Automatically sets no_unreads to 1 e.g. 1
        :param no_unreads: Optional. Skip unread counts for each channel (improves performance). e.g. true
        :param simple_latest: Optional. Return timestamp only for latest message object of each channel (improves performance). e.g. true
        """
        optional_kwargs = {}
        if mpim_aware is not None:
            optional_kwargs['mpim_aware'] = mpim_aware
        if no_latest is not None:
            optional_kwargs['no_latest'] = no_latest
        if no_unreads is not None:
            optional_kwargs['no_unreads'] = no_unreads
        if simple_latest is not None:
            optional_kwargs['simple_latest'] = simple_latest

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
