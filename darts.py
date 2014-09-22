import sys
from config import *

class Turn:
    def __init__(self, params):
        pass

class Game:
    def __init__(self, params):
        self.params = params[:]
        self.confObj = Config(self.params)
        self.listOfTurns = []
        self.score = self.confObj.score

    def startGame(self):
        #now decrement self.score
        pass

if __name__ == "__main__":
    print("configuring game: ")
    g = Game(["just a random parameter"])
    print("starting game...")
    g.startGame()

    
