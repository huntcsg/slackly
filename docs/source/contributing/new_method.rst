How to add a new Web Method
===========================

For code organization and a usable API, two classes make up each endpoint.

There is the :class:`BaseAPIDispatch` class and the :class:`BaseAPIEndpoint`.

For example, if you had a single slack endpoint called foo.bar, that took a required argument baz, and an optional
argument foobar. If it requires a token, then indicated it. Here's how it would be written:

    .. code-block:: python

        class Foo(BaseAPIDispatch):
            pass

        @Foo.register('bar')
        class Bar(BaseAPIEndpoint):
            required_args = {
                'baz',
            }
            optional_args = {
                 'foobar',
            }
            options = {
                'requires_token': True
            }s

            def __call__(self,baz, foobar=None):
                optional_args = {}
                if foobar is not None:
                    optional_args['foobar'] = foobar

                return BaseAPIEndpoint.__call__(self, baz=baz, **optional_args)

        class SlackAPI(object):
            foo = Foo()


Adding a new endpoint
---------------------

1. In the module named like the root of the endpoint (the 'foo.py' in the above example), create a class like so:

    .. code-block:: python

        @Foo.register('bar')
        class FooBar(BaseAPIEndpoint):
            ...


2. Although I did not go into detail above, please include the description of the endpoint from the docs as well as
at least one json code block

3. Add a new directory under tests/data/endpoints (e.g. tests/data/endpoints/foo.bar) with simple.json file with an
example json object representative of the response the endpoint produces.

Adding a new dispatch route
---------------------------

1. Add a new module in the `src/slackly/api/endpoints` directory. Within this module create a class:

    .. code-block:: python

        class Foo(BaseAPIEndpoint):
            pass

2. In the src/api/slackly/__init__.py add the new dispatch object as a class attribute

    .. code-block:: python

        class SlackAPI(object):
            foo = Foo()

3. Follow the directions above for registering endpoints.
