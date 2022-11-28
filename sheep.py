import random


class Sheep():

    def __init__(self, p1):
        self.p1 = p1
        self.type = "sheep"
        self.health = 30

    def fight(self):
        aim = random.randrange(3)
        if aim == 1:
            print("You were rammed by the disturbed sheep and " +
                  "incurred 4 damage!")
            self.p1.stats["health"] -= 4
        else:
            print("The sheep attempted to ram you, but missed.")

    def attack(self):
        print(f"\nYou attacked the sheep doing {self.p1.hitPoints} damage.")
        self.health -= self.p1.hitPoints

    def fireball(self):
        print("You cast a fireball at the demon doing 20 damage! Harsh.")
        self.health -= 20

    def death(self):
        if self.p1.equipped == "sword":
            self.p1.stats["sanctity"] -= 5
            self.p1.stats["goodness"] -= 5
            self.p1.stats["trading"] += 5
            newWool = random.randrange(1, 6)
            self.p1.items["wool"] += newWool
            self.p1.items["meat"] += 2
            print(f"\nYou've killed the sheep and gained {newWool} wool " +
                  "and 2 meat. You hope it was worth it.")

        elif self.p1.equipped == "Slayer":
            self.p1.stats["sanctity"] -= 5
            self.p1.stats["goodness"] -= 5
            self.p1.stats["trading"] += 5
            newWool = random.randrange(1, 21)
            self.p1.items["wool"] += newWool
            newMeat = random.randrange(5, 11)
            self.p1.items["meat"] += newMeat
            print("\nYou destroyed the sheep. An unsanctimonious death, " +
                  f"but at least you got {newWool} wool and " +
                  f"{newMeat} meat.")

        elif self.p1.equipped == "stick":
            self.p1.stats["sanctity"] += 5
            self.p1.stats["goodness"] += 5
            self.p1.stats["trading"] -= 5
            newWool = random.randrange(1, 6)
            self.p1.items["wool"] += newWool
            print(f"\nYou've knocked the sheep out, giving you the time to " +
                  f"harvest {newWool} wool. Not much, but at " +
                  "the sheep got to live.")

        elif self.p1.equipped == "Shear":
            self.p1.stats["sanctity"] += 5
            self.p1.stats["goodness"] += 10
            self.p1.stats["trading"] -= 5
            newWool = random.randrange(10, 21)
            self.p1.items["wool"] += newWool
            print("\nYou pacified the sheep and were able to shear " +
                  f"{newWool} wool.")
