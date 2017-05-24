import argparse
import code
import slackly
import sys


try:
    parser = argparse.ArgumentParser(prog="slackly.start_here", description="")
    parser.add_argument("token", type=str, help="A Slack API Token. Not a Client Secret.")
    options = parser.parse_args()

    client = slackly.SlackClient(token=options.token, response_factory=slackly.SlackAPIObjectResponse)
    code.interact(banner="", local=locals())

except SystemExit:
    print("Use Ctrl-D to exit")
