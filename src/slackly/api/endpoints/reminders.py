from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Reminders(BaseAPIDispatch):
    pass


@Reminders.register('add')
class RemindersAdd(BaseAPIEndpoint):
    """This method creates a reminder.

    (Note: only non-recurring reminders will have time and complete_ts field.)

    .. code-block:: json

        {
            "ok": true,
            "reminder": {
                "id": "Rm12345678",
                "creator": "U18888888",
                "user": "U18888888",
                "text": "eat a banana",
                "recurring": false,
                "time": 1602288000,
                "complete_ts": 0
            }
        }


    For more information see https://api.slack.com/methods/add
    """
    endpoint = 'reminders.add'
    required_args = {
        'text',
        'time',
    }
    optional_args = {
        'user',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reminders:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 text,
                 time,
                 user=None,
                 ):
        """Creates a reminder.

        :param text: Required. The content of the reminder e.g. eat a banana
        :param time: Required. When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes," or "every Thursday") e.g. 1602288000
        :param user: Optional. The user who will receive the reminder. If no user is specified, the reminder will go to user who created it. e.g. U18888888
        """
        optional_kwargs = {}
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        text=text,
                                        time=time,
                                        **optional_kwargs
                                        )


@Reminders.register('complete')
class RemindersComplete(BaseAPIEndpoint):
    """This method completes a reminder.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/complete
    """
    endpoint = 'reminders.complete'
    required_args = {
        'reminder',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reminders:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 reminder,
                 ):
        """Marks a reminder as complete.

        :param reminder: Required. The ID of the reminder to be marked as complete e.g. Rm12345678
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        reminder=reminder,
                                        **optional_kwargs
                                        )


@Reminders.register('delete')
class RemindersDelete(BaseAPIEndpoint):
    """This method deletes a reminder.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/delete
    """
    endpoint = 'reminders.delete'
    required_args = {
        'reminder',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reminders:write',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 reminder,
                 ):
        """Deletes a reminder.

        :param reminder: Required. The ID of the reminder e.g. Rm12345678
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        reminder=reminder,
                                        **optional_kwargs
                                        )


@Reminders.register('info')
class RemindersInfo(BaseAPIEndpoint):
    """This method returns information about a reminder.

    (Note: only non-recurring reminders will have time and complete_ts field.)

    .. code-block:: json

        {
            "ok": true,
            "reminder": {
                "id": "Rm12345678",
                "creator": "U18888888",
                "user": "U18888888",
                "text": "eat a banana",
                "recurring": false,
                "time": 1458678068,
                "complete_ts": 1458678200
            }
        }


    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'reminders.info'
    required_args = {
        'reminder',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reminders:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 reminder,
                 ):
        """Gets information about a reminder.

        :param reminder: Required. The ID of the reminder e.g. Rm23456789
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        reminder=reminder,
                                        **optional_kwargs
                                        )


@Reminders.register('list')
class RemindersList(BaseAPIEndpoint):
    """This method lists all reminders created by or for a given user.

    (Note: only non-recurring reminders will have time and complete_ts field.)

    .. code-block:: json

        {
            "ok": true,
            "reminders": [
                {
                    "id": "Rm12345678",
                    "creator": "U18888888",
                    "user": "U18888888",
                    "text": "eat a banana",
                    "recurring": false,
                    "time": 1458678068,
                    "complete_ts": 0
                },
                {
                    "id": "Rm23456789",
                    "creator": "U18888888",
                    "user": "U18888888",
                    "text": "drink water",
                    "recurring": true
                }
            ]
        }


    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'reminders.list'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'reminders:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 ):
        """Lists all reminders created by or for a given user.

        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
