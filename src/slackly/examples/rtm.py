import os
from slackly import SlackRTMClient, SlackEventParsed
from slackly.events import ReconnectUrl


def main():
    rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
    rtm_client.event_factory = SlackEventParsed

    for event in rtm_client.get_events_forever():
        if isinstance(event, ReconnectUrl):
            print("I don't want to reconnect")
        else:
            print(event)


if __name__ == '__main__':
    main()
