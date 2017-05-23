from ._base import HasIDMixin, SlackType


class User(HasIDMixin, SlackType):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._repr_keys.update([
            'id',
            'name',
            'deleted',
            'status'
        ])

    """A User"""
    @property
    def schema(self):
        from . import String, Bool, Profile, Integer
        return {
            'id': String,
            'color': String,
            'deleted': Bool,
            'is_admin': Bool,
            'is_bot': Bool,
            'is_owner': Bool,
            'is_primary_owner': Bool,
            'is_restricted': Bool,
            'is_ultra_restricted': Bool,
            'name': String,
            'profile': Profile,
            'real_name': String,
            'status': String,
            'team_id': String,
            'tz': String,
            'tz_label': String,
            'tz_offset': Integer,
        }
