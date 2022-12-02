import narratives

class Market():

    def __init__(self, p1):
        self.p1 = p1
        self.returning = 0
        self.hasItems = False
        self.items = {
            "wool": False,
            "meat": False,
            "artifacts": False,
            "demon scales": False
        }

    # calls options, feeds response into execute
    def visitMarket(self):
        if not self.returning:
            self.firstVisit()
            self.returning = 1
        print("\n'Good day, Traveller. What can I interest you it?'")
        self.marketOptions()
        choice = input().upper()
        self.execute(choice)

    # prints market options depending on money and status
    def marketOptions(self):
        self.checkItems()
        if self.hasItems:
            print("S) Sell Items")
        if self.p1.stats["money"] >= 9:
            print("B) Buy Items")
        if self.p1.stats["mercantilism"] == "Hunter" and \
                not self.p1.quipment["Slayer"]:
            print("H) Become Hunter")
        print("L) Leave Market")

    # hodgepodge of buy/sell mechanics and executing simple commands
    def execute(self, choice):
        if choice == "S":
            self.sellOptions()
            choice = input().upper()
            if choice == "L":
                pass
            elif choice == "W":
                self.sell("wool", "Wool", 2)
            elif choice == "M":
                self.sell("meat", "Meat", 5)
            elif choice == "A":
                a = self.sell("artifacts", "Artifacts", 20)
                self.p1.stats["sanctity"] -= 3 * a
                print("\nThe Clerics have take note of your irreverence.")
            elif choice == "S":
                self.sell("demon scales", "Scales", 10)
        elif choice == "B" and self.p1.stats["mercantilism"] != "Leech":
            self.buyOptions()
            choice = input().upper()
            if choice == "L":
                pass
            elif choice == "P":
                self.buy("potions", "Potions", 15)
            elif choice == "F":
                self.buy("fireballs", "Fireballs", 9)
            elif choice == "B":
                self.buy("berserk", "Berserk", 30)
            elif choice == "A":
                self.buyArmor("Armor", 20, 4, 10)
            elif choice == "AA":
                self.buyArmor("Advanced Armor", 35, 7, 20)
        elif choice == "B":
            print("\n'I don't want to sell to you. You don't bring "
                  "enough to Market to be taking out of it!'")
        elif choice == "H":
            narratives.hunter()
            self.p1.equipment["Redeemer"] = False
            self.p1.equipment["Shear"] = False
            self.p1.equipment["Slayer"] = True
            print("\nYou are handed the Slayer. This powerful Weapon provides "
                  "bountiful harvests and damns Demon Souls back to whatever "
                  "hell they came from. The Clerics may disapprove, but with "
                  "this Weapon they can do nothing to stop you. Beware, if "
                  "you lose your 'Hunter' status or accept a different "
                  "Special Weapon it will no longer be available.")
        elif choice == "P":
            pass

    # provides selling options based on availability
    def sellOptions(self):
        print("\nWhat would you like to sell?")
        if self.items["wool"]:
            print("W) Wool")
        if self.items["meat"]:
            print("M) Meat")
        if self.items["artifacts"]:
            print("A) Artifacts")
        if self.items["demon scales"]:
            print("S) Demon Scales")
        print("L) Leave Market")

    # executes a sale based on number the player wants to sell
    def sell(self, item, itemName, price):
        print(f"\nYou have {self.p1.items[item]} {itemName}. How many would "
              f"you like to sell for ${price} each?")
        sellNum = int(input())
        self.p1.items[item] -= sellNum
        self.p1.stats["money"] += sellNum * price
        print(f"\nYou have sold {sellNum} {itemName} for ${sellNum * price}.")
        if item == "artifacts":
            return sellNum

    # provides buying options based on money
    def buyOptions(self):
        print("\nWhat would you like to buy?")
        if self.p1.stats["money"] >= 15:
            print("P) +20 Health Potion: Cost $15")
        if self.p1.stats["money"] >= 9:
            print("F) 20 damage Fireballs: Cost $9")
        if self.p1.stats["money"] >= 30:
            print("B) Berserk: Cost $30 Berserk greatly reduces damage "
                  "taken, even allowing negative damage. Beware, you will not "
                  "be able to heal whit Berserk active and it only "
                  "deactivates once you return to Town.")
        if self.p1.stats["money"] >= 20:
            print("A) 4 defense Armor: Cost $20")
        if self.p1.stats["money"] >= 35:
            print("AA) 7 defense Advanced Armor: Cost $35")
        print("L) Leave Market")

    # executes buy based on number a player wants to buy
    # includes suggested max based on available funds, but no enforcement
    def buy(self, item, itemName, cost):
        print(f"\nHow many {itemName} would you like to buy for "
              f"{cost} each? Max: {self.p1.stats['money']//cost}")
        sellNum = int(input())
        self.p1.items[item] += sellNum
        self.p1.stats["money"] -= sellNum * cost
        print(f"\nYou have bought {sellNum} {itemName} for ${sellNum * cost}.")

    # armor gets its own buy cause it has multiple properties unlike others
    def buyArmor(self, itemName, cost, rating, health):
        print(f"\nAre you sure you would like to buy {itemName} "
              f"for ${cost}? Y/N")
        choice = input().upper()
        if choice == "Y":
            self.p1.stats["money"] -= cost
            self.p1.equipment["armor"] = True
            self.p1.equipment["armor rating"] = rating
            self.p1.equipment["armor health"] = health
        else:
            pass

    # checks if the user has anything they can sell
    def checkItems(self):
        for i in self.p1.items:
            if i in ["potions", "food", "fireballs", "souls", "berserk"]:
                continue
            else:
                if self.p1.items[i] != 0:
                    self.items[i] = True
                else:
                    self.items[i] = False
        self.hasItems = False
        for i in self.items:
            if self.items[i]:
                self.hasItems = True
                break

    # only run the first time user goes to market
    def firstVisit(self):
        narratives.firstMarket()
        if self.p1.stats["trading"] < 50:
            narratives.badMarket()
        else:
            narratives.goodMarket()
