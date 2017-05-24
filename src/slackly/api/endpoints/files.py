from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Files(BaseAPIDispatch):
    pass


@Files.register('comments')
class Comments(BaseAPIDispatch):
    pass


@Comments.register('add')
class CommentsAdd(BaseAPIEndpoint):
    """Add a comment to an existing file.

    If successful, the response will include a file comment object.

    .. code-block:: json

        {
            "ok": true,
            "comment": {
                "id": "Fc1234567890",
                "created": 1356032811,
                "timestamp": 1356032811,
                "user": "U1234567890",
                "comment": "Everyone should take a moment to read this file.",
                "channel": "C1234467890"
            }
        }


    For more information see https://api.slack.com/methods/add
    """
    endpoint = 'files.comments.add'
    required_args = {
        'comment',
        'file',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 comment,
                 file,
                 ):
        """Add a comment to an existing file.

        :param comment: Required. Text of the comment to add. e.g. Everyone should take a moment to read this file.
        :param file: Required. File to add a comment to. e.g. F1234467890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        comment=comment,
                                        file=file,
                                        **optional_kwargs
                                        )


@Comments.register('delete')
class CommentsDelete(BaseAPIEndpoint):
    """Delete an existing comment on a file. Only the original author of the comment or a Team Administrator may delete a file comment.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/delete
    """
    endpoint = 'files.comments.delete'
    required_args = {
        'file',
        'id',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 file,
                 id,
                 ):
        """Deletes an existing comment on a file.

        :param file: Required. File to delete a comment from. e.g. F1234567890
        :param id: Required. The comment to delete. e.g. Fc1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        file=file,
                                        id=id,
                                        **optional_kwargs
                                        )


@Comments.register('edit')
class CommentsEdit(BaseAPIEndpoint):
    """Edit an existing comment on a file. Only the user who created a comment may make edits. Teams may configure a limited time window during which file comment edits are allowed.

    If successful, the response will include a file comment object.

    .. code-block:: json

        {
            "ok": true,
            "comment": {
                "id": "Fc1234567890",
                "created": 1356032811,
                "timestamp": 1356032811,
                "user": "U1234567890",
                "comment": "Everyone should take a moment to read this file, seriously."
            }
        }


    For more information see https://api.slack.com/methods/edit
    """
    endpoint = 'files.comments.edit'
    required_args = {
        'comment',
        'file',
        'id',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 comment,
                 file,
                 id,
                 ):
        """Edit an existing file comment.

        :param comment: Required. Text of the comment to edit. e.g. Everyone should take a moment to read this file, seriously.
        :param file: Required. File containing the comment to edit. e.g. F1234567890
        :param id: Required. The comment to edit. e.g. Fc1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        comment=comment,
                                        file=file,
                                        id=id,
                                        **optional_kwargs
                                        )


@Files.register('delete')
class FilesDelete(BaseAPIEndpoint):
    """This method deletes a file from your team.


    .. code-block:: json

        {
            "ok": true
        }


    For more information see https://api.slack.com/methods/delete
    """
    endpoint = 'files.delete'
    required_args = {
        'file',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 file,
                 ):
        """Deletes a file.

        :param file: Required. ID of file to delete. e.g. F1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        file=file,
                                        **optional_kwargs
                                        )


@Files.register('info')
class FilesInfo(BaseAPIEndpoint):
    """This method returns information about a file in your team.

    The response contains a file object, and a list of comment objects followed by paging information.

    .. code-block:: json

        {
            "ok": true,
            "file": {
                "id" : "F2147483862",
                "timestamp" : 1356032811,

                "name" : "file.htm",
                "title" : "My HTML file",
                "mimetype" : "text\/plain",
                "filetype" : "text",
                "pretty_type": "Text",
                "user" : "U2147483697",

                "mode" : "hosted",
                "editable" : true,
                "is_external": false,
                "external_type": "",

                "size" : 12345,

                "url": "https:\/\/slack-files.com\/files-pub\/T024BE7LD-F024BERPE-09acb6\/1.png",
                "url_download": "https:\/\/slack-files.com\/files-pub\/T024BE7LD-F024BERPE-09acb6\/download\/1.png",
                "url_private": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/1.png",
                "url_private_download": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/download\/1.png",

                "thumb_64": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_64.png",
                "thumb_80": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_80.png",
                "thumb_360": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.png",
                "thumb_360_gif": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.gif",
                "thumb_360_w": 100,
                "thumb_360_h": 100,

                "permalink": "https:\/\/tinyspeck.slack.com\/files\/cal\/F024BERPE\/1.png",
                "edit_link": "https:\/\/tinyspeck.slack.com\/files\/cal\/F024BERPE\/1.png/edit",
                "preview": "&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;meta charset='utf-8'&gt;",
                "preview_highlight": "&lt;div class=\"sssh-code\"&gt;&lt;div class=\"sssh-line\"&gt;&lt;pre&gt;&lt;!DOCTYPE html...",
                "lines" : 123,
                "lines_more": 118,

                "is_public": true,
                "public_url_shared": false,
                "channels": ["C024BE7LT", ...],
                "groups": ["G12345", ...],
                "initial_comment": {...},
                "num_stars": 7,
                "is_starred": true
            },
            "comments": [
                {
                    "id": "Fc027BN9L9",
                    "timestamp": 1356032811,
                    "user": "U2147483697",
                    "comment": "This is a comment"
                },
                ...
            ],
            "paging": {
                "count": 100,
                "total": 2,
                "page": 1,
                "pages": 0
            }
        }

    The file object contains information about the uploaded file.
    Each comment object in the comments array contains details about a single comment. Comments are returned oldest first.
    The paging information contains the count of comments returned, the total number of
    comments, the page of results returned in this response and the total number of pages available. Please note that the max count value is 1000 and the max page value is 100.
    Bot user tokens may use this method to access information about files appearing in the channels they belong to.

    For more information see https://api.slack.com/methods/info
    """
    endpoint = 'files.info'
    required_args = {
        'file',
    }
    optional_args = {
        'count',
        'page',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'files:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 file,
                 count=None,
                 page=None,
                 ):
        """Gets information about a team file.

        :param file: Required. Specify a file by providing its ID. e.g. F2147483862
        :param count: Optional, default=100. Number of items to return per page. e.g. 20
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        """
        optional_kwargs = {}
        if count is not None:
            optional_kwargs['count'] = count
        if page is not None:
            optional_kwargs['page'] = page

        return BaseAPIEndpoint.__call__(self,
                                        file=file,
                                        **optional_kwargs
                                        )


@Files.register('list')
class FilesList(BaseAPIEndpoint):
    """This method returns a list of files within the team. It can be filtered and sliced in various ways.


    .. code-block:: json

        {
            "ok": true,
            "files": [
                {...},
                {...},
                {...},
                ...
            ],
            "paging": {
                "count": 100,
                "total": 295,
                "page": 1,
                "pages": 3
            }
        }

    The response contains a list of file objects, followed by paging information. Files are always returned with
    the most recent first.
    The paging information contains the count of files returned, the total number of
    files matching the filter (if any was supplied), the page of results returned in this response and
    the total number of pages available.

    For more information see https://api.slack.com/methods/list
    """
    endpoint = 'files.list'
    required_args = {}
    optional_args = {
        'channel',
        'count',
        'page',
        'ts_from',
        'ts_to',
        'types',
        'user',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': {
            'files:read',
        },
        'bot': set(),
        'user': set(),
    }

    def __call__(self,
                 channel=None,
                 count=None,
                 page=None,
                 ts_from=None,
                 ts_to=None,
                 types=None,
                 user=None,
                 ):
        """Lists & filters team files.

        :param channel: Optional. Filter files appearing in a specific channel, indicated by its ID. e.g. C1234567890
        :param count: Optional, default=100. Number of items to return per page. e.g. 20
        :param page: Optional, default=1. Page number of results to return. e.g. 2
        :param ts_from: Optional, default=0. Filter files created after this timestamp (inclusive). e.g. 123456789
        :param ts_to: Optional, default=now. Filter files created before this timestamp (inclusive). e.g. 123456789
        :param types: Optional, default=all. Filter files by type:


    all - All files
    spaces - Posts
    snippets - Snippets
    images - Image files
    gdocs - Google docs
    zips - Zip files
    pdfs - PDF files


    You can pass multiple values in the types argument, like types=spaces,snippets.The default value is all, which does not filter the list. e.g. images
        :param user: Optional. Filter files created by a single user. e.g. U1234567890
        """
        optional_kwargs = {}
        if channel is not None:
            optional_kwargs['channel'] = channel
        if count is not None:
            optional_kwargs['count'] = count
        if page is not None:
            optional_kwargs['page'] = page
        if ts_from is not None:
            optional_kwargs['ts_from'] = ts_from
        if ts_to is not None:
            optional_kwargs['ts_to'] = ts_to
        if types is not None:
            optional_kwargs['types'] = types
        if user is not None:
            optional_kwargs['user'] = user

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )


@Files.register('revokePublicURL')
class FilesRevokePublicURL(BaseAPIEndpoint):
    """This method disables public/external sharing for a file.

    The response contains a file object.

    For more information see https://api.slack.com/methods/revokePublicURL
    """
    endpoint = 'files.revokePublicURL'
    required_args = {
        'file',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 file,
                 ):
        """Revokes public/external sharing access for a file

        :param file: Required. File to revoke e.g. F1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        file=file,
                                        **optional_kwargs
                                        )


@Files.register('sharedPublicURL')
class FilesSharedPublicURL(BaseAPIEndpoint):
    """This method enables public/external sharing for a file.

    The response contains a file object, including the permalink_public url.

    .. code-block:: json

        {
            "ok": true,
            "file": {
                "id" : "F2147483862",
                "timestamp" : 1356032811,

                "name" : "file.htm",
                "title" : "My HTML file",
                "mimetype" : "text\/plain",
                "filetype" : "text",
                "pretty_type": "Text",
                "user" : "U2147483697",

                "mode" : "hosted",
                "editable" : true,
                "is_external": false,
                "external_type": "",

                "size" : 12345,

                "url": "https:\/\/slack-files.com\/files-pub\/T024BE7LD-F024BERPE-09acb6\/1.png",
                "url_download": "https:\/\/slack-files.com\/files-pub\/T024BE7LD-F024BERPE-09acb6\/download\/1.png",
                "url_private": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/1.png",
                "url_private_download": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/download\/1.png",

                "thumb_64": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_64.png",
                "thumb_80": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_80.png",
                "thumb_360": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.png",
                "thumb_360_gif": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.gif",
                "thumb_360_w": 100,
                "thumb_360_h": 100,

                "permalink": "https:\/\/tinyspeck.slack.com\/files\/cal\/F024BERPE\/1.png",
                "permalink_public": "https:\/\/slack-files.com\/T024BE7LD-F024BERPE-8004f909b1",
                "edit_link": "https:\/\/tinyspeck.slack.com\/files\/cal\/F024BERPE\/1.png/edit",
                "preview": "&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;meta charset='utf-8'&gt;",
                "preview_highlight": "&lt;div class=\"sssh-code\"&gt;&lt;div class=\"sssh-line\"&gt;&lt;pre&gt;&lt;!DOCTYPE html...",
                "lines" : 123,
                "lines_more": 118,

                "is_public": true,
                "public_url_shared": false,
                "channels": ["C024BE7LT", ...],
                "groups": ["G12345", ...],
                "initial_comment": {...},
                "num_stars": 7,
                "is_starred": true
            },
            "comments": [
                {
                    "id": "Fc027BN9L9",
                    "timestamp": 1356032811,
                    "user": "U2147483697",
                    "comment": "This is a comment"
                },
                ...
            ],
            "paging": {
                "count": 100,
                "total": 2,
                "page": 1,
                "pages": 0
            }
        }

    The file object contains information about the uploaded file.
    Each comment object in the comments array contains details about a single comment. Comments are returned oldest first.
    The paging information contains the count of comments returned, the total number of
    comments, the page of results returned in this response and the total number of pages available. Please note that the max count value is 1000 and the max page value is 100.

    For more information see https://api.slack.com/methods/sharedPublicURL
    """
    endpoint = 'files.sharedPublicURL'
    required_args = {
        'file',
    }
    optional_args = {}
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 file,
                 ):
        """Enables a file for public/external sharing.

        :param file: Required. File to share e.g. F1234567890
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        file=file,
                                        **optional_kwargs
                                        )


@Files.register('upload')
class FilesUpload(BaseAPIEndpoint):
    """This method allows you to create or upload an existing file.

    If successful, the response will include a file object.

    .. code-block:: json

        {
            "ok": true,
            "file": {...}
        }

    By default all newly-uploaded files are private and only visible to the owner.
    They become public once they are shared into a public channel (which can
    happen at upload time via the channels argument).

    Examples
    Upload "dramacat.gif" and share it in channel, using multipart/form-data:
    curl -F file=@dramacat.gif -F channels=C024BE91L,#general -F token=xxxx-xxxxxxxxx-xxxx https://slack.com/api/files.upload

    Create an editable file containing the text "Hello":
    curl -F content="Hello" -F token=xxxx-xxxxxxxxx-xxxx https://slack.com/api/files.upload


    For more information see https://api.slack.com/methods/upload
    """
    endpoint = 'files.upload'
    required_args = {}
    optional_args = {
        'channels',
        'content',
        'file',
        'filename',
        'filetype',
        'initial_comment',
        'title',
    }
    options = {
        'include_token': True,
    }

    # Scope Information
    scopes = {
        'all': set(),
        'bot': set(),
        'user': {
            'files:write:user',
        },
    }

    def __call__(self,
                 channels=None,
                 content=None,
                 file=None,
                 filename=None,
                 filetype=None,
                 initial_comment=None,
                 title=None,
                 ):
        """Uploads or creates a file.

        :param channels: Optional. Comma-separated list of channel names or IDs where the file will be shared. e.g. C1234567890,C2345678901,C3456789012
        :param content: Optional. File contents via a POST variable. If omitting this parameter, you must provide a file. e.g. ...
        :param file: Optional. File contents via multipart/form-data. If omitting this parameter, you must submit content. e.g. ...
        :param filename: Optional. Filename of file. e.g. foo.txt
        :param filetype: Optional. A file type identifier. e.g. php
        :param initial_comment: Optional. Initial comment to add to file. e.g. Best!
        :param title: Optional. Title of file. e.g. My File
        """
        optional_kwargs = {}
        if channels is not None:
            optional_kwargs['channels'] = channels
        if content is not None:
            optional_kwargs['content'] = content
        if file is not None:
            optional_kwargs['file'] = file
        if filename is not None:
            optional_kwargs['filename'] = filename
        if filetype is not None:
            optional_kwargs['filetype'] = filetype
        if initial_comment is not None:
            optional_kwargs['initial_comment'] = initial_comment
        if title is not None:
            optional_kwargs['title'] = title

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs
                                        )
