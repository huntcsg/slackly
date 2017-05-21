class BaseSlackObject(object):

    def __init__(self, **attributes):
        for key, value in attributes.items():
            setattr(self, key, value)

    def update(self, **attributes):
        for key, value in attributes.items():
            setattr(key, value)
