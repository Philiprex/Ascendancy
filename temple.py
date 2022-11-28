import narratives


class Temple():

    def __init__(self, p1):
        self.p1 = p1
        self.returning = 0

    # calls options, feeds response into execute
    def visitTemple(self):
        if not self.returning:
            self.firstVisit()
            self.returning = 1
        print("\n'Welcome back to the Temple, Traveller. How might we be of "
              "service?'")
        self.templeOptions()
        choice = input().upper()
        self.execute(choice)

    # prints temple options depending on money and status
    def templeOptions(self):
        print("P) Ask for a Prayer")
        if self.p1.stats["money"] >= 25:
            print("D) Make a $25 Donation")
        if self.p1.items["artifacts"]:
            print("A) Turn in Artifacts")
        if self.p1.stats["holiness"] == "Holy" and \
                not self.p1.equipment["Redeemer"]:
            print("E) Be Enlightened")
        print("L) Leave the Temple")

    # executes player choice. also a hodgepodge of temple-specific mechanics
    def execute(self, choice):
        if choice == "P" and self.p1.stats["holiness"] != "Infidel":
            self.p1.stats["sanctity"] += 4
            narratives.goodPrayer()
            print("\nWith that, your Sanctity increases by 4.")
        elif choice == "P" and self.p1.stats["holiness"] == "Infidel":
            self.p1.stats["sanctity"] += 4
            narratives.badPrayer()
            print("\nWith that, your Sanctity increases by 4.")
        elif choice == "D":
            self.p1.stats["sanctity"] += 15
            self.p1.stats["money"] -= 25
            narratives.donation()
            print("\nWith that, your Sanctity increases by 12. Kind of "
                  "scummy, huh?")
        elif choice == "A":
            print(f"\nYou have {self.p1.items['artifacts']} Artifacts. How "
                  "many would you like to return to the church?")
            artifactNum = int(input())
            self.p1.items["artifacts"] -= artifactNum
            tDecrease = 3 * artifactNum
            self.p1.stats["trading"] -= tDecrease
            sIncrease = 7 * artifactNum
            self.p1.stats["sanctity"] += sIncrease
            narratives.artifactReturn()
            print(f"\nFor donating {artifactNum}, you gained {sIncrease} "
                  f"Sanctity, though you did lose {tDecrease} Trading.")
        elif choice == "E":
            narratives.enlightenment()
            self.p1.equipment["Redeemer"] = True
            self.p1.equipment["Shear"] = False
            self.p1.equipment["Slayer"] = False
            print("\nYou have now earned The Redeemer. With The Redeemer "
                  "you will get a larger Sanctity bonus for not killing "
                  "Demons, however the other interests in Town my not be so "
                  "happy. Beware, if you lose your 'Holy' status or accept a different "
                  "Special Weapon it will no longer be available.")
        elif choice == "L":
            pass

    # only run the first time user goes to temple
    def firstVisit(self):
        narratives.firstTemple()
        if self.p1.stats["sanctity"] < 50:
            narratives.fTGBad()
        else:
            narratives.fTGood()
        if self.p1.items["artifacts"]:
            narratives.fTYA()
        else:
            narratives.fTNA()
