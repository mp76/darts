import sys
import re
from datetime import datetime
from config import Config


class Dart:
    """ the class Dart has:
    score (int), optional
    tags (list), optional """
    def __init__(self, string):
        # strip score from metadata here, handle each in seperate f.
        self.score = re.search(r'\d+', string)
        self.timestamp = datetime.now().timestamp()
        self.tags = re.findall(r'\D', string)
        
        
        
class Turn(list):
    def __init__(self):
        for i in range(self.confObj.dartsPerTurn):
            self.append(input('dart %d, enter code: '%(i+1)))
            print('you entered: %s, i appended it to actual turn.'%(t[i]))
        pass



class Session:
    def __init__(self, params=[]):
        self.params = params[:]
        self.confObj = Config(self.params)
        self.timestamp = datetime.now().timestamp()
        self.listOfTurns = []

    def logTurn(self):
        t = Turn()
        self.listOfTurns.append(t)
        print('appended turn to listOfTurns')
        
    def saveSession(self):
        #flatList = [ 
        for t in self.listOfTurns:
            print(t)
            for d in t:
                print (d)
        pass
         #TODO: save the listOfTurns in csv
        

    def startSession(self):
        print('starting session, your tags read:')
        print(self.confObj.tags)
        print('\"q return\" will end your session.')
        while True:
            self.logTurn()
            #TODO: idea: catch Exception EOFError in logTurn() or here and 
            # save session in handler

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
    

if __name__ == "__main__":
    print("configuring session: ")
    s = Session()
    #g = Game(["just a random parameter"])
    #print("starting game...")
    #g.startGame()

    
