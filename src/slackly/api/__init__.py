from .endpoints import (
    api,
    auth,
    bots,
    channels,
    chat,
    dnd,
    emoji,
    files,
    groups,
    im,
    mpim,
    oauth,
    pins,
    reactions,
    reminders,
    rtm,
    search,
    stars,
    team,
    usergroups,
    users,
)


class SlackAPI(object):
    """The API object"""

    api = api.Api()
    auth = auth.Auth()
    bots = bots.Bots()
    channels = channels.Channels()
    chat = chat.Chat()
    dnd = dnd.Dnd()
    emoji = emoji.Emoji()
    files = files.Files()
    groups = groups.Groups()
    im = im.Im()
    mpim = mpim.Mpim()
    oauth = oauth.Oauth()
    pins = pins.Pins()
    reactions = reactions.Reactions()
    reminders = reminders.Reminders()
    rtm = rtm.Rtm()
    search = search.Search()
    stars = stars.Stars()
    team = team.Team()
    usergroups = usergroups.Usergroups()
    users = users.Users()

    def __init__(self, bind=None):
        """
        
        :param bind: Optional. The client to bind to this API object.
        """
        self.bind = bind

    @property
    def bound(self):
        return self.bind is not None

    def __repr__(self):
        bind = repr(self.bind)
        return "{0.__class__.__name__}(bind={1})".format(self, bind)
