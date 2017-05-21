import os
from slackly import SlackClient, SlackAPI, SlackEventParsed
from slackly.client.response_factory import SlackAPIObjectResponse
import slackly.schema.endpoints

client = SlackClient(
    token=os.environ['SLACK_TOKEN'],
    response_factory=SlackAPIObjectResponse,
)

slack = SlackAPI(bind=client)
