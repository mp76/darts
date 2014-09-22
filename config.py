import sys
class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Config(Borg):
        """ implemented as Borg """
        def __init__(self, args):
            Borg.__init__(self)
            self.d=dict.fromkeys(range(180), 0)
        def mapFu():
            pass


