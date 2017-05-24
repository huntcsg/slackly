from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Auth(BaseAPIDispatch):
    pass


@Auth.register('revoke')
class AuthRevoke(BaseAPIEndpoint):
    """This method revokes an access token. Use it when you no longer need a token. For example, with a Sign In With Slack app, call this to log a user out.

    The response indicates whether the token was actually revoked:

    .. code-block:: json

        {
            "ok": true,
            "revoked": true
        }


    For more information see https://api.slack.com/methods/revoke
    """
    endpoint = 'auth.revoke'
    required_args = {}
    optional_args = {
        'test',
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
                 test=None,
                 ):
        """Revokes a token.

        :param test: Optional. Setting this parameter to 1 triggers a testing mode where the specified token will not actually be revoked. e.g. true
        """
        optional_kwargs = {}
        if test is not None:
            optional_kwargs['test'] = test

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Auth.register('test')
class AuthTest(BaseAPIEndpoint):
    """This method checks authentication and tells you who you are.


    .. code-block:: json

        {
            "ok": true,
            "url": "https:\/\/myteam.slack.com\/",
            "team": "My Team",
            "user": "cal",
            "team_id": "T12345",
            "user_id": "U12345"
        }

    When working against a team within an Enterprise Grid, you'll also find their enterprise_id here.

    For more information see https://api.slack.com/methods/test
    """
    endpoint = 'auth.test'
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
        """Checks authentication & identity.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
