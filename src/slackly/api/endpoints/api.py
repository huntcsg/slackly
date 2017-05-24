from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Api(BaseAPIDispatch):
    pass


@Api.register('test')
class ApiTest(BaseAPIEndpoint):
    """This method helps you test your calling code.

    The response includes any supplied arguments:

    .. code-block:: json

        {
            "ok": true,
            "args": {
                "foo": "bar"
            }
        }

    If called with an error argument an error response is returned:

    .. code-block:: json

        {
            "ok": false,
            "error": "my_error",
            "args": {
                "error": "my_error"
            }
        }


    For more information see https://api.slack.com/methods/test
    """
    endpoint = 'api.test'
    required_args = {}
    optional_args = {
        'error',
        'foo',
    }
    options = {}

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 error=None,
                 foo=None,
                 ):
        """Checks API calling code.

        :param error: Optional. Error response to return e.g. my_error
        :param foo: Optional. example property to return e.g. bar
        """
        optional_kwargs = {}
        if error is not None:
            optional_kwargs['error'] = error
        if foo is not None:
            optional_kwargs['foo'] = foo

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
