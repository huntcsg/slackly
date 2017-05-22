Examples
========

Creating a Client
-----------------

    .. code-block:: python

        from slackly import SlackClient
        import os

        client = SlackClient(token=os.environ['SLACK_TOKEN'])

        client.api_call('api.test')

Creating the API object
-----------------------

    .. code-block:: python

        from slackly import SlackClient, SlackAPI
        import os
        client = SlackClient(token=os.environ['SLACK_TOKEN'])
        slack = SlackAPI()
        slack.bind = client

        slack.api.test()
    
Creating the API object and calling against a specific Client
-------------------------------------------------------------

    .. code-block:: python

        from slackly import SlackClient, SlackAPI
        import os
        client = SlackClient(token=os.environ['SLACK_TOKEN'])
        slack = SlackAPI()

        call = slack.api.test()
        call(client)

Printing Events off of the Real Time Messaging API
--------------------------------------------------

    .. code-block:: python

        import os
        from slackly import SlackRTMClient

        rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
        for event in rtm_client.get_events_forever():
            print(event)
        
More Better event types
-----------------------

    .. code-block:: python

        import os
        from slackly import SlackRTMClient, SlackEventParsed
        rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
        rtm_client.event_factory = SlackEventParsed

        # e.g., if this is a Message
        event = rtm_client.get_event()
        print(event['channel'])  # slackly.types.Channel
        print(event['User'])  # slackly.types.Users
    