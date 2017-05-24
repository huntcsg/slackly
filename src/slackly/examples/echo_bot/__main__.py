import os
from slackly import SlackRTMClient, SlackEventParsed, SlackAPI
from slackly.events import Message


def main():
    rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
    rtm_client.event_factory = SlackEventParsed
    slack = SlackAPI()
    slack.bind = rtm_client.client

    for event in rtm_client.get_events_forever():
        if isinstance(event, Message):
            if event.get('subtype', '') == 'bot_message':
                print("I won't reply to my own message")
                continue
            print("I'm gonna echo this!")
            channel_id = event['channel'].id
            text = event['text']

            slack.chat.postMessage(channel=channel_id, text=text)


if __name__ == '__main__':
    main()
