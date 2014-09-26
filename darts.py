import sys
import re
from config import Config

class Dart:
    """ the class Dart has:
    score (int), optional
    tags (list), optional """
    def __init__(self, string):
        #FIXME
        # strip score from metadata here, handle each.
        # make sure self.inPlay is unset when checkou
        #for i in (re.findall(r'\D+', t[i])):
            #score i in some map
         #   print(i)
        #self.score -= re.search(r'\d+', t[i]
        pass

class Turn(dict):
    # inherit list or dict or what?
    # should consist of Darts, anyway
    def __init__(self, params=[]):
        #FIXME
        pass

class Game:
    def __init__(self, params=[]):
        self.inPlay = False
        self.params = params[:]
        self.confObj = Config(self.params)
        self.listOfTurns = []
        self.score = self.confObj.score

    def startGame(self):
        self.inPlay = True
        while self.inPlay: 
            self.logTurn()
    
    def logTurn(self):
        t = Turn()
        for i in range(self.confObj.dartsPerTurn):
            t[i] = Dart(input('dart %d, enter code: '%(i+1)))
            print('you entered: %s, i appended it to actual turn.'%(t[i]))
        self.listOfTurns.append(t)
            print('appended turn to listOfTurns')
        
        
    #    self.listOfTurns.append(newTurn)

if __name__ == "__main__":
    print("configuring game: ")
    g = Game(["just a random parameter"])
    #print("starting game...")
    #g.startGame()

    
