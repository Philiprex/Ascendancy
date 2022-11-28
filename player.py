import narratives


class Player():

    def __init__(self):
        self.inTown = False
        self.stats = {
            "health": 70,
            "sanctity": 50,
            "holiness": "Merciful",
            "goodness": 50,
            "goodliness": "Commoner",
            "trading": 50,
            "mercantilism": "Trader",
            "money": 0
        }
        self.items = {
            "potions": 0,         # costs
            "food": 0,            # costs
            "wool": 0,            # sells for
            "meat": 0,            # sells for
            "artifacts": 0,       # sells for
            "fireballs": 0,       # costs
            "demon scales": 0,    # sells for
            "souls": 0,
            "berserk": 0          # costs
        }
        self.equipment = {
            "sword": True,      # damage: 7
            "stick": True,      # damage: 5
            "Shear": False,     # damage: 9
            "Slayer": False,    # damage: 12
            "Redeemer": True,  # damage: 9
            "armor": False,
            "armor rating": 0,  # decided by type purchased
            "armor health": 0   # decided by how many times hit
        }
        self.equipped = "sword"
        self.hitPoints = 7
        self.berserkStatus = False

    def statsUpdate(self):
        if self.stats["sanctity"] < 33:
            self.stats["holiness"] = "Infidel"
            self.equipment["Redeemer"] = False
        elif 33 <= self.stats["sanctity"] < 66:
            self.stats["holiness"] = "Merciful"
            self.equipment["Redeemer"] = False
        elif 66 <= self.stats["sanctity"]:
            self.stats["holiness"] = "Holy"
        if self.stats["goodness"] < 33:
            self.stats["goodliness"] = "Trouble Maker"
            self.equipment["Shear"] = False
        elif 30 <= self.stats["goodness"] < 66:
            self.stats["goodliness"] = "Commoner"
            self.equipment["Shear"] = False
        elif 66 <= self.stats["goodness"]:
            self.stats["goodliness"] = "Hero"
        if self.stats["trading"] < 33:
            self.stats["mercantilism"] = "Leech"
            self.equipment["Slayer"] = False
        elif 33 <= self.stats["trading"] < 66:
            self.stats["mercantilism"] = "Trader"
            self.equipment["Slayer"] = False
        elif 66 <= self.stats["trading"]:
            self.stats["mercantilism"] = "Hunter"

    # checks a few qualities, calls the appropriate narrative
    def death(self):
        if self.stats["holiness"] == "Holy":
            narratives.playerDeaths("Holy")
            self.stats["health"] = 20
            return False

        elif self.stats["holiness"] == "Infidel":
            narratives.playerDeaths("Infidel")
            return False

        elif self.stats["goodliness"] == "Hero":
            narratives.playerDeaths("Hero")
            self.stats["health"] = 20
            return False

        else:
            narratives.playerDeaths(None)
            return True
