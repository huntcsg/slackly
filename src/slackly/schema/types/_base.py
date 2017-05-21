from copy import deepcopy
import json


class SlackType(object):
    def __init__(self, kwargs):
        if kwargs is None:
            kwargs = {}

        self._dict = deepcopy(kwargs)

        if hasattr(self, 'schema'):
            for key, factory in self.schema.items():
                setattr(self, key, factory(self._dict.get(key)))
        else:
            for key, value in self._dict.items():
                setattr(self, key, value)

    @property
    def as_dict(self):
        return deepcopy(self._dict)

    @property
    def as_json(self):
        return json.dumps(self._dict)

    def __repr__(self):
        return "{0.__class__.__name__}()".format(self)


class HasIDMixin(object):

    @classmethod
    def Id(cls, id):
        return cls(dict(id=id))

    def __repr__(self):
        return "{0.__class__.__name__}(id='{0.id}')".format(self)
