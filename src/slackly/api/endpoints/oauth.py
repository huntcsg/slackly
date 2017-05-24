from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Oauth(BaseAPIDispatch):
    pass


@Oauth.register('access')
class OauthAccess(BaseAPIEndpoint):
    """This method allows you to exchange a temporary OAuth code for an API access token.
    This is used as part of the OAuth authentication flow.



    As discussed in RFC 6749 it is possible to supply the Client ID and Client
    Secret using the HTTP Basic authentication scheme. If HTTP Basic authentication is used you do not need to supply the
    client_id and client_secret parameters as part of the request.



    Keep your tokens secure. Do not share tokens with users or anyone else.


    .. code-block:: json

        {
            "access_token": "xoxp-23984754863-2348975623103",
            "scope": "read"
        }

    You can use the returned token to call protected API methods on behalf of the user.

    For more information see https://api.slack.com/methods/access
    """
    endpoint = 'oauth.access'
    required_args = {
        'client_id',
        'client_secret',
        'code',
    }
    optional_args = {
        'redirect_uri',
    }
    options = {}

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 client_id,
                 client_secret,
                 code,
                 redirect_uri=None,
                 ):
        """Exchanges a temporary OAuth code for an API token.

        :param client_id: Required. Issued when you created your application. e.g. 4b39e9-752c4
        :param client_secret: Required. Issued when you created your application. e.g. 33fea0113f5b1
        :param code: Required. The code param returned via the OAuth callback. e.g. ccdaa72ad
        :param redirect_uri: Optional. This must match the originally submitted URI (if one was sent). e.g. http://example.com
        """
        optional_kwargs = {}
        if redirect_uri is not None:
            optional_kwargs['redirect_uri'] = redirect_uri

        return BaseAPIEndpoint.__call__(self,
                                        client_id=client_id,
                                        client_secret=client_secret,
                                        code=code,
                                        **optional_kwargs
                                        )
