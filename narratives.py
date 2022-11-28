def disclaimer():
    print("\nWelcome to Ascendancy, an adventure through a word of "
          "mysterious beasts and competing interests. Please be careful "
          "text entry. While capitalization does not matter, it is "
          "imperative that you enter the character(s) before the ). It is "
          "also suggested for exposition's sake that upon your first trip to "
          "the Town, you first go to the Town Square I hope you enjoy your "
          "journey!")

def open():
    print("It has been long since you have seen Esme and Abraham. You "
          "remember the day the left every night in your sleep. Torn away "
          "intro nothingness by the beast. The wretched hell-spawn beast. "
          "Massive and ferocious yet seemingly weightless. A dark mass devoid "
          "of any God's touch. Long have you searched for them down the "
          "King's road. Long have you found nothing but strife. Ever further "
          "do you journey, ever more a looming darkness grows over you.")


def battle(eType):
    if eType == "sheep":
        print("\nYou come across a sheep grazing. Murderous rage fills your "
              "heart... or maybe it doesn't. Regardless, you prepare to "
              "attack.")

    elif eType == "nPr":
        print("\nA horrible cloud amasses in front of you, Covered with "
              "scales constantly changing placement and order. You wonder if "
              "you could determine the possibilities of this apparition and "
              "use your knowledge against it. This ~thing~ cannot remain.")

    elif eType == "seq":
        print("\nA horrible cloud amasses in front of you. It appears like a "
              "horrid floating snake, long and slender. It does have the "
              "peculiarity of seemingly being broken in one area. It's as if "
              "there is the implication of more body. Maybe you could exploit "
              "that. Regardless, it is clearly up to you do stop it.")

    elif eType == "sol":
        print("\nA horrible cloud amasses in front of you. It takes a form "
              "that hurts your brain. It appears like an ouroboros, but in a "
              "series of inconceivable dimensions. It feeds in and out of "
              "itself. Maybe if you could predict where a certain part was "
              "you could deliver a fatal strike. Until then, you must do "
              "whatever you can to defeat it.")


def playerDeaths(quality):
    if quality == "Holy":
        print("\nYou are knocked to the ground. The will to stand seems to "
              "escape you. You know you cannot carry on this fight. Just as "
              "the world begins to escape from around you a blinding light "
              "appears. In it you see Esme and Abraham smiling down at you. A"
              "drive like no other fills you, one of love and determination. "
              "You still feel weak, but you are able to scramble to your "
              "feet. You can't give up now. Perhaps you have been Chosen for "
              "this journey. By whom you cannot know, but you love them "
              "nonetheless. For now, at least, you will push on.")

    elif quality == "Infidel":
        print("\nThe attack throws you down. You know you have lost this "
              "battle. You wonder what will await when you pass on, but as "
              "the energy leaves you all that you find is darkness. A deep, "
              "cold dark like you could neve imagine. All you wish is to see "
              "your wife and child one more time, but your wishes are met "
              "with lonely silence. You are truly alone as you fade into the "
              "void.")

    elif quality == "Hero":
        print("\nThe beast before you hits you with a force you knew not to "
              "be possible. As you lie in the cold mud you wonder if this is "
              "your end. You wonder what will become of the townsfolk. As you "
              "fade into darkness you hear a commotion. Through your "
              "bleariness you see familiar faces from the city. A number of "
              "them seem to confront your enemy as two more begin to drag you "
              "away. Before you lose consciousness you are able to croak out "
              "a word of gratitude to your saviors, those whom you have "
              "fought so hard to protect.")

    else:
        print("\nA piercing pain shoots through you as you fall to the earth "
              "below. This time you can't get up. It is time to accept that "
              "this is your fate. As the light fades around you a calming "
              "warmth soothes you. You think once more of Esme and Abraham "
              "and pray that wherever they are, they know you love them. If "
              "nothing else, at least the world will know you tried.")


def firstTemple():
    print("\nYou approach the Temple. Compared to the city it is a massive "
          "structure. Meticulously crafted, yet elegantly simple. You push "
          "through the large wooden doors and are greeted by hymns and "
          "incense. A Cleric greets you.\n\n'Good day, Traveller. Welcome to "
          "our place of prayer. Here we can honor ALL life purely and without "
          "distraction.'")


def fTGood():
    print("\nThe Cleric continues. 'It seems as though you have respected "
          "life so far on your travels. That is good to hear. Some are not so "
          "receptive to our beliefs. Well, that's nothing that a small "
          "donation couldn't fix, anyway. Before I forget, have you come "
          "across any misplaced artifacts? I'm sure you've seen the Demons "
          "about. Well they tore through town a bit ago and scattered many of "
          "our artifacts.'")


def fTGBad():
    print("\nThe Cleric continues. 'It seems as though you have not respected "
          "life so far on your travels. That is sad to hear. Many are not so "
          "receptive to our beliefs. Well, that's nothing that a small "
          "donation couldn't fix, anyway. Before I forget, have you come "
          "across any misplaced artifacts? I'm sure you've seen the Demons "
          "about. Well they tore through town a bit ago and scattered many of "
          "our artifacts.'")


def fTNA():
    print("\n'I'm sorry, but I haven't found any,' you reply.\n\n'That's too "
          "bad,' says the Cleric. 'Well if you do ever find any, the church "
          "would be very grateful if you returned them.'\n")


def fTYA():
    print("\n'Actually, yes,' you respond. 'I was wonder what that was. \n\n"
          "'Well then,' says the Cleric with new enthusiasm, 'we would "
          "greatly appreciate it if you would return it. I'm sure the Life "
          "Spirits would smile down on you for it.'\n")


def goodPrayer():
    print("\nA true passion and reverence undertone the Cleric's mumbled "
          "prayer. It sounds like an unrecognizable language, but that "
          "bothers you not. As he speaks, you feel your connecting with the "
          "living world around you strengthening. Maybe there is something to "
          "this religion.")


def badPrayer():
    print("\nBegrudgingly, the Cleric agrees. He is one for forgiveness. He "
          "speaks in some weird foreign language. Who cares. Whatever it "
          "takes to gain their favor, right?")


def donation():
    print("\n'Thank you very much for you generous Donation!' exclaims the "
          "Cleric. 'There is much good that we can do with this Money. You "
          "can be sure your generosity has been noted.'")


def artifactReturn():
    print("\n'You've found an artifact,' the Cleric says excitedly. 'I wish "
          "we could repay you for you noble deed!'")


def enlightenment():
    print("\nThe Cleric speaks, 'Traveller, we have come to understand your "
          "Holiness. For that, we would like to gift you with this, The "
          "Redeemer.' He hands you a beautiful sword. Like the Temple, it is "
          "meticulously crafted, but not garish. He continues, 'With "
          "this, instead of incapacitating or... killing... the Demons, you "
          "can instead return their souls to Life Spirits.'")


def firstSquare():
    print("\nAs you walk into the Town Square you are met by a group of "
          "concerned Townsfolk. One beckons you over. 'Here here, traveller, "
          "have you just come from outside of Town? You must know that it has "
          "become quite dangerous out there. There are Demons all about! They "
          "keep killing our flocks. It was bad enough with the poachers about "
          "I tell you. Word is that they are being spawned from a beast like "
          "one couldn't imagine over yonder. They call it... Thon Bane.'\n\n"
          "You could feel the air tense up at the utterance of the name.")


def goodSquare():
    print("\n'It seems like you've been doing a good enough job keeping "
          "our lands safe. Here, have some bread.'\n\nThe person hands you "
          "some bread. After thanking them you quickly scarf it down. you "
          "start feeling a bit better.\n\n'As long as you keep putting in the "
          "work, there will always be warm bread here for you.'\n")


def badSquare():
    print("\n'It doesn't seem like you've been much of a help, anyway. Maybe "
          "if you spent more on killing those Demons instead of our Sheep it "
          "wouldn't be so hard around here. I'd share with you my bread, but "
          "it doesn't seem like you'd put it to any good use. Come back when "
          "you've done something food for a change.'\n")


def noBread():
    print("\n'You do nothing for this town and then ask us for Food? get out "
          "of here. Come back when you actually help us!'")


def yesBread():
    print("\n'We appreciate what you have done for use. Of course, have some "
          "Food.'")

def elevate():
    print("\nA towns person approaches you with a robust looking bladed "
          "implement.\n\n'Traveller, to show our gratitude for all you've "
          "done for us we would like to give you this, the Shear. This will "
          "allow you to harvest plentiful amounts of our wool without "
          "having to kill our sheep.'")


def firstMarket():
    print("\n'Hello, Traveller. Welcome to the Market. Here you can buy and "
          "sell items.'\n\nThe Merchant who greeted you gives you a once "
          "over. It's as though he's pricing you. It makes you somewhat "
          "uncomfortable.")


def goodMarket():
    print("\n'I hear you've been doing well, should I say... harvesting, "
          "the natural resources of these fertile lands. Keep doing that and "
          "my colleagues and I can make you a very well endowed individual. "
          "Anything you collect in the field we will be more than happy to "
          "relieve you of. And don't worry about the others in Town. The "
          "Clerics are cooks and the commoners are powerless. We run the show "
          "here. Feel free to visit a stall at any time if you'd like to make "
          "an exchange.'\n\nThe Merchant spoke with a serpent's tongue, but "
          "you could use some Money. You wonder what they may have available.")


def badMarket():
    print("\n'It seems like you have no mind for business, though. What are "
          "you, one of those pacifist cultists? Listen, go back out there "
          "~collect~ some resources, and then maybe we can start building a "
          "relationship. The Merchants can make you a very powerful "
          "individual, but only if you're willing to bring something to the "
          "table. Anyway, if you do have anything to exchange, you can visit "
          "one of the stalls in the Market.")


def hunter():
    print("\n'You've done a good job, Traveller. Brought us a lot of good "
          "stuff. Here, take this.'\n\nThe Merchant hands you a large sword. "
          "\n\n'This will cut right through those demons. You should also be "
          "able to get some extra Meat and Wool off of the Sheep.'")


def thonBaneHolyIntro():
    print("\nOn your way out of town you are stopped by a Cleric.\n\n"
          "'Traveller, I heard you are on the road to face Thon Bane. When "
          "the time comes, I hope you will make the right decision. You've "
          "walked the Holy path thus far. The spirits smile down on you.'\n\n"
          "After a long trek, you reach him lingering in the ruins of what "
          "a homestead. Whereas the Demons you could almost describe, this... "
          "thing gives you a headache just looking at it. It exudes hateful "
          "energy and seems to cast a shadow on the open sky. You've come "
          "far, there's no turning back. You will Redeem Thon Bane.")


def thonBaneHeroIntro():
    print("\nOn your way out of town you are stopped by a commoner.\n\n"
          "'Traveller, I heard you are on the road to face Thon Bane. It "
          "escapes me how one could acquire such courage, but if no one could "
          "we would truly by doomed. I only wish there was a way for us to "
          "thank you.'\n\n After a long trek, you reach him lingering in the "
          "ruins of what a homestead. Whereas the Demons you could almost "
          "describe, this... thing gives you a headache just looking at it. "
          "It exudes hateful energy and seems to cast a shadow on the open "
          "sky. You've come far, there's no turning back. You will defeat "
          "Thon Bane.")

def thonBaneHunterIntro():
    print("\nOn your way out of town you are stopped by a Merchant.\n\n"
          "'Traveller, word is you are on the road to face Thon Bane. I can't "
          "imagine how many Scales he may leave behind. Destroy him. And "
          "bring back whatever's left. We can make a fortune.\n\n After a "
          "long trek, you reach him lingering in the ruins of what a "
          "homestead. Whereas the Demons you could almost describe, this... "
          "thing gives you a headache just looking at it. It exudes hateful "
          "energy and seems to cast a shadow on the open sky. You've come "
          "far, there's no turning back. You will destroy Thon Bane.")


def thonHolyHelp():
    print("\nEvery strike, your strength drains. It becomes apparent that "
          "your resolve may not be enough to carry you through. Despite that, "
          "you know this is a battle you cannot afford to lose. Behind you is "
          "a beautiful land brimming with life. To let that be consumed by "
          "such an evil darkness would be sorrow beyond all compare\n\n"
          "Just as you think you are going to fall, you are filled with "
          "a vigor like never before. A column of light beams from the sky. "
          "Within it, a single, massive bolt of lightning shoots down towards "
          "Thon Bane followed shortly by a boom that nearly forces you off "
          "feet. As you regain your composure, you see your wretched foe is "
          "fairing no better. Smoldering and with a chunk of what you can "
          "only describe as his body taken out of the side. You wonder if "
          "there was someone watching out for you. Something from above. "
          "Something from beyond.")


def thonHeroHelp():
    print("\nYour courage remains unyielding, but you worry that your strength "
          "may not be so infallible. You can't afford to lose this battle. "
          "The Townsfolk you've fought so har to protect can't afford for you "
          "to lose this battle. If not you then who?\n\nYou wonder how much "
          "more you can take. Just as Thon Bane readies another attack, "
          "previously hidden figure rush from the shadows. They're... the "
          "commoners. The Townsfolk. They must have followed you. Perhaps you "
          "inspire them. Perhaps they are just grateful for your help. "
          "Anyway, it gives you a moment to recover as they take turns "
          "attacking. You are ready to rejoin the fight. You WILL win.")


def thonHunterHelp():
    print("\nYou can feel yourself weakening. You wish you could call in "
          "support. An extra hand from a towns person. Hell, an act of God."
          "You wish could call for help. But you know no one would listen.")


def thonHolyDeath():
    pass


def thonHeroDeath():
    pass


def thonHunterDeath():
    pass
