Slackly - A Slack Toolkit
-------------------------

|gitter| |travis| |pypi| |docs|

Use Cases:

    - Use the :class:`slackly.SlackClient` to make calls to the Web API
    - Use the :class:`slackly.SlackRTMClient` to listen to the Real Time Messaging API (via a websocket connection)
    - Use the :mod:`slackly.events` and :mod:`slackly.schema.types` in this library to build higher level abstractions on the Slack API

Installing
==========

   .. code-block:: shell

      $ pip install slackly

Simple Examples
===============

Creating a Client and Making an API Call
****************************************

    .. code-block:: python

        from slackly import SlackClient
        import os

        client = SlackClient(token=os.environ['SLACK_TOKEN'])

        # Call the api.test endpoint
        client.api_call('api.test')

Creating the API object and preparing a call
********************************************

    .. code-block:: python

        from slackly import SlackAPI, SlackClient
        import os
        slack = SlackAPI()

        # Prepare an api call. Pass "api_call" a client to get actually make the call
        api_call = slack.api.test()

        client = SlackClient(token=os.environ['SLACK_TOKEN'])
        result = api_call(client)

Printing Events off of the Real Time Messaging API
**************************************************

    .. code-block:: python

        import os
        from slackly import SlackRTMClient

        rtm_client = SlackRTMClient.from_token(token=os.environ['SLACK_TOKEN'])
        for event in rtm_client.get_events_forever():
            print(event)
        
Using Event Types
*****************

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


Development
===========

   .. code-block:: shell

      $ git clone https://github.com/huntcsg/slackly.git
      $ cd slackly
      $ tox    # Runs test suites against all python versions, pypy, does style and test coverage analysis

1. All pull requests must pass the travis-ci builds
2. All pull requests should include inline (docstring) documentation, updates to built documentation if applicable,
   and test coverage. This project aspires to be a 100% test coverage library.
3. If integration or regression test coverage is needed, let the project maintainer know and we can work out
   the best way to do so.


.. |gitter| image:: https://badges.gitter.im/huntcsg/slackly.png
   :target: https://gitter.im/slackly/Lobby
.. |travis| image:: https://travis-ci.org/huntcsg/slackly.svg?branch=master
   :target: https://travis-ci.org/huntcsg/slackly
.. |pypi| image:: https://img.shields.io/pypi/v/slackly.svg
   :target: https://pypi.python.org/pypi/slackly
.. |docs| image:: https://readthedocs.org/projects/slackly/badge/?version=latest
   :target: http://slackly.readthedocs.io/en/latest/?badge=latest
