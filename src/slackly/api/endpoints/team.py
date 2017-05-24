from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Team(BaseAPIDispatch):
    pass


@Team.register('profile')
class Profile(BaseAPIDispatch):
    pass


@Team.register('accessLogs')
class TeamAccessLogs(BaseAPIEndpoint):
    """This method is used to get the access logs for users on a team.

    The response contains a list of logins followed by pagination
    information.

    .. code-block:: json

        {
            "ok": true,
            "logins": [
                {
                    "user_id": "U12345",
                    "username": "bob",
                    "date_first": 1422922864,
                    "date_last": 1422922864,
                    "count": 1,
                    "ip": "127.0.0.1",
                    "user_agent": "SlackWeb Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/41.0.2272.35 Safari\/537.36",
                    "isp": "BigCo ISP",
                    "country": "US",
                    "region": "CA"
                },
                {
                    "user_id": "U45678",
                    "username": "alice",
                    "date_first": 1422922493,
                    "date_last": 1422922493,
                    "count": 1,
                    "ip": "127.0.0.1",
                    "user_agent": "SlackWeb Mozilla\/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit\/600.1.4 (KHTML, like Gecko) Version\/8.0 Mobile\/12B466 Safari\/600.1.4",
                    "isp": "BigCo ISP",
                    "country": "US",
                    "region": "CA"
                },
            ],
            "paging": {
                "count": 100,
                "total": 2,
                "page": 1,
                "pages": 1
            }
        }

    Each login contains the user id and username that logged in. date_first is a unix timestamp of the first login for this user/ip/user_agent combination.
    date_last is the most recent for that combination. count is the total number of logins for that combination. ip is the ip address of the device used
    to login. user_agent is the reported user agent string from the browser or client application. isp is our best guess at the internet service provider who
    owns the ip address. country and region are similarly where we think that login came from, based on the ip address.
    The paging information contains the count of items returned, the total number of items reacted to, the page of results returned in this response and
    the total number of pages available. Please note that the max count value is 1000 and the max page value is 100.

    For more information see https://api.slack.com/methods/accessLogs
    """
    endpoint = 'team.accessLogs'
    required_args = {}
    optional_args = {
        'before',
        'count',
        'page',
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
                 before=None,
                 count=None,
                 page=None,
                 ):
        """Gets the access logs for the current team.

        :param before: Optional, default=now. End of time range of logs to include in results (inclusive). e.g. 1457989166
        :param count: Optional, default=100. Number of items to return per page. e.g. 20
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        """
        optional_kwargs = {}
        if before is not None:
            optional_kwargs['before'] = before
        if count is not None:
            optional_kwargs['count'] = count
        if page is not None:
            optional_kwargs['page'] = page

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Team.register('billableInfo')
class TeamBillableInfo(BaseAPIEndpoint):
    """This method lists billable information for each user on the team. Currently this consists solely of whether the user is
    subject to billing per Slack's Fair Billing policy.

    The response contains a list of activity logs followed by pagination
    information.

    .. code-block:: json

        {
            "ok": true,
            "billable_info": {
                "U0632EWRW": {
                    "billing_active": false
                },
                "U02UCPE1R": {
                    "billing_active": true
                },
                "U02UEBSD2": {
                    "billing_active": true
                }
            }
        }

    A billing_active status of true indicates that the user is eligible per billing per Slack's Fair Billing policy.
    The billing_active status is computed periodically and the values returned by this API reflect the most recently
    computed status and should not be interpreted as a real-time view of each user's billing_active status.

    For more information see https://api.slack.com/methods/billableInfo
    """
    endpoint = 'team.billableInfo'
    required_args = {}
    optional_args = {
        'user',
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
                 user=None,
                 ):
        """Gets billable users information for the current team.

        :param user: Optional. A user to retrieve the billable information for. Defaults to all users. e.g. U1234567890
        """
        optional_kwargs = {}
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Team.register('info')
class TeamInfo(BaseAPIEndpoint):
    """This method provides information about your team.


    .. code-block:: json

         {
             "ok": true,
             "team": {
                 "id": "T12345",
                 "name": "My Team",
                 "domain": "example",
                 "email_domain": "example.com",
                 "icon": {
                     "image_34": "https:\/\/...",
                     "image_44": "https:\/\/...",
                     "image_68": "https:\/\/...",
                     "image_88": "https:\/\/...",
                     "image_102": "https:\/\/...",
                     "image_132": "https:\/\/...",
                     "image_default": true
                 },
                "enterprise_id": "E1234A12AB",
                "enterprise_name": "Umbrella Corporation"
             }
         }


    Team Icon
    If a team has not yet set a custom icon, the value of team.icon.image_default will be true.
    If the team belongs to an Enterprise Grid, the enterprise_id and enterprise_name fields will indicate the owning enterprise organization.

    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'team.info'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'team:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Gets information about the current team.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Team.register('integrationLogs')
class TeamIntegrationLogs(BaseAPIEndpoint):
    """This method lists the integration activity logs for a team, including when integrations are added, modified and removed. This method can only be called by Admins.

    The response contains a list of activity logs followed by pagination
    information.

    .. code-block:: json

        {
            "ok": true,
            "logs": [
                {
                    "service_id": "1234567890",
                    "service_type": "Google Calendar",
                    "user_id": "U1234ABCD",
                    "user_name": "Johnny",
                    "channel": "C1234567890",
                    "date": "1392163200",
                    "change_type": "enabled",
                    "scope": "incoming-webhook"
                },
                {
                    "app_id": "2345678901",
                    "app_type": "Johnny App"
                    "user_id": "U2345BCDE",
                    "user_name": "Billy",
                    "date": "1392163201",
                    "change_type": "added"
                    "scope": "chat:write:user,channels:read"
                },
                {
                    "service_id": "3456789012",
                    "service_type": "Airbrake",
                    "user_id": "U3456CDEF",
                    "user_name": "Joey",
                    "channel": "C1234567890",
                    "date": "1392163202",
                    "change_type": "disabled",
                    "reason": "user",
                    "scope": "incoming-webhook"
                }
            ],
            "paging": {
                    "count": 3,
                    "total": 3,
                    "page": 1,
                    "pages": 1
            }
        }

    Logs can contain data for either a service or API application. If it's a service, service_id and service_type will be returned, and if it's an API application, app_id and app_type will be returned.
    Logs can also contain different change_types. The possible types are: added, removed, enabled, disabled, and updated.
    If the log entry is an RSS feed, the log will also contain rss_feed (with a value of true), rss_feed_change_type, rss_feed_title and rss_feed_url.
    When a disabled event is logged, its log entry will also contain a reason for why the event occurred. The list of possible reasons are:

    user - Manually disabled by user
    rate_limits - Rate limits exceeded
    slack - Disabled by Slack
    errors - Too many errors
    system - A system change (i.e. channel archived)
    admin - Admin (i.e. user deleted)
    api_decline - User declied the API TOS
    deauth - Service deauthorized

    The paging information contains the count of logs returned, the total number of logs, the page of results returned in this response and the total number of pages available.

    For more information see https://api.slack.com/methods/integrationLogs
    """
    endpoint = 'team.integrationLogs'
    required_args = {}
    optional_args = {
        'app_id',
        'change_type',
        'count',
        'page',
        'service_id',
        'user',
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
                 app_id=None,
                 change_type=None,
                 count=None,
                 page=None,
                 service_id=None,
                 user=None,
                 ):
        """Gets the integration logs for the current team.

        :param app_id: Optional. Filter logs to this Slack app. Defaults to all logs. e.g.
        :param change_type: Optional. Filter logs with this change type. Defaults to all logs. e.g. added
        :param count: Optional, default=100. Number of items to return per page. e.g. 20
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        :param service_id: Optional. Filter logs to this service. Defaults to all logs. e.g.
        :param user: Optional. Filter logs generated by this user’s actions. Defaults to all logs. e.g. U1234567890
        """
        optional_kwargs = {}
        if app_id is not None:
            optional_kwargs['app_id'] = app_id
        if change_type is not None:
            optional_kwargs['change_type'] = change_type
        if count is not None:
            optional_kwargs['count'] = count
        if page is not None:
            optional_kwargs['page'] = page
        if service_id is not None:
            optional_kwargs['service_id'] = service_id
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Profile.register('get')
class ProfileGet(BaseAPIEndpoint):
    """This method is used to get the profile field definitions for this team.

    The response contains a profile item with an array of key value pairs. Right now only the fields key is supported, and it contains a list of field definitions for this team.
    Note that returned field definitions always have an id.

    .. code-block:: json

        {
            "ok": true,
            "profile": {
                "fields": [
                    {
                        "id": "Xf06054AAA",
                        "ordering": 0,
                        "label": "Phone extension",
                        "hint": "Enter the extension to reach your desk",
                        "type": "text",
                        "possible_values": null,
                        "options": null,
                        "is_hidden": 1
                    },
                    {
                        "id": "Xf06054BBB",
                        "ordering": 1,
                        "label": "Date of birth",
                        "hint": "When you were born",
                        "type": "date",
                        "possible_values": null,
                        "options": null
                    },
                    {
                        "id": "Xf06054CCC",
                        "ordering": 2,
                        "label": "Facebook",
                        "hint": "Enter a link to your Facebook profile",
                        "type": "link",
                        "possible_values": null,
                        "options": null
                    },
                    {
                        "id": "Xf06054DDD",
                        "ordering": 3,
                        "label": "House",
                        "hint": "Hogwarts, obviously",
                        "type": "options_list",
                        "possible_values": [
                            "Gryffindor",
                            "Hufflepuff",
                            "Ravenclaw",
                            "Slytherin",
                        ],
                        "options": null
                    },
                    {
                        "id": "Xf06054EEE",
                        "ordering": 4,
                        "label": "Location",
                        "hint": "Office location (LDAP)",
                        "type": "text",
                        "possible_values": null,
                        "options": {
                            "is_protected": 1
                        }
                    },
                    {
                       "id": "Xf06054FFF",
                        "ordering": 5,
                        "label": "Manager",
                        "hint": "The boss",
                        "type": "user",
                        "possible_values": null,
                        "options": null
                    }
                ]
            }
        }


    For more information see https://api.slack.com/methods/get
    """
    endpoint = 'team.profile.get'
    required_args = {}
    optional_args = {
        'visibility',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users.profile:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 visibility=None,
                 ):
        """Retrieve a team's profile.

        :param visibility: Optional. Filter by visibility. e.g. all
        """
        optional_kwargs = {}
        if visibility is not None:
            optional_kwargs['visibility'] = visibility

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
