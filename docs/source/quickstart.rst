Quickstart
==========

1. Follow `these instructions <https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens>`_ to get a token from slack
2. Set the environment variable `SLACK_TOKEN` as the token you got in Step 1
3. Install slackly

    .. code-block:: shell

        $ pip install slackly

4. List your team's channels and users:

    .. code-block:: python

        from slackly import SlackClient
        import os
        client = SlackClient(token=os.environ['SLACK_TOKEN'])

        channels = client.api.channels.list()
        users = client.api.users.list()

        print(channels)
        print(users)
