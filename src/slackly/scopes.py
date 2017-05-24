import urllib
import uuid
import warnings

OAUTH_ENDPOINT = "https://slack.com/oauth/authorize/"


def get_scopes_from_methods(methods, bot=True):
    """Given a list of method instances, gets the scopes (and warns if there is a mismatch in your bot setting)
    
    :param methods: an iterable of :class:`BaseAPIEndpoint` subclass instances
    :param bot: A :class:`bool` indicating whether or not the scopes requested may post on behalf
    of your user or the app. The default is :class:`True`.
    :return: A :class:`set` of :class:`str` objects representing slack scopes
    """
    scopes = set()
    for method in methods:
        method_scopes = method.get_scopes(bot=bot)
        if not method_scopes:
            if method.endpoint == 'api.test':
                continue
            warnings.warn('The method [ {} ] does not appear to require any scopes. '
                          'This may be correct, or it may indicate that you want '
                          'the user vs. bot aspect. See: bot=True|False'.format(method.endpoint))
        scopes.update(method_scopes)

    return scopes


def create_request_url(client_id, scopes, redirect_uri, state=None, team=None, oauth_endpoint=OAUTH_ENDPOINT):
    """Given your client_id, an iteralble of scopes, and a redirect uri, prepares a uri to GET in your
    browser. In order for this uri to work, you must be listening at the redirect_uri. Otherwise, your attempts
    will be fruitless.
    
    :param client_id: A :class:`str` client_id
    :param scopes: An iterable of :class:`str` objects representing oauth scopes
    :param redirect_uri: A :class:`str` address that is reachable on the internet and controlled by you.
    :param state: A unique identifier that you can use to endsure that the redirect you recieve was initiated by you
    :param team: Optional. A team id to limit this request to.
    :param oauth_endpoint: The slack endpoint to hit. Unless you are doing some testing against a dummy server, you
    should leave this alone.
    :return: A :class:`str` representing a properly formed url to do the oauth handshake with
    """
    if state is None:
        state = str(uuid.uuid4())

    params = {
        'client_id': client_id,
        'scope': " ".join(scopes),
        'redirect_url': redirect_uri,
        'state': state,
    }

    if team is not None:
        params['team'] = team

    encoded_params = urllib.parse.urlencode(params)
    return "{}?{}".format(oauth_endpoint, encoded_params)
