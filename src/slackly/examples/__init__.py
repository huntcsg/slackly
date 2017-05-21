import os
from slackly import SlackClient, SlackAPI

client = SlackClient(
    token=os.environ['SLACKLY_TOKEN'],
)

slack = SlackAPI(bind=client)

slack.api.test()
