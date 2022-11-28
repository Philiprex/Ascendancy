import narratives


class TownSquare():

    def __init__(self, p1):
        self.p1 = p1
        self.returning = 0

    # calls options, feeds response into execute
    def visitSquare(self):
        if not self.returning:
            self.firstVisit()
            self.returning = 1
        print("\n'Welcome back to the Town, Traveller.'")
        self.squareOptions()
        choice = input().upper()
        self.execute(choice)

    # prints square options depending on money and status
    def squareOptions(self):
        print("F) Ask for Food")
        if self.p1.items["demon scales"]:
            print("S) Hand over Demon Scales")
        if self.p1.stats["goodliness"] == "Hero" and \
                not self.p1.equipment["Shear"]:
            print("E) Become Elevated")
        print("L) Leave the Town Square")

    # executes player choice. also a hodgepodge of square-specific mechanics
    def execute(self, choice):
        if choice == "F" and self.p1.stats["goodliness"] == "Hero":
            narratives.goodSquare()
            self.p1.items["food"] += 2
            print("\nYou have received 2 Food")
        elif choice == "F" and self.p1.stats["goodliness"] == "Commoner":
            narratives.goodSquare()
            self.p1.items["food"] += 1
            print("\nYou have received 1 Food")
        elif choice == "F":
            narratives.badSquare()
        elif choice == "S":
            print("\nYou throw a Demon Scale to the crowd. There are gasps "
                  "and murmurs. There is clearly some relief.")
            self.p1.stats["goodness"] += 10
            print("\nYou have gained 10 Goodness")
        elif choice == "E":
            narratives.elevate()
            self.p1.equipment["Redeemer"] = False
            self.p1.equipment["Shear"] = True
            self.p1.equipment["Slayer"] = False
            print("\nYou have been gifted the Shear. It will provide "
                  "plentiful Wool, but you will not be able to kill sheep "
                  "with it, nor will you be able to attack Demons. Beware, "
                  "if you lose your 'Hero' status or accept a different "
                  "Special Weapon it will no longer be available.")
        elif choice == "L":
            pass

    #  only run the first time user goes to temple
    def firstVisit(self):
        narratives.firstSquare()
        if self.p1.stats["goodness"] < 50:
            narratives.badSquare()
        else:
            narratives.goodSquare()
            self.p1.stats["health"] += 20
