import narratives


class Battle():

    def __init__(self, p1, enemy):
        self.p1 = p1
        self.enemy = enemy
        self.specialCounter = 0
        narratives.battle(enemy.type)
        self.equip()
        self.death = self.battle()


    # depending on what's available, offers weapon options. Sets equipped and hitPoints
    def equip(self):
        print("\nWhich weapon would you like to equip?")

        print("1) Sword\n2) Stick")
        if self.p1.equipment["Slayer"]:
            print("Sl) Slayer")
        if self.p1.equipment["Shear"] and self.enemy.type == "sheep":
            print("Sh) Shear")
        if self.p1.equipment["Redeemer"] and self.enemy.type != "sheep":
            print("R) Redeemer")

        weapon = input()

        if weapon == "1":
            self.p1.equipped = "sword"
            self.p1.hitPoints = 7
        elif weapon == "2":
            self.p1.equipped = "stick"
            self.p1.hitPoints = 5
        elif weapon.upper() == "SL":
            self.p1.equipped = "Slayer"
            self.p1.hitPoints = 12
        elif weapon.upper() == "SH":
            self.p1.equipped = "Shear"
            self.p1.hitPoints = 9
        elif weapon.upper() == "R":
            self.p1.equipped = "Redeemer"
            self.p1.hitPoints = 9

    # provides action inputs
    def battleOptions(self):
        print("\nWhat action would you like to perform?\nA) Attack")
        if self.p1.equipped not in ["Slayer", "Redeemer"]:
            print("R) Re-Equip")
        if not self.specialCounter and self.enemy.type != "sheep":
            print("S) Special Attack")
        if self.p1.items["fireballs"]:
            print("Fi) Use Fireball")
        if self.p1.items["potions"] and not self.p1.berserkStatus:
            print("P) Use Potion")
        if self.p1.items["food"] and not self.p1.berserkStatus:
            print("Fo) Eat Food")
        if self.p1.items["berserk"]:
            print("B) Use Berserk")

    # executes action
    def execute(self, choice):
        if choice == "A":
            self.enemy.attack()
        elif choice == "R":
            self.equip()
            print("\n")
        elif choice == "S":
            self.enemy.specialAttack()
            self.specialCounter += 1
        elif choice == "FI":
            self.enemy.fireball()
            self.p1.items["fireballs"] -= 1
        elif choice == "P":
            self.p1.stats["health"] += 20
            self.p1.items["potions"] -= 1
            print("\nYou drank a potion and gained 20 health!\n")
        elif choice == "FO":
            self.p1.stats["health"] += 7
            self.p1.stats["food"] -= 1
            print("\nYou ate some bread. You can taste the care " +
                  "put into it by the baker. You gain 7 health!\n")
        elif choice == "B":
            self.p1.items["berserk"] -= 1
            self.p1.berserkStatus = True
            print("\nYou feel unstoppable. Your foe WILL be defeated!\n")

    def battle(self):
        while self.p1.stats["health"] > 0 and self.enemy.health > 0:
            self.battleOptions()
            choice = input().upper()
            self.execute(choice)

            if self.p1.stats["health"] < 0:
                self.p1.stats["health"] = 0
                break
            if self.enemy.health < 0:
                self.enemy.health = 0
                break

            self.enemy.fight()

            print(f"\nHealth: {self.p1.stats['health']}    Enemy Health: {self.enemy.health}")

        self.p1.statsUpdate()

        if self.p1.stats["health"] <= 0:
            return self.p1.death()
        elif self.enemy.health <= 0:
            self.enemy.death()
            return False
