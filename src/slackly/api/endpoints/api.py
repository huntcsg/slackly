from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Api(BaseAPIDispatch):
    pass


@Api.register('test')
class Test(BaseAPIEndpoint):
    """This method helps you test your calling code.
    
    The response includes any supplied arguments:
    {
        "ok": true,
        "args": {
            "foo": "bar"
        }
    }
    
    If called with an error argument an error response is returned:
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
        'error'
        'foo'
    }
    options = {}

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
                                        **optional_kwargs,
                                        )
