import sys
import re
from config import Config

class Dart:
    def __init__(self, string):
        self.score = re.findall(r'\d+', string)

class Turn(dict):
    # inherit list or dict or what?
    def __init__(self, params):
        pass

class Game:
    def __init__(self, params=[]):
        self.params = params[:]
        self.confObj = Config(self.params)
        self.listOfTurns = []
        self.checkout = False
        self.score = (int)(self.confObj.score)

    def startGame(self):
        while self.checkout == False:
            self.logTurn(input("tell me: "))
    
    def logTurn(self, newTurn):
        """ expects a Turn object (dict) """
        #strip score from metadata here, handle each.
#        for i in (re.findall(r'\d+', foo)):
#                print(i)
# FIXME: this shall do, replace foo
        
        self.listOfTurns.append(newTurn)

if __name__ == "__main__":
    print("configuring game: ")
    g = Game(["just a random parameter"])
    print("starting game...")
    g.startGame()

    
