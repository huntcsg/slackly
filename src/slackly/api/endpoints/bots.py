from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Bots(BaseAPIDispatch):
    pass


@Bots.register('info')
class BotsInfo(BaseAPIEndpoint):
    """This method returns information about a bot user.



    bot_id is returned from bot_message message events and in the response of methods like channels.history.



    Use this method to look up the username and icons for those bot users. Use the app_id field to identify whether a bot belongs to your Slack app.

    Returns a bot user:

    .. code-block:: json

        {
            "ok": true,
            "bot": {
                "id": "B12345678",
                "app_id": "A4H1JB4AZ",
                "deleted": false,
                "name": "My Bot",
                "icons": {
                    "image_36": "https://...",
                    "image_48": "https://...",
                    "image_72": "https://..."
                }
            }
        }


    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'bots.info'
    required_args = {}
    optional_args = {
        'bot',
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
                 bot=None,
                 ):
        """Gets information about a bot user.

        :param bot: Optional. Bot user to get info on e.g. B12345678
        """
        optional_kwargs = {}
        if bot is not None:
            optional_kwargs['bot'] = bot

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
