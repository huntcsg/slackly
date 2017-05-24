from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Usergroups(BaseAPIDispatch):
    pass


@Usergroups.register('users')
class Users(BaseAPIDispatch):
    pass


@Usergroups.register('create')
class UsergroupsCreate(BaseAPIEndpoint):
    """This method is used to create a User Group.

    If successful, the command returns a usergroup object, including preferences:

    .. code-block:: json

        {
            "ok": true,
            "usergroup": {
                "id": "S0615G0KT",
                "team_id": "T060RNRCH",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1446746793,
                "date_update": 1446746793,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060RNRCZ",
                "updated_by": "U060RNRCZ",
                "deleted_by": null,
                "prefs": {
                    "channels": [

                    ],
                    "groups": [

                    ]
                },
                "user_count": "0"
            }
        }


    For more information see https://api.slack.com/methods/create
    """
    endpoint = 'usergroups.create'
    required_args = {
        'name',
    }
    optional_args = {
        'channels',
        'description',
        'handle',
        'include_count',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name,
                 channels=None,
                 description=None,
                 handle=None,
                 include_count=None,
                 ):
        """Create a User Group

        :param name: Required. A name for the User Group. Must be unique among User Groups. e.g. My Test Team
        :param channels: Optional. A comma separated string of encoded channel IDs for which the User Group uses as a default. e.g. C1234567890,C2345678901,C3456789012
        :param description: Optional. A short description of the User Group. e.g.
        :param handle: Optional. A mention handle. Must be unique among channels, users and User Groups. e.g. marketing
        :param include_count: Optional. Include the number of users in each User Group. e.g. true
        """
        optional_kwargs = {}
        if channels is not None:
            optional_kwargs['channels'] = channels
        if description is not None:
            optional_kwargs['description'] = description
        if handle is not None:
            optional_kwargs['handle'] = handle
        if include_count is not None:
            optional_kwargs['include_count'] = include_count

        return BaseAPIEndpoint.__call__(self,
                                        name=name,
                                        **optional_kwargs
                                        )


@Usergroups.register('disable')
class UsergroupsDisable(BaseAPIEndpoint):
    """This method disables an existing User Group.


    .. code-block:: json

        {
            "ok": true,
            "usergroup": {
                "id": "S0615G0KT",
                "team_id": "T060RNRCH",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1446746793,
                "date_update": 1446747568,
                "date_delete": 1446747568,
                "auto_type": null,
                "created_by": "U060RNRCZ",
                "updated_by": "U060RNRCZ",
                "deleted_by": "U060RNRCZ",
                "prefs": {
                    "channels": [

                    ],
                    "groups": [

                    ]
                },
                "user_count": "0"
            }
        }

    When a User Group has been disabled its date_delete parameter will be non-zero.

    For more information see https://api.slack.com/methods/disable
    """
    endpoint = 'usergroups.disable'
    required_args = {
        'usergroup',
    }
    optional_args = {
        'include_count',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 usergroup,
                 include_count=None,
                 ):
        """Disable an existing User Group

        :param usergroup: Required. The encoded ID of the User Group to disable. e.g. S0604QSJC
        :param include_count: Optional. Include the number of users in the User Group. e.g. true
        """
        optional_kwargs = {}
        if include_count is not None:
            optional_kwargs['include_count'] = include_count

        return BaseAPIEndpoint.__call__(self,
                                        usergroup=usergroup,
                                        **optional_kwargs
                                        )


@Usergroups.register('enable')
class UsergroupsEnable(BaseAPIEndpoint):
    """This method enables a User Group which was previously disabled.


    .. code-block:: json

        {
            "ok": true,
            "usergroup": {
                "id": "S0615G0KT",
                "team_id": "T060RNRCH",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1446746793,
                "date_update": 1446747767,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060RNRCZ",
                "updated_by": "U060RNRCZ",
                "deleted_by": null,
                "prefs": {
                    "channels": [

                    ],
                    "groups": [

                    ]
                },
                "user_count": "0"
            }
        }

    When a User Group is enabled, it's date_delete parameter will be 0 (zero).

    For more information see https://api.slack.com/methods/enable
    """
    endpoint = 'usergroups.enable'
    required_args = {
        'usergroup',
    }
    optional_args = {
        'include_count',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 usergroup,
                 include_count=None,
                 ):
        """Enable a User Group

        :param usergroup: Required. The encoded ID of the User Group to enable. e.g. S0604QSJC
        :param include_count: Optional. Include the number of users in the User Group. e.g. true
        """
        optional_kwargs = {}
        if include_count is not None:
            optional_kwargs['include_count'] = include_count

        return BaseAPIEndpoint.__call__(self,
                                        usergroup=usergroup,
                                        **optional_kwargs
                                        )


@Usergroups.register('list')
class UsergroupsList(BaseAPIEndpoint):
    """This method returns a list of all User Groups in the team. This can optionally include disabled User Groups.

    Returns a list of usergroup objects, in no particular order:

    .. code-block:: json

        {
            "ok": true,
            "usergroups": [
                {
                    "id": "S0614TZR7",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Team Admins",
                    "description": "A group of all Administrators on your team.",
                    "handle": "admins",
                    "is_external": false,
                    "date_create": 1446598059,
                    "date_update": 1446670362,
                    "date_delete": 0,
                    "auto_type": "admin",
                    "created_by": "USLACKBOT",
                    "updated_by": "U060RNRCZ",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [

                        ],
                        "groups": [

                        ]
                    },
                    "user_count": "2"
                },
                {
                    "id": "S06158AV7",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Team Owners",
                    "description": "A group of all Owners on your team.",
                    "handle": "owners",
                    "is_external": false,
                    "date_create": 1446678371,
                    "date_update": 1446678371,
                    "date_delete": 0,
                    "auto_type": "owner",
                    "created_by": "USLACKBOT",
                    "updated_by": "USLACKBOT",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [

                        ],
                        "groups": [

                        ]
                    },
                    "user_count": "1"
                },
                {
                    "id": "S0615G0KT",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Marketing Team",
                    "description": "Marketing gurus, PR experts and product advocates.",
                    "handle": "marketing-team",
                    "is_external": false,
                    "date_create": 1446746793,
                    "date_update": 1446747767,
                    "date_delete": 1446748865,
                    "auto_type": null,
                    "created_by": "U060RNRCZ",
                    "updated_by": "U060RNRCZ",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [

                        ],
                        "groups": [

                        ]
                    },
                    "user_count": "0"
                }
            ]
        }


    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'usergroups.list'
    required_args = {}
    optional_args = {
        'include_count',
        'include_disabled',
        'include_users',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 include_count=None,
                 include_disabled=None,
                 include_users=None,
                 ):
        """List all User Groups for a team

        :param include_count: Optional. Include the number of users in each User Group. e.g. true
        :param include_disabled: Optional. Include disabled User Groups. e.g. true
        :param include_users: Optional. Include the list of users for each User Group. e.g. true
        """
        optional_kwargs = {}
        if include_count is not None:
            optional_kwargs['include_count'] = include_count
        if include_disabled is not None:
            optional_kwargs['include_disabled'] = include_disabled
        if include_users is not None:
            optional_kwargs['include_users'] = include_users

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Usergroups.register('update')
class UsergroupsUpdate(BaseAPIEndpoint):
    """This method updates the properties of an existing User Group.


    .. code-block:: json

        {
            "ok": true,
            "usergroup": {
                "id": "S0615G0KT",
                "team_id": "T060RNRCH",
                "is_usergroup": true,
                "name": "Marketing Gurus",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1446746793,
                "date_update": 1446748574,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060RNRCZ",
                "updated_by": "U060RNRCZ",
                "deleted_by": null,
                "prefs": {
                    "channels": [

                    ],
                    "groups": [

                    ]
                },
                "user_count": "0"
            }
        }


    For more information see https://api.slack.com/methods/update
    """
    endpoint = 'usergroups.update'
    required_args = {
        'usergroup',
    }
    optional_args = {
        'channels',
        'description',
        'handle',
        'include_count',
        'name',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 usergroup,
                 channels=None,
                 description=None,
                 handle=None,
                 include_count=None,
                 name=None,
                 ):
        """Update an existing User Group

        :param usergroup: Required. The encoded ID of the User Group to update. e.g. S0604QSJC
        :param channels: Optional. A comma separated string of encoded channel IDs for which the User Group uses as a default. e.g. C1234567890,C2345678901,C3456789012
        :param description: Optional. A short description of the User Group. e.g.
        :param handle: Optional. A mention handle. Must be unique among channels, users and User Groups. e.g. marketing
        :param include_count: Optional. Include the number of users in the User Group. e.g. true
        :param name: Optional. A name for the User Group. Must be unique among User Groups. e.g. My Test Team
        """
        optional_kwargs = {}
        if channels is not None:
            optional_kwargs['channels'] = channels
        if description is not None:
            optional_kwargs['description'] = description
        if handle is not None:
            optional_kwargs['handle'] = handle
        if include_count is not None:
            optional_kwargs['include_count'] = include_count
        if name is not None:
            optional_kwargs['name'] = name

        return BaseAPIEndpoint.__call__(self,
                                        usergroup=usergroup,
                                        **optional_kwargs
                                        )


@Users.register('list')
class UsersList(BaseAPIEndpoint):
    """This method returns a list of all users within a User Group.


    .. code-block:: json

        {
            "ok": true,
            "users": [
                "U060R4BJ4"
            ]
        }


    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'usergroups.users.list'
    required_args = {
        'usergroup',
    }
    optional_args = {
        'include_disabled',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 usergroup,
                 include_disabled=None,
                 ):
        """List all users in a User Group

        :param usergroup: Required. The encoded ID of the User Group to update. e.g. S0604QSJC
        :param include_disabled: Optional. Allow results that involve disabled User Groups. e.g. true
        """
        optional_kwargs = {}
        if include_disabled is not None:
            optional_kwargs['include_disabled'] = include_disabled

        return BaseAPIEndpoint.__call__(self,
                                        usergroup=usergroup,
                                        **optional_kwargs
                                        )


@Users.register('update')
class UsersUpdate(BaseAPIEndpoint):
    """This method updates the list of users that belong to a User Group. This method replaces all users in a User Group with the list of users provided in the users parameter.


    .. code-block:: json

        {
            "ok": true,
            "usergroup": {
                "id": "S0616NG6M",
                "team_id": "T060R4BHN",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1447096577,
                "date_update": 1447102109,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060R4BJ4",
                "updated_by": "U060R4BJ4",
                "deleted_by": null,
                "prefs": {
                    "channels": [

                    ],
                    "groups": [

                    ]
                },
                "users": [
                    "U060R4BJ4",
                    "U060RNRCZ"
                ],
                "user_count": 1
            }
        }


    For more information see https://api.slack.com/methods/update
    """
    endpoint = 'usergroups.users.update'
    required_args = {
        'usergroup',
        'users',
    }
    optional_args = {
        'include_count',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'usergroups:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 usergroup,
                 users,
                 include_count=None,
                 ):
        """Update the list of users for a User Group

        :param usergroup: Required. The encoded ID of the User Group to update. e.g. S0604QSJC
        :param users: Required. A comma separated string of encoded user IDs that represent the entire list of users for the User Group. e.g. U060R4BJ4,U060RNRCZ
        :param include_count: Optional. Include the number of users in the User Group. e.g. true
        """
        optional_kwargs = {}
        if include_count is not None:
            optional_kwargs['include_count'] = include_count

        return BaseAPIEndpoint.__call__(self,
                                        usergroup=usergroup,
                                        users=users,
                                        **optional_kwargs
                                        )
