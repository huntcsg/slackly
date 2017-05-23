from copy import deepcopy
import json


class SlackType(object):
    """The base SlackType. It handles the default creation of attributes from keyword arguments"""
    def __init__(self, kwargs):
        """
        
        :param kwargs: An arbitrary dictionary of keyword arguments
        :return: None
        """
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
        """Returns a deepcopy of the object as a dictionary
        
        :return: A :class:`dict`
        """
        return deepcopy(self._dict)

    @property
    def as_json(self):
        """Returns a utf-8 string of the json dump of the dictionary
        
        :return: A :class:`str`
        """
        return json.dumps(self._dict)

    def __repr__(self):
        return "{0.__class__.__name__}()".format(self)


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
        return cls(dict(id=id))

    def __repr__(self):
        return "{0.__class__.__name__}(id='{0.id}')".format(self)
