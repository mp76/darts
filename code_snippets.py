# reading with configparser
import configparser
cp = configparser.Configparser()
cp.read('file')
cp.sections()

# catching command line args
import sys
for a in sys.argv:
	print (a)

# Borg Pattern:
class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
