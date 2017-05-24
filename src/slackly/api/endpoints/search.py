from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Search(BaseAPIDispatch):
    pass


@Search.register('all')
class SearchAll(BaseAPIEndpoint):
    """This method allows users and applications to search both messages and files in a single call.

    The response returns matches broken down by their type of content, similar to the facebook/gmail auto-completed search widgets.

    .. code-block:: json

        {
            "ok": true,
            "query": "Best Pickles",
            "messages": {...},
            "files": {...}
        }

    Within each content group, data is returned in the following format:

    .. code-block:: json

        {
            "matches": [],
            "paging": {
                "count": 100,  - number of records per page
                "total": 15,   - total records matching query
                "page": 1,     - page of records returned
                "pages": 1     - total pages matching query
            }
        }

    This block gives the (estimated) total number of matches of this type, then has an array containing the specified page of the
    top matches. The format of matches depends on the match type, as described in the documentation for
    search.messages and search.files. These methods can be used to fetch
    further pages of messages or files.

    For more information see https://api.slack.com/methods/all
    """
    endpoint = 'search.all'
    required_args = {
        'query',
    }
    optional_args = {
        'count',
        'highlight',
        'page',
        'sort',
        'sort_dir',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'search:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 query,
                 count=None,
                 highlight=None,
                 page=None,
                 sort=None,
                 sort_dir=None,
                 ):
        """Searches for messages and files matching a query.

        :param query: Required. Search query. May contains booleans, etc. e.g. pickleface
        :param count: Optional, default=20. Number of items to return per page. e.g. 20
        :param highlight: Optional. Pass a value of true to enable query highlight markers (see below). e.g. true
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        :param sort: Optional, default=score. Return matches sorted by either score or timestamp. e.g. timestamp
        :param sort_dir: Optional, default=desc. Change sort direction to ascending (asc) or descending (desc). e.g. asc
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if highlight is not None:
            optional_kwargs['highlight'] = highlight
        if page is not None:
            optional_kwargs['page'] = page
        if sort is not None:
            optional_kwargs['sort'] = sort
        if sort_dir is not None:
            optional_kwargs['sort_dir'] = sort_dir

        return BaseAPIEndpoint.__call__(self,
                                        query=query,
                                        **optional_kwargs
                                        )


@Search.register('files')
class SearchFiles(BaseAPIEndpoint):
    """This method returns files matching a search query.

    The response envelope contains paging and result information:

    .. code-block:: json

        {
            "ok": true,
            "query": "test",
            "files": {
                "total": 829,
                "paging": {
                    "count": 20,
                    "total": 829,
                    "page": 1,
                    "pages": 42
                },
                "matches": [
                    {...},
                    {...},
                    {...}
                ]
            }
        }

    Matches contains a list of file objects.
    All search methods support the highlight parameter. If specified, the matching query terms will be marked
    up in the results so that clients may replace them with appropriate highlighting markers
    (e.g. <span class="highlight"></span>). The UTF-8 markers we use are:
    start: "\xEE\x80\x80"; # U+E000 (private-use)
    end  : "\xEE\x80\x81"; # U+E001 (private-use)

    Please note that the max count value is 1000 and the max page value is 100.

    For more information see https://api.slack.com/methods/files
    """
    endpoint = 'search.files'
    required_args = {
        'query',
    }
    optional_args = {
        'count',
        'highlight',
        'page',
        'sort',
        'sort_dir',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'search:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 query,
                 count=None,
                 highlight=None,
                 page=None,
                 sort=None,
                 sort_dir=None,
                 ):
        """Searches for files matching a query.

        :param query: Required. Search query. May contain booleans, etc. e.g. pickleface
        :param count: Optional, default=20. Number of items to return per page. e.g. 20
        :param highlight: Optional. Pass a value of true to enable query highlight markers (see below). e.g. true
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        :param sort: Optional, default=score. Return matches sorted by either score or timestamp. e.g. timestamp
        :param sort_dir: Optional, default=desc. Change sort direction to ascending (asc) or descending (desc). e.g. asc
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if highlight is not None:
            optional_kwargs['highlight'] = highlight
        if page is not None:
            optional_kwargs['page'] = page
        if sort is not None:
            optional_kwargs['sort'] = sort
        if sort_dir is not None:
            optional_kwargs['sort_dir'] = sort_dir

        return BaseAPIEndpoint.__call__(self,
                                        query=query,
                                        **optional_kwargs
                                        )


@Search.register('messages')
class SearchMessages(BaseAPIEndpoint):
    """This method returns messages matching a search query.

    The response envelope contains paging and result information:

    .. code-block:: json

        {
            "ok": true,
            "query": "test",
            "messages": {
                "total": 829,
                "paging": {
                    "count": 20,
                    "total": 829,
                    "page": 1,
                    "pages": 42
                },
                "matches": [
                    {...},
                    {...},
                    {...}
                ]
            }
        }

    The actual matches are returned as hashes containing contextual messages:

    .. code-block:: json

        {
            "type": "message",
            "channel": {
                "id": "C2147483753",
                "name": "foo"
            },
            "user": "U2147483709",
            "username": "johnnytest",
            "ts": "1359414002.000003",
            "text": "mention test: johnnyrodgers".
            "permalink": "https:\/\/example.slack.com\/channels\/foo\/p1359414002000003",
            "previous_2": {
                "user": "U2147483709",
                "username": "johnnytest",
                "text": "This was said before before",
                "ts": "1359413987.000000",
                "type": "message"
            },
            "previous": {
                "user": "U2147483709",
                "username": "johnnytest",
                "text": "This was said before",
                "ts": "1359414001.000000",
                "type": "message"
            },
            "next": {
                "user": "U2147483709",
                "username": "johnnytest",
                "text": "This was said after",
                "ts": "1359414020.000000",
                "type": "message"
            },
            "next_2": {
                "user": "U2147483709",
                "username": "johnnytest",
                "text": "This was said after after",
                "ts": "1359414021.000000",
                "type": "message"
            }
        }

    Messages are searched primarily inside the message text themselves, with a lower priority on the messages
    immediately before and after. If more than one search term is provided, user and channel are also matched
    at a lower priority. To specifically search within a channel, group, or DM, add in:channel_name,
    in:group_name, or in:username. To search for messages from a specific speaker, add from:username or
    from:botname.
    For IM results, the type is set to "im" and the channel.name property contains the user ID of the
    target user. For private group results, type is set to "group".
    All search methods support the highlight parameter. If specified, the matching query terms will be marked
    up in the results so that clients may replace them with appropriate highlighting markers
    (e.g. <span class="highlight"></span>). The UTF-8 markers we use are:
    start: "\xEE\x80\x80"; # U+E000 (private-use)
    end  : "\xEE\x80\x81"; # U+E001 (private-use)

    Please note that the max count value is 1000 and the max page value is 100.

    For more information see https://api.slack.com/methods/messages
    """
    endpoint = 'search.messages'
    required_args = {
        'query',
    }
    optional_args = {
        'count',
        'highlight',
        'page',
        'sort',
        'sort_dir',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'search:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 query,
                 count=None,
                 highlight=None,
                 page=None,
                 sort=None,
                 sort_dir=None,
                 ):
        """Searches for messages matching a query.

        :param query: Required. Search query. May contains booleans, etc. e.g. pickleface
        :param count: Optional, default=20. Number of items to return per page. e.g. 20
        :param highlight: Optional. Pass a value of true to enable query highlight markers (see below). e.g. true
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        :param sort: Optional, default=score. Return matches sorted by either score or timestamp. e.g. timestamp
        :param sort_dir: Optional, default=desc. Change sort direction to ascending (asc) or descending (desc). e.g. asc
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if highlight is not None:
            optional_kwargs['highlight'] = highlight
        if page is not None:
            optional_kwargs['page'] = page
        if sort is not None:
            optional_kwargs['sort'] = sort
        if sort_dir is not None:
            optional_kwargs['sort_dir'] = sort_dir

        return BaseAPIEndpoint.__call__(self,
                                        query=query,
                                        **optional_kwargs
                                        )
