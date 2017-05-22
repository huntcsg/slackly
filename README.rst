Slackly - A Slack Toolkit
-------------------------

|gitter| |travis| |pypi| |docs| |coveralls|

Use Cases:

    - Use the :class:`slackly.SlackClient` to make calls to the Web API
    - Use the :class:`slackly.SlackRTMClient` to listen to the Real Time Messaging API (via a websocket connection)
    - Use the :mod:`slackly.events` and :mod:`slackly.schema.types` in this library to build higher level abstractions on the Slack API

Simple Examples
---------------

Creating a Client and Making an API Call
========================================

    .. code-block:: python

        from slackly import SlackClient
        import os

        client = SlackClient(token=os.environ['SLACK_TOKEN'])

        # Call the api.test endpoint
        client.api_call('api.test')

Creating the API object and preparing a call
============================================

    .. code-block:: python

        from slackly import SlackAPI, SlackClient
        import os
        slack = SlackAPI()

        # Prepare an api call. Pass "api_call" a client to get actually make the call
        api_call = slack.api.test()

        client = SlackClient(token=os.environ['SLACK_TOKEN'])
        result = api_call(client)

Printing Events off of the Real Time Messaging API
==================================================

    .. code-block:: python

        import os
        from slackly import SlackRTMClient

        rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
        for event in rtm_client.get_events_forever():
            print(event)
        
Using Event Types
=================

    .. code-block:: python

        import os
        from slackly import SlackRTMClient, SlackEventParsed
        from slackly.events import Message, UserTyping
        rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
        rtm_client.event_factory = SlackEventParsed  # Tell the RTM client to make events using this class

        for event in rtm_client.get_events_forever():
            if isinstance(event, Message):
                print("We're dealing with a message")

            elif isinstance(event, UserTyping):
                print("Someone's typing")

            else:
                print("I don't care about this event")

.. |gitter| image:: https://badges.gitter.im/huntcsg/slackly.png
.. |travis| image:: https://travis-ci.org/huntcsg/slackly.svg?branch=master
.. |pypi| image:: https://img.shields.io/pypi/v/slackly.svg
   :target: https://img.shields.io/pypi/v/slackly.svg
.. |docs| image:: https://readthedocs.org/projects/slackly/badge/?version=latest
   :target: http://slackly.readthedocs.io/en/latest/?badge=latest
.. |coveralls| image:: https://coveralls.io/repos/github/huntcsg/slackly/badge.svg?branch=master
   :target: https://coveralls.io/github/huntcsg/slackly?branch=master
