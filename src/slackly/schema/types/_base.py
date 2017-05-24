import copy
import json


class SlackType(object):
    """The base SlackType. It handles the default creation of attributes from keyword arguments"""
    def __init__(self, kwargs):
        """
        
        :param kwargs: An arbitrary dictionary of keyword arguments
        :return: None
        """
        self._repr_keys = set()

        if kwargs is None:
            kwargs = {}

        if isinstance(kwargs, dict):
            self._dict = copy.deepcopy(kwargs)
        else:
            self._dict = {'value': copy.deepcopy(kwargs)}
            self._repr_keys.add('value')

        if hasattr(self, 'schema'):
            for key, factory in self.schema.items():
                setattr(self, key, factory(self._dict.get(key)))
        else:
            for key, value in self._dict.items():
                setattr(self, key, value)

    @property
    def as_dict(self):
        """Returns a deepcopy of the object as a dictionary
        
        :return: A :class:`dict`
        """
        return copy.deepcopy(self._dict)

    @property
    def as_json(self):
        """Returns a utf-8 string of the json dump of the dictionary
        
        :return: A :class:`str`
        """
        return json.dumps(self._dict)

    def __repr__(self):
        detail = []
        for key in sorted(self._repr_keys):
            detail.append("{}={}".format(key, repr(self._dict.get(key, None))))
        detail = ', '.join(detail)

        return "{0.__class__.__name__}({1})".format(self, detail)


class HasIDMixin(object):
    """This mixin adds the behavior of allowing the object to be instantiated from an ID.
    Also updates the __repr__ to include the id in the repr
    """

    @classmethod
    def Id(cls, id):
        """Class method to create the class from an ID
        
        :param id: A slack ID, e.g. T1NASNDSP
        :return: A class instance of whatever class this is mixed in to
        """
        cls_instance = cls(dict(id=id))
        cls_instance._repr_keys.add('id')
        return cls_instance
