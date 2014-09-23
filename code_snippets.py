# reading with configparser
import configparser
cp = configparser.ConfigParser()
cp.read('file')
cp.sections()
cp['SPECIAL']['tags']
# gives true if present

# catching command line args
import sys
for a in sys.argv:
	print (a)

# Borg Pattern:
class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

foo.__dict__
#the STATE of foo

dir(foo)
#bzw foo.__dir__()  

id(foo)
#addres

type(foo)
# yo man
