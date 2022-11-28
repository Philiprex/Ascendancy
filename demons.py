from abc import ABC, abstractmethod
import random
import questions


class Demon(ABC):

    def __init__(self, p1):
        self.p1 = p1
        self.health = None
        self.aBreak = False

    @abstractmethod
    def fight(self):
        pass

    @abstractmethod
    def specialAttack(self):
        pass

    def attack(self):
        print(f"\nYou attacked the demon doing {self.p1.hitPoints} damage.")
        self.health -= self.p1.hitPoints

    def fireball(self):
        print("\nYou cast a fireball at the demon doing 20 damage!")
        self.health -= 20

    def death(self):
        if self.p1.equipped == "sword":
            self.p1.stats["sanctity"] -= 5
            self.p1.stats["goodness"] += 5
            self.p1.stats["trading"] += 5
            self.p1.items["demon scales"] += 1
            print("\nAs you cast your final strike the beast lets out a "
                  "horrible screech and collapses in on itself. You won't "
                  "have to worry about that creature again. You take a Scale "
                  "from its ash-pile remains. You're sure the townspeople "
                  "will be happy to hear of its demise, though you feel weird "
                  "about killing it for some reason.")

        elif self.p1.equipped == "Slayer":
            self.p1.stats["sanctity"] -= 5
            self.p1.stats["goodness"] += 5
            self.p1.stats["trading"] += 10
            newScales = random.randrange(1, 6)
            self.p1.items["demon scales"] += newScales
            print("\nYour last thrust pierces directly through the "
                  "horrid being. Its terrible cry tears through "
                  "the air and it torn to shred before your eyes. " 
                  "All that is left behind are a few of its Scales. You "
                  f"collect {newScales} of them and go on your way. The "
                  "darkness in you grows.")

        elif self.p1.equipped == "stick":
            self.p1.stats["sanctity"] += 5
            self.p1.stats["goodness"] -= 5
            self.p1.stats["trading"] -= 5
            print("\nYou hit it a final time and it seems to become "
                  "incapacitated. You're not sure if that was enough, but "
                  "it will have to do for now.")

        elif self.p1.equipped == "Redeemer":
            self.p1.stats["sanctity"] += 10
            self.p1.stats["goodness"] -= 5
            self.p1.stats["trading"] -= 5
            self.p1.items["souls"] += 1
            print("\nAs you slice into the creature light begins to explode "
                  "from within. A piercing yet beautiful cry emerges as the "
                  "damned soul contained within is sucked into The "
                  "Redeemer. You may not have gained anything of "
                  "monetary value, but at least you know the Clerics can "
                  "finally give peace to this damned being.")


class NPRDemon(Demon):

    def __init__(self, p1):
        super().__init__(p1)
        self.type = "nPr"
        self.health = 20

    def fight(self):
        damage = random.randrange(1, 6)
        if self.p1.berserkStatus:
            damage -= 3
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
        print("The beast throws a barrage of dark material at you doing " +
              f"{damage} damage")
        if self.aBreak:
            print("Your Armor broke!")

    def specialAttack(self):
        question = questions.nPrQuestions(random.randrange(1, 5))
        answer = input(question[0] + "\n")
        if answer == question[1]:
            damage = self.p1.hitPoints + 10
            self.health -= damage
            print(f"\nDemon took {damage} damage!")
        else:
            print("\nYour attack missed!")


class SeqGuessDemon(Demon):

    def __init__(self, p1):
        super().__init__(p1)
        self.type = "seq"
        self.health = 30

    def fight(self):
        damage = random.randrange(5, 16)
        if self.p1.berserkStatus:
            damage -= 10
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
        print(f"The beast whips its tail at you causing {damage} damage.")
        if self.aBreak:
            print("Your Armor broke!")


    def specialAttack(self):
        question = questions.sequenceQuestions(random.randrange(1, 5))
        answer = input(question[0] + "\n")
        if answer == question[1]:
            damage = self.p1.hitPoints + 15
            self.health -= damage
            print(f"\nDemon took {damage} damage!")
        else:
            print("\nYour attack missed!")


class SolutionDemon(Demon):

    def __init__(self, p1):
        super().__init__(p1)
        self.type = "sol"
        self.health = 50

    def fight(self):
        damage = random.randrange(0, 21)
        if self.p1.berserkStatus:
            damage -= 10
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
              f"bites you causing {damage} damage.")
        if self.aBreak:
            print("Your Armor broke!")


    def specialAttack(self):
        question = questions.solutionQuestions(random.randrange(1, 5))
        answer = input(question[0] + " Y/N\n")
        if answer.upper() == question[1]:
            damage = self.p1.hitPoints + 20
            self.health -= damage
            print(f"\nDemon took {damage} damage!")
        else:
            print("\nYour attack missed!")
