from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Dnd(BaseAPIDispatch):
    pass


@Dnd.register('endDnd')
class DndEndDnd(BaseAPIEndpoint):
    """Ends the user's currently scheduled Do Not Disturb session immediately.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/endDnd
    """
    endpoint = 'dnd.endDnd'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'dnd:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Ends the current user's Do Not Disturb session immediately.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Dnd.register('endSnooze')
class DndEndSnooze(BaseAPIEndpoint):
    """Ends the current user's snooze mode immediately.


    .. code-block:: json

        {
            "ok": true,
            "dnd_enabled": true,
            "next_dnd_start_ts": 1450418400,
            "next_dnd_end_ts": 1450454400,
            "snooze_enabled": false
        }


    For more information see https://api.slack.com/methods/endSnooze
    """
    endpoint = 'dnd.endSnooze'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'dnd:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Ends the current user's snooze mode immediately.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Dnd.register('info')
class DndInfo(BaseAPIEndpoint):
    """Provides information about a user's current Do Not Disturb settings.


    .. code-block:: json

        {
            "ok": true,
            "dnd_enabled": true,
            "next_dnd_start_ts": 1450416600,
            "next_dnd_end_ts": 1450452600,
            "snooze_enabled": true,
            "snooze_endtime": 1450416600,
            "snooze_remaining": 1196
        }


    Snooze properties
    All of the snooze_* properties will only be visible if the user being queried is also the current user.
    The snooze_endtime and snooze_remaining properties will only be returned if snooze_enabled is true.

    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'dnd.info'
    required_args = {}
    optional_args = {
        'user',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'dnd:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 user=None,
                 ):
        """Retrieves a user's current Do Not Disturb status.

        :param user: Optional. User to fetch status for (defaults to current user) e.g. U1234
        """
        optional_kwargs = {}
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Dnd.register('setSnooze')
class DndSetSnooze(BaseAPIEndpoint):
    """Adjusts the snooze duration for a user's Do Not Disturb settings. If a snooze session is not already active for the user, invoking this method will begin one for the specified duration.


    .. code-block:: json

        {
            "ok": true,
            "snooze_enabled": true,
            "snooze_endtime": 1450373897,
            "snooze_remaining": 60,
        }

    The snooze_remaining field is expressed in seconds. If your request presents a num_minutes value of 1, the response's snooze_remaining will be 60.

    For more information see https://api.slack.com/methods/setSnooze
    """
    endpoint = 'dnd.setSnooze'
    required_args = {
        'num_minutes',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'dnd:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 num_minutes,
                 ):
        """Turns on Do Not Disturb mode for the current user, or changes its duration.

        :param num_minutes: Required. Number of minutes, from now, to snooze until. e.g. 60
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        num_minutes=num_minutes,
                                        **optional_kwargs
                                        )


@Dnd.register('teamInfo')
class DndTeamInfo(BaseAPIEndpoint):
    """Provides information about the current Do Not Disturb settings for users of a Slack team.


    .. code-block:: json

        {
            "ok": true,
            "users": {
                "U023BECGF": {
                    "dnd_enabled": true,
                    "next_dnd_start_ts": 1450387800,
                    "next_dnd_end_ts": 1450423800
                },
                "U058CJVAA": {
                    "dnd_enabled": false,
                    "next_dnd_start_ts": 1,
                    "next_dnd_end_ts": 1
                }
            }
        }


    For more information see https://api.slack.com/methods/teamInfo
    """
    endpoint = 'dnd.teamInfo'
    required_args = {}
    optional_args = {
        'users',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'dnd:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 users=None,
                 ):
        """Retrieves the Do Not Disturb status for users on a team.

        :param users: Optional. Comma-separated list of users to fetch Do Not Disturb status for e.g. U1234,U4567
        """
        optional_kwargs = {}
        if users is not None:
            optional_kwargs['users'] = users

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
