from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Users(BaseAPIDispatch):
    pass


@Users.register('profile')
class Profile(BaseAPIDispatch):
    pass


@Users.register('deletePhoto')
class UsersDeletePhoto(BaseAPIEndpoint):
    """This method allows the user to delete their profile image. It will clear whatever image is currently set.



    To upload a new profile image, use the companion method users.setPhoto.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/deletePhoto
    """
    endpoint = 'users.deletePhoto'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users.profile:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Delete the user profile photo

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Users.register('getPresence')
class UsersGetPresence(BaseAPIEndpoint):
    """This method lets you find out information about a user's presence.
    Consult the presence documentation for more details.

    When requesting information for a different user, this method just returns the
    current presence (either active or away):

    .. code-block:: json

        {
            "ok": true,
            "presence": "active"
        }

    If you are requesting presence information for the authed user, this method returns
    the current presence, along with details on how it was calculated:

    .. code-block:: json

        {
            "ok": true,
            "presence": "active",
            "online": true,
            "auto_away": false,
            "manual_away": false,
            "connection_count": 1,
            "last_activity": 1419027078
        }

    presence indicates the user's overall presence, it will either be active or away.
    online will be true if they have a client currently connected to Slack. auto_away will be true if our servers haven't detected any activity from the user in the last 30 minutes. manual_away will be true if the user has manually set their presence to away.
    connection_count gives a count of total connections.
    last_activity indicates the last activity seen by our servers. If a user has no connected clients then this property will be absent.

    For more information see https://api.slack.com/methods/getPresence
    """
    endpoint = 'users.getPresence'
    required_args = {
        'user',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 user,
                 ):
        """Gets user presence information.

        :param user: Required. User to get presence info on. Defaults to the authed user. e.g. U1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        user=user,
                                        **optional_kwargs
                                        )


@Users.register('identity')
class UsersIdentity(BaseAPIEndpoint):
    """After your Slack app is awarded an identity token through Sign in with Slack, use this method to retrieve a user's identity.



    The returned fields depend on any additional authorization scopes you've requested.



    This method may only be used by tokens with the identity.basic scope, as provided in the Sign in with Slack process.

    You will receive at a minimum the following information:

    .. code-block:: json

        {
            "ok": true,
            "user": {
                "name": "Sonny Whether",
                "id": "U0G9QF9C6"
            },
            "team": {
              "id": "T0G9PQBBK"
            }
        }

    Notice that user IDs are not guaranteed to be globally unique across all Slack users. The combination of user ID and team ID, on the other hand, is guaranteed to be globally unique.
    See the Sign in with Slack docs for even more information on these responses.

    Authorization scopes
    In addition, you can request access to additional profile fields by adding the following authorization scopes to your OAuth request:
    identity.email provides the team member's email address, if available:

    .. code-block:: json

        {
            "ok": true,
            "user": {
                "name": "Sonny Whether",
                "id": "U0G9QF9C6",
                "email": "bobby@example.com"
            },
            "team": {
              "id": "T0G9PQBBK"
            }
        }

    identity.avatar yield the team member's avatar images. Available sizes may vary in the future.

    .. code-block:: json

        {
            "ok": true,
            "user": {
                "name": "Sonny Whether",
                "id": "U0G9QF9C6",
                "image_24": "https://cdn.example.com/sonny_24.jpg",
                "image_32": "https://cdn.example.com/sonny_32.jpg",
                "image_48": "https://cdn.example.com/sonny_48.jpg",
                "image_72": "https://cdn.example.com/sonny_72.jpg",
                "image_192": "https://cdn.example.com/sonny_192.jpg"
            },
            "team": {
                "id": "T0G9PQBBK"
            }
        }

    Use identity.team to retrieve the user's team name:

    .. code-block:: json

        {
            "ok": true,
            "user": {
                "name": "Sonny Whether",
                "id": "U0G9QF9C6"
            },
            "team": {
                "name": "Captain Fabian's Naval Supply",
                "id": "T0G9PQBBK"
            }
        }


    For more information see https://api.slack.com/methods/identity
    """
    endpoint = 'users.identity'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'identity.basic',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Get a user's identity.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Users.register('info')
class UsersInfo(BaseAPIEndpoint):
    """This method returns information about a team member.

    Returns a user object:

    .. code-block:: json

        {
            "ok": true,
            "user": {
                "id": "U023BECGF",
                "name": "bobby",
                "deleted": false,
                "color": "9f69e7",
                "profile": {
                    "avatar_hash": "ge3b51ca72de",
                    "current_status": ":mountain_railway: riding a train",
                    "first_name": "Bobby",
                    "last_name": "Tables",
                    "real_name": "Bobby Tables",
                    "email": "bobby@slack.com",
                    "skype": "my-skype-name",
                    "phone": "+1 (123) 456 7890",
                    "image_24": "https:\/\/...",
                    "image_32": "https:\/\/...",
                    "image_48": "https:\/\/...",
                    "image_72": "https:\/\/...",
                    "image_192": "https:\/\/..."
                },
                "is_admin": true,
                "is_owner": true,
                "updated": 1490054400,
                "has_2fa": true
            }
        }


    Profile
    The profile hash contains as much information as the user has supplied in the default profile fields: first_name, last_name, real_name, email, skype, and the image_* fields. Only the image_* fields are guaranteed to be included. Data that has not been supplied may not be present at all, may be null or may contain the empty string ("").
    A user's custom profile fields may be discovered using users.profile.get.

    Email addresses
    Apps created after January 4th, 2017 must request both the users:read and users:read.email OAuth permission scopes when using the OAuth app installation flow to enable access to the email field of user objects returned by this method.

    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'users.info'
    required_args = {
        'user',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 user,
                 ):
        """Gets information about a user.

        :param user: Required. User to get info on e.g. U1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.savecall(self,
                                        user=user,
                                        **optional_kwargs
                                        )


@Users.register('list')
class UsersList(BaseAPIEndpoint):
    """This method returns a list of all users in the team. This includes deleted/deactivated users.

    Returns a list of user objects, in no particular order:

    .. code-block:: json

        {
            "ok": true,
            "members": [
                {
                    "id": "U023BECGF",
                    "team_id": "T021F9ZE2",
                    "name": "bobby",
                    "deleted": false,
                    "color": "9f69e7",
                    "real_name": "Bobby Tables",
                    "tz": "America\/Los_Angeles",
                    "tz_label": "Pacific Daylight Time",
                    "tz_offset": -25200,
                    "profile": {
                        "avatar_hash": "ge3b51ca72de",
                        "current_status": ":mountain_railway: riding a train",
                        "first_name": "Bobby",
                        "last_name": "Tables",
                        "real_name": "Bobby Tables",
                        "email": "bobby@slack.com",
                        "skype": "my-skype-name",
                        "phone": "+1 (123) 456 7890",
                        "image_24": "https:\/\/...",
                        "image_32": "https:\/\/...",
                        "image_48": "https:\/\/...",
                        "image_72": "https:\/\/...",
                        "image_192": "https:\/\/..."
                    },
                    "is_admin": true,
                    "is_owner": true,
                    "updated": 1490054400,
                    "has_2fa": false
                },
                ...
            ]
        }


    Profile
    The profile hash contains as much information as the user has supplied
    in the default profile fields: first_name, last_name, real_name,
    email, skype, and the image_* fields. Only the image_* fields are
    guaranteed to be included. Data that has not been supplied may not be
    present at all, may be null or may contain the empty string ("").
    A user's custom profile fields may be discovered using users.profile.get.

    Email addresses
    Apps created after January 4th, 2017 must request both the users:read and users:read.email OAuth permission scopes when using the OAuth app installation flow to enable access to the email field of user objects returned by this method.

    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'users.list'
    required_args = {}
    optional_args = {
        'presence',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 presence=None,
                 ):
        """Lists all users in a Slack team.

        :param presence: Optional. Whether to include presence data in the output e.g. true
        """
        optional_kwargs = {}
        if presence is not None:
            optional_kwargs['presence'] = presence

        return BaseAPIEndpoint.savecall(self,
                                        **optional_kwargs
                                        )


@Users.register('setActive')
class UsersSetActive(BaseAPIEndpoint):
    """This method lets the slack messaging server know that the authenticated user
    is currently active. Consult the presence documentation for
    more details.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/setActive
    """
    endpoint = 'users.setActive'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Marks a user as active.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Users.register('setPhoto')
class UsersSetPhoto(BaseAPIEndpoint):
    """This method allows the user to set their profile image. The caller can pass image data via image.



    Providing a "crop box" with crop_x, crop_y, and crop_w is optional. Otherwise, the whole image will be used. If cropping instructions are not specified and the source image is not square, the image will be letterboxed, just like your favorite old laserdiscs.



    Please limit your images to a maximum size of 1024 by 1024 pixels. 512x512 pixels is the minimum.



    To remove a profile image, use the companion method users.deletePhoto.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/setPhoto
    """
    endpoint = 'users.setPhoto'
    required_args = {
        'image',
    }
    optional_args = {
        'crop_w',
        'crop_x',
        'crop_y',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users.profile:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 image,
                 crop_w=None,
                 crop_x=None,
                 crop_y=None,
                 ):
        """Set the user profile photo

        :param image: Required. File contents via multipart/form-data. e.g. ...
        :param crop_w: Optional. Width/height of crop box (always square) e.g. 100
        :param crop_x: Optional. X coordinate of top-left corner of crop box e.g. 10
        :param crop_y: Optional. Y coordinate of top-left corner of crop box e.g. 15
        """
        optional_kwargs = {}
        if crop_w is not None:
            optional_kwargs['crop_w'] = crop_w
        if crop_x is not None:
            optional_kwargs['crop_x'] = crop_x
        if crop_y is not None:
            optional_kwargs['crop_y'] = crop_y

        return BaseAPIEndpoint.__call__(self,
                                        image=image,
                                        **optional_kwargs
                                        )


@Users.register('setPresence')
class UsersSetPresence(BaseAPIEndpoint):
    """This method lets you set the calling user's manual presence.
    Consult the presence documentation for more details.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/setPresence
    """
    endpoint = 'users.setPresence'
    required_args = {
        'presence',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 presence,
                 ):
        """Manually sets user presence.

        :param presence: Required. Either auto or away e.g. away
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        presence=presence,
                                        **optional_kwargs
                                        )


@Profile.register('get')
class ProfileGet(BaseAPIEndpoint):
    """Use this method to retrieve a user's profile information.

    The response contains a profile item with an array of key:value pairs.
    We hope you find the first_name, last_name, email attributes self-explanatory.
    The user's custom-set "current status" can be found in the status_text and status_emoji attributes. See custom status for more.
    The image_ keys hold links to the different sizes we support for the user's profile image from 24x24 to 1024x1024 pixels. A link to the image in its original size is stored in image_original.
    Bot users may contain an always_active profile field, indicating whether the bot user is active in a way that overrides traditional presence rules. The presence docs tell the whole story.
    For a description of the fields key, see the users.profile.set method.

    .. code-block:: json

        {
            "ok": true,
            "profile": {
                "status_text": "riding a train",
                "status_emoji": ":mountain_railway:",
                "first_name": "John",
                "last_name": "Smith",
                "email": "john@smith.com",
                "skype": "johnsmith",
                "image_24": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_24.jpg",
                "image_32": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_32.jpg",
                "image_48": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_48.jpg",
                "image_72": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_72.jpg",
                "image_192": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_192.jpg",
                "image_512": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_512.jpg",
                "image_1024": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_1024.jpg",
                "image_original": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_original.jpg",
                "fields": {
                    "Xf06054AAA": {
                        "value": "San Francisco",
                        "alt": "Giants, yo!",
                        "label": "Favorite Baseball Team"
                    },
                    "Xf06054BBB": {
                        "value": "Barista",
                        "alt": "I make the coffee & the tea!",
                        "label": "Position"
                    }
                }
            }
        }


    For more information see https://api.slack.com/methods/get
    """
    endpoint = 'users.profile.get'
    required_args = {}
    optional_args = {
        'include_labels',
        'user',
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
                 include_labels=None,
                 user=None,
                 ):
        """Retrieves a user's profile information.

        :param include_labels: Optional, default=false. Include labels for each ID in custom profile fields e.g. true
        :param user: Optional. User to retrieve profile info for e.g. U1234567890
        """
        optional_kwargs = {}
        if include_labels is not None:
            optional_kwargs['include_labels'] = include_labels
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Profile.register('set')
class ProfileSet(BaseAPIEndpoint):
    """Use this method to set a user's profile information, including name, email, current status, and other attributes.

    After making this call, the complete user's profile will be returned in the same format as above.

    .. code-block:: json

        {
            "ok": true,
            "profile": {
                "avatar_hash": "ge3b51ca72ze",
                "status_text": "riding a train",
                "status_emoji": ":mountain_railway:",
                "first_name": "John",
                "last_name": "Smith",
                "email": "john@smith.com",
                "skype": "johnsmith",
                "image_24": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_24.jpg",
                "image_32": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_32.jpg",
                "image_48": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_48.jpg",
                "image_72": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_72.jpg",
                "image_192": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_192.jpg",
                "image_512": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_512.jpg",
                "image_1024": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_1024.jpg",
                "image_original": "https://s3.amazonaws.com/slack-files/avatars/2015-11-16/123456_original.jpg",
                "fields": {
                    "Xf06054AAA": {
                        "value": "San Francisco",
                        "alt": "Giants, yo!",
                        "label": "Favorite Baseball Team"
                    },
                    "Xf06054BBB": {
                        "value": "Barista",
                        "alt": "I make the coffee & the tea!",
                        "label": "Position"
                    }
                }
            }
        }

    This method will generate a user_change event on success, containing the complete user.

    For more information see https://api.slack.com/methods/set
    """
    endpoint = 'users.profile.set'
    required_args = {}
    optional_args = {
        'name',
        'profile',
        'user',
        'value',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'users.profile:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 name=None,
                 profile=None,
                 user=None,
                 value=None,
                 ):
        """Set the profile information for a user.

        :param name: Optional. Name of a single key to set. Usable only if profile is not passed. e.g. first_name
        :param profile: Optional. Collection of key:value pairs presented as a URL-encoded JSON hash. e.g. { first_name: "John", ... }
        :param user: Optional. ID of user to change. This argument may only be specified by team admins on paid teams. e.g. U1234567890
        :param value: Optional. Value to set a single key to. Usable only if profile is not passed. e.g. John
        """
        optional_kwargs = {}
        if name is not None:
            optional_kwargs['name'] = name
        if profile is not None:
            optional_kwargs['profile'] = profile
        if user is not None:
            optional_kwargs['user'] = user
        if value is not None:
            optional_kwargs['value'] = value

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
