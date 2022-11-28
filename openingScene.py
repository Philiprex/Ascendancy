from battle import Battle
from sheep import Sheep
import narratives


class OpeningScene():

    def __init__(self, p1):
        narratives.disclaimer()
        print()
        narratives.open()
        sacrificialLamb = Sheep(p1)
        initBattle = Battle(p1, sacrificialLamb)
        del sacrificialLamb
        del initBattle
        p1.statsUpdate()
