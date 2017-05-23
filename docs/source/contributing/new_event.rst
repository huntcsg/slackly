New Event
=========

1. Add a new module in the src/slackly/events/ directory. Follow the below template:

    .. code-block:: python

        @register_event('accounts_changed')
        class AccountsChanged(BaseEvent):
            """
                .. code-block:: json
                    :caption: Example json response

                    {
                        "type": "accounts_changed"
                    }


            For more information see https://api.slack.com/events/accounts_changed
            """
            @property
            def schema(self):
                return {
                    'type': types.String,
                }

2. Be sure of the following details:

    a) The event should be "registered" under the string found in event['type'] key
    b) The class subclasses from :class:`slackly.events.BaseEvent`
    c) The class includes a rst json code-block with an example event json blob
    d) Although it is not 100% necessary, please include a `schema` property as shown

3. Add an import in src/slackly/events/__init__.py

    .. code-block:: python

        from .accounts_changed import AccountsChanged

4. Add an example json file in tests/data/events/[YOUR EVENT]/example.json, where [YOUR EVENT] is the string you registered
5. Run the test suite
