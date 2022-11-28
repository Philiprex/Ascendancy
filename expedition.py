import random
from battle import Battle
from sheep import Sheep
from demons import NPRDemon, SeqGuessDemon, SolutionDemon


class Expedition():

    def __init__(self, p1):
        self.p1 = p1

    def sheepBattle(self):
        sheep = Sheep(self.p1)
        return Battle(self.p1, sheep).death

    def nPrBattle(self):
        nPr = NPRDemon(self.p1)
        return Battle(self.p1, nPr).death

    def seqBattle(self):
        seq = SeqGuessDemon(self.p1)
        return Battle(self.p1, seq).death

    def solBattle(self):
        sol = SolutionDemon(self.p1)
        return Battle(self.p1, sol).death

    def artifact(self):
        self.p1.items["artifacts"] += 1
        print("\nYou discover what seems to be a carved object. You're not "
              "sure what it is, but it may be of some use. You put it in "
              "your sack and carry on.")

    # randomly generates an enemy (or an artifact), calls a battle
    def range(self):
        event = random.choice([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5])
        if event == 1:
            return self.sheepBattle()
        elif event == 2:
            return self.nPrBattle()
        elif event == 3:
            return self.seqBattle()
        elif event == 4:
            return self.solBattle()
        elif event == 5:
            self.artifact()
