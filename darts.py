import sys
import re
from config import Config

class Dart:
    """ the class Dart has:
    score (int), optional
    tags (list), optional """
    def __init__(self, string):
        # strip score from metadata here, handle each in seperate f.
        # make sure self.inPlay is unset when in checkout mode

        for i in (re.findall(r'\D+', t[i])):
            pass
            #FIXME
            #score i in some map
            #in some map, yeah... hmmm
         #   print(i)
        self.score -= re.search(r'\d+', t[i]
        pass

class Turn(dict):
    # inherit list or dict or what?
    # should consist of Darts, anyway
    def __init__(self, params=[]):
        #TODO
        pass

class Session:
    def __init__(self, params=[]):
        self.params = params[:]
        self.confObj = Config(self.params)
        self.confObj.timestamp = datetime.now().timestamp()
        self.listOfTurns = []

    def logTurn(self):
        t = Turn()
        for i in range(self.confObj.dartsPerTurn):
            t[i] = Dart(input('dart %d, enter code: '%(i+1)))
            print('you entered: %s, i appended it to actual turn.'%(t[i]))
        self.listOfTurns.append(t)
        print('appended turn to listOfTurns')
        
    def saveSession(self):
        for t in self.listOfTurns:
            print(t)
            for d in t:
                print (d)
        pass
         #TODO: save the listOfTurns in an appropriate format.
        

    def startSession(self):
        print('starting session, your tags read:')
        print(self.confObj.tags)
        print('\"q return\" will end your session.')
        while True:
            self.logTurn()
            #idea: catch EOF Error in logTurn() or here and 
            # save session in handler

        self.saveSession()



class Game(Session):
    def __init__(self, params=[]):
        super().__init__()
        self.inPlay = True
        self.score = self.confObj.score
    

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

    
