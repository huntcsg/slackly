from slackly.client.response_factory import SlackAPIObjectResponse
from slackly.schema import types

# Users
User = SlackAPIObjectResponse.register('users.info', key='user')(types.User)
Users = SlackAPIObjectResponse.register('users.list', key='members')(types.List(types.User))

# Channels
Channel = SlackAPIObjectResponse.register('channels.info', key='channel')(types.Channel)
Channels = SlackAPIObjectResponse.register('channels.list', key='channels')(types.List(types.Channel))
CreatedChannel = SlackAPIObjectResponse.register('channels.create')(types.CreatedChannel)


# Chat
PostedMessage = SlackAPIObjectResponse.register('chat.postMessage')(types.PostedMessage)
PostedMeMessage = SlackAPIObjectResponse.register('chat.meMessage')(types.PostedMeMessage)
UpdatedMessage = SlackAPIObjectResponse.register('chat.update')(types.UpdatedMessage)
