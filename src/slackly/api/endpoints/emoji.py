from ._base import BaseAPIDispatch, BaseAPIEndpoint


class Emoji(BaseAPIDispatch):
    pass


@Emoji.register('list')
class List(BaseAPIEndpoint):
    """This method lists the custom emoji for a team.
    
    {
        "ok": true,
        "emoji": {
            "bowtie": "https:\/\/my.slack.com\/emoji\/bowtie\/46ec6f2bb0.png",
            "squirrel": "https:\/\/my.slack.com\/emoji\/squirrel\/f35f40c0e0.png",
            "shipit": "alias:squirrel",
            …
        }
    }
    
    The emoji property contains a map of name/url pairs, one for each custom
    emoji used by the team. The alias: pseudo-protocol will be used where the
    emoji is an alias, the string following the colon is the name of the other
    emoji this emoji is an alias to.
    
    """
    endpoint = 'emoji.list'
    required_args = {}
    optional_args = {}
    options = {
        'include_token': True
    }

    def __call__(self,
                 ):
        """Lists custom emoji for a team.
        
        """
        optional_kwargs = {}

        return BaseAPIEndpoint.__call__(self,
                                        **optional_kwargs,
                                        )
