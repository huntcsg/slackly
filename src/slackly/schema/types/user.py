from ._base import HasIDMixin, SlackType


class User(HasIDMixin, SlackType):
    """A User"""
    @property
    def schema(self):
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

    def __repr__(self):
        return "User(id='{0.id}', name='{0.name}')".format(self)
