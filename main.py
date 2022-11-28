import time
from player import Player
from openingScene import OpeningScene
from expedition import Expedition
from temple import Temple
from townSquare import TownSquare
from market import Market
from thonBane import ThonBane


gameOver = False


def statusCheck(p1):
    print("\nItems")
    print(
        f"Potions: {p1.items['potions']}         "
        f"Food: {p1.items['food']}         "
        f"Wool: {p1.items['wool']}\n"
        f"Meat: {p1.items['meat']}            "
        f"Artifacts: {p1.items['potions']}    "
        f"Fireballs: {p1.items['fireballs']}\n"
        f"Demon Scales: {p1.items['demon scales']}    "
        f"Souls: {p1.items['souls']}        "
        f"Berserk: {p1.items['berserk']}"
    )
    print()
    print("Equipment")
    print(f"Sword    Stick")
    if p1.equipment["Shear"]:
        print("Shear")
    elif p1.equipment["Slayer"]:
        print("Slayer")
    elif p1.equipment["Redeemer"]:
        print("Redeemer")
    if p1.equipment["armor"]:
        print(f"Armor Rating: {p1.equipment['armor rating']}    "
              f"Armor Health: {p1.equipment['armor health']}")
    print()
    print("Stats")
    print(
        f"Health:   {p1.stats['health']}\n"
        f"Money:    {p1.stats['money']}\n"
        f"Sanctity: {p1.stats['sanctity']} '{p1.stats['holiness']}'\n"
        f"Goodness: {p1.stats['goodness']} '{p1.stats['goodliness']}'\n"
        f"Trading:  {p1.stats['trading']} '{p1.stats['mercantilism']}'"
    )


def actionOptions(p1):
    print("\nWhat would you like to do?")
    print("I) Check Inventory")
    if not p1.inTown:
        print("T) Go to Town")
        print("E) Continue Expedition")
    elif p1.inTown:
        print("C) Visit the Clerics' Temple")
        print("M) Visit the Merchants' Market")
        print("S) Visit the Town Square")
        print("L) Leave Town")
    if p1.inTown and ((p1.stats["holiness"] == "Holy" and
                       p1.equipment["Redeemer"])
                      or (p1.stats["goodliness"] == "Hero" and
                      p1.equipment["Shear"])
                      or (p1.stats["mercantilism"] == "Hunter" and
                      p1.equipment["Slayer"])):
        print("A) Go to Anomaly to face Thon Bane")


def execute(p1, choice):
    if choice == "I":
        statusCheck(p1)
    elif choice == "T" and not p1.inTown:
        p1.inTown = True
    elif choice == "E" and not p1.inTown:
        return journey.range()
    elif choice == "C" and p1.inTown:
        temple.visitTemple()
    elif choice == "M" and p1.inTown:
        market.visitMarket()
    elif choice == "S" and p1.inTown:
        townSquare.visitSquare()
    elif choice == "L" and p1.inTown:
        p1.inTown = False
        journey.range()
    elif choice == "A" and p1.inTown:
        return ThonBane(p1).death


# gameplay loop once done with opening scene
def generalPlay(p1):
    while not gameOver:
        actionOptions(p1)
        actionChoice = input().upper()
        death = execute(p1, actionChoice)
        if death:
            print("\nGame over.")
            time.sleep(1)
            break
        p1.statsUpdate()


# sets up play, expedition, and town, and plays opening scene
def playGame():
    global journey
    global temple
    global townSquare
    global market
    p1 = Player()
    journey = Expedition(p1)
    temple = Temple(p1)
    townSquare = TownSquare(p1)
    market = Market(p1)
    opening = OpeningScene(p1)
    del opening
    generalPlay(p1)


# prompt user whether they want to play
def start():
    choice = input("Would you like to play Ascendancy?\n0) No\n1) Yes\n")
    if choice == "0":
        print("\nOkay, have a nice day!")
        time.sleep(1)
    elif choice == "1":
        playGame()


start()
