import random
import narratives
import questions


class ThonBane():

    def __init__(self, p1):
        self.p1 = p1
        self.health = 100
        self.sAttackCount = 0
        self.opener()
        self.aBreak = False
        self.death = self.battle()

    def opener(self):
        if self.p1.stats["holiness"] == "Holy":
            narratives.thonBaneHolyIntro()
        if self.p1.stats["goodliness"] == "Hero":
            narratives.thonBaneHeroIntro()
        if self.p1.stats["mercantilism"] == "Hunter":
            narratives.thonBaneHunterIntro()

    def equip(self):
        print("\nWhich weapon would you like to equip?")

        print("1) Sword\n2) Stick")
        if self.p1.equipment["Slayer"]:
            print("Sl) Slayer")
        if self.p1.equipment["Shear"]:
            print("Sh) Shear")
        if self.p1.equipment["Redeemer"]:
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


    def attack(self):
        print(f"\nYou attacked the Thon Bane doing {self.p1.hitPoints} "
              "damage.")
        self.health -= self.p1.hitPoints

    def fireball(self):
        print("\nYou cast a fireball at Thon Bane doing 20 damage!")
        self.health -= 20

    def specialAttack(self):
        qType = random.randrange(1, 4)
        if qType == 1:
            question = questions.nPrQuestions(random.randrange(1, 5))
        if qType == 2:
            question = questions.sequenceQuestions(random.randrange(1, 5))
        if qType == 3:
            question = questions.solutionQuestions(random.randrange(1, 5))
        answer = input(question[0] + "\n")
        if answer == question[1]:
            damage = self.p1.hitPoints + 9
            self.health -= damage
            print(f"\nThon Bane took {damage} damage!")
        else:
            print("\nYour attack missed!")

    def helpCall(self):
        if self.p1.stats["holiness"] == "Holy":
            narratives.thonHolyHelp()
            self.health -= 25
            print("\nThon Bane took 25 damage!")
        elif self.p1.stats["goodliness"] == "Hero":
            narratives.thonHeroHelp()
            for i in range(3):
                damage = random.randrange(15)
                self.health -= damage
                print(f"\nThon Bane took {damage} damage!")
        elif self.p1.stats["holiness"] == "Holy":
            narratives.thonHunterHelp()
            self.p1.stats["health"] -= 3
            print("\nYou take 3 damage!")

    def fight(self):
        damage = random.randrange(0, 31)
        if self.p1.berserkStatus:
            damage -= 9
        if self.p1.equipment["armor"]:
            damage -= self.p1.equipment["armor rating"]
            self.p1.equipment["armor health"] -= 1
            self.aBreak = False
            if self.p1.equipment["armor health"] <= 0:
                self.p1.equipment["armor"] = False
                self.p1.equipment["armor rating"] = 0
                self.p1.equipment["armor health"] = 0
                self.aBreak = True
        self.p1.stats["health"] -= damage
        print("Suddenly, what must be the head of the beast emerges and " +
              f"bites you causing {damage} damage.") # change
        if self.aBreak:
            print("Your Armor broke!")

    def thonBaneOptions(self):
        print("\nWhat action would you like to perform?\nA) Attack")
        if self.p1.equipped not in ["Slayer", "Redeemer"]:
            print("R) Re-Equip")
        if self.sAttackCount < 2:
            print("S) Special Attack")
        if self.p1.items["fireballs"]:
            print("Fi) Use Fireball")
        if self.p1.items["potions"] and not self.p1.berserkStatus:
            print("P) Use Potion")
        if self.p1.items["food"] and not self.p1.berserkStatus:
            print("Fo) Eat Food")
        if self.p1.items["berserk"]:
            print("B) Use Berserk")
        if self.p1.stats["health"] <= 20:
            print("C) Call for help")

    def execute(self, choice):
        if choice == "A":
            self.attack()
        elif choice == "R":
            self.equip()
            print("\n")
        elif choice == "S":
            self.specialAttack()
            self.sAttackCount += 1
        elif choice == "FI":
            self.fireball()
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
        elif choice == "C":
            self.helpCall()


    def battle(self):
        self.equip()
        while self.p1.stats["health"] > 0 and self.health > 0:
            self.thonBaneOptions()
            choice = input().upper()
            self.execute(choice)

            if self.p1.stats["health"] < 0:
                self.p1.stats["health"] = 0
                break
            if self.health < 0:
                self.health = 0
                break

            self.fight()

            print(f"\nHealth: {self.p1.stats['health']}    "
                  f"Thon Bane Health: {self.health}")

        self.p1.statsUpdate()

        if self.p1.stats["health"] <= 0:
            return self.p1.death()
        elif self.health <= 0:
            if self.p1.stats["holiness"] == "Holy":
                narratives.thonHolyDeath()
            elif self.p1.stats["goodliness"] == "Hero":
                narratives.thonHeroDeath()
            elif self.p1.stats["holiness"] == "Holy":
                narratives.thonHunterDeath()
        # add in end game
