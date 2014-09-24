import sys
import re
from config import Config

class Dart:
    def __init__(self, string):
        self.score = re.findall(r'\d+', string)

class Turn(dict):
    # inherit list or dict or what?
    def __init__(self, params=[]):
        #FIXME: should get darts
        pass

class Game:
    def __init__(self, params=[]):
        self.params = params[:]
        self.confObj = Config(self.params)
        self.listOfTurns = []
        self.score = self.confObj.score
        self.inPlay = False

    def startGame(self):
        self.inPlay = True
        while self.inPlay: 
            self.logTurn()
    
    def logTurn(self):
        t = Turn()
        for i in range(self.confObj.dartsPerTurn):
            t[i] = input('dart %d, enter code: '%(i+1))
        # strip score from metadata here, handle each.
        # make sure self.inPlay is unset when checkou
#        for i in (re.findall(r'\d+', foo)):
#                print(i)
# FIXME: this shall do, replace foo
        
    #    self.listOfTurns.append(newTurn)

if __name__ == "__main__":
    print("configuring game: ")
    g = Game(["just a random parameter"])
    #print("starting game...")
    #g.startGame()

    
