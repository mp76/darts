import sys,configparser

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Config(Borg):
        """ implemented as Borg """
        def __init__(self, args=[]):
            Borg.__init__(self)
            cparser = configparser.ConfigParser()
            cparser.read('darts.conf')
            self.score = int(cparser['GAME']['score'])
            self.dartsPerTurn = int(cparser['GAME']['dartsPerTurn'])
            self.tags = dict(cparser['TAGS'])
            #self.d = dict.fromkeys(range(180), 0)
        def mapFu():
            pass


