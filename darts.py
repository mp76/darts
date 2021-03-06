import sys, re, csv
from datetime import datetime
from config import Config

class Dart:
    """ the class Dart has:
    score (int), optional
    tags (list), optional """
    def __init__(self, string):
        # strip score from metadata 
        self.score = re.search(r'\d+', string)
        self.tags = re.findall(r'\D', string)
        
class Turn(list):
    #FIXME: this thing needs a timestamp
    #FIXME: user interaction shouldn't really go here
    """ a List of Darts """
    def __init__(self):
        for i in range(Config().dartsPerTurn):
            self.append(input('dart %d, enter code: '%(i+1)))
            #FIXME  
            if i==2:
                print('\n')

class Session:
    #TODO: Sessions should be taggable too    
    def __init__(self, params=[]):
        self.params = params[:]
        self.confObj = Config(self.params)
        self.timestamp = datetime.now().timestamp()
        self.listOfTurns = []
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.listOfTurns = []
    
    def logTurn(self):
        t = Turn()
        self.listOfTurns.append(t)

    def openSession(self):
        with open('darts.csv','r', newline='') as csvfile:
            r = csv.reader(csvfile)
            for row in r:
                #TODO: what exactly is it we want to import here
                self.listOfTurns.append(row)

    def saveSession(self):
        #flatList = [ 
        with open('darts.csv', 'a', newline='') as csvfile:
            csvfile.write(str(self.timestamp) + '\n')
            wri=csv.writer(csvfile)
            for t in self.listOfTurns:
                wri.writerow(t)
        #TODO add new tags to configparser file here

    def startSession(self):
        print('starting session, your definded tags read:')
        print(self.confObj.tags)
        print('\"Ctrl-D\" will end your session.')
        try:
            while True:
                self.logTurn()
        except (EOFError):
            print('\n.\n.\nEOF caught, closing session\.\.\.')
            self.saveSession()

class Game(Session):
    def __init__(self, params=[]):
        super().__init__()
        self.inPlay = True
        self.score = self.confObj.score
        # make sure self.inPlay is unset when checking out
    def startGame(self):
        self.inPlay = True
        while self.inPlay: 
            self.logTurn()
    

#if __name__ == "__main__":
 #   print("configuring session: ")
 #   with Session() as s:
 #       s.startSession()
