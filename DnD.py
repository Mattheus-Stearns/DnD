import random
import sys, time
import math

clearWindow = 100*"\n"
print(clearWindow)



def print1by1(text, delay=0.05): #The game will run at 0.05 seconds per each character
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

print1by1("Would you like to play a game?(Y/N)\n\n")

counter = 1

while counter > 0:

    play = input().lower()

    if play != "y" and play != "n":

        counter += 1
        print1by1("Input Error: The values were neither (Y) or (N), therefore please try again:\n\n")

    if play == "n":

        sys.exit()

    if play == "y":

        counter = 0

    counter -= 1

   


print(clearWindow)

print1by1("Would you like to have the characters continue to Scroll (print each character one by one), or print in Blocks?(S/B)\n\n")

counter = 1

while counter > 0:

    delayCheck = input().lower()

    if delayCheck == "b":

        def print1by1(text, delay=0):
            for c in text:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(delay)
            print

    if delayCheck != "s" and delayCheck != "b":

        counter += 1
        print1by1("Input Error: The values were neither (S) or (B), therefore please try again:\n\n")

    else:

        counter = 0

    counter -= 1

    




print(clearWindow)
print1by1("Loading...")
print(clearWindow)

print("""
____________________________________________________________________________________________________________________________________________________________________________________________________
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

                                                                    Dungeons and Dragons:
                                                                                                         The Lost Mine of Phandelver

____________________________________________________________________________________________________________________________________________________________________________________________________
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


""")

print1by1("""
Welcome to the tavern! We are sitting down to play some Dungeons and Dragons. Do you have a character to play with?

I am sorry, I don't.

That's okay. Let's give you a choice of what possible (pregenerated) characters you can have, and their respective race and background.
Remember, the specific stats are STRENGTH (measuring physical power), DEXTERITY (measuring agility), CONSTITUTION (measuring endurance), INTELLIGENCE (measuring reasoning and memory), WISDOM (measuring perception and insight), and CHARISMA (measuring force of personality).

Also, I almost forgot. You will find out your hit points (depending on your character).
""")



# Giving the player the choice of the characters

print1by1("""
Okay! Here are the possible characters!

The Warriors

(1) A strong, charismatic human fighter who craves adventure, and was a soldier in a past life.

(2) A strong, engduring human barabarian who is a stranger to civilization, and was an outlander in a past life

(3) An intelligent, agile high elf who has studied the art of combat for decades, and was a sage in a past life.

(4) An agile, enduring halfling monk who's ascetic life tempered its endurance, and was an acolyte in a past life.

The Scoundrels

(5) A charismatic, agile drow rogue who became an expert in death, (of its own we can't tell), and was a charlatan in a past life.

(6) A charismatic, agile half-elf bard who has a vagobond's life, and was an entertainer in a past life.

(7) An enduring, intelligent halfling rogue who is completely self-sufficient, and was a criminal in a past life.

(8) A wise, agile elf ranger who is the epitome of a rugged individualist, and was an outlander in a past life.

The Mages

(9) A charismatic, enduring dragonborn sorcerer who is the ferocious wanderer of the untrodden ways, and was an outlander in a past life.

(10) An agile, intelligent elf wizard who craves the arcane knowledge of the eons long forgotten, and was a noble in a past life.

(11) A wise, enduring human driud who was marked from birth with supernatural gifts, and was a folk hero in a past life.

(12) A charasmatic, agile tiefling warlock who made a deal with a fiendish entity years ago, and was a hermit in a past life

The Healers

(13) A wise, strong dwarf cleric whos acts of artistry became acts of reverence, and was a guild jeweler in a past life.

(14) A strong, charismatic half-orc padalin, who has sworn vengence against those who would bring misery to the helpless, and was an outlander in a past life.

(15) A strong, wise human cleric who worships destructive weather, and was a pirate in the past life.

(16) A strong, enduring human paladin who follows the path of righteousness (everyone knows it), and was a noble in a past life.

Choose your character by entering a number from 1 to 16 (each number corresponding to each different character):


""")

playerCharacter = 0

while playerCharacter > 16 or playerCharacter < 1:

    try:

        playerCharacter = int(input(""))

        if int(playerCharacter) > 16 or int(playerCharacter) < 1:

            print1by1("Input Error: Input a number outside the range of selectable characters. Please try again:\n\n")

    except ValueError:

        print1by1("Input Error: Input something other than an integer. Please try again:\n\n")



# Introducting the variables

playerSTRENGTH = 0
playerDEXTERITY = 0
playerCONSTITUTION = 0
playerINTELLIGENCE = 0
playerWISDOM = 0
playerCHARISMA = 0

STRENGTH = 0
DEXTERITY = 0
CONSTITUTION = 0
INTELLIGENCE = 0
WISDOM = 0
CHARISMA = 0

# The character cheat sheets which the character will always have access to throughout the campaign

if playerCharacter == 1:

    playerSTRENGTH = 16
    playerDEXTERITY = 9
    playerCONSTITUTION = 15
    playerINTELLIGENCE = 13
    playerWISDOM = 11
    playerCHARISMA = 14

    playerCharacterInfo = '''

Race: Human

Class: Fighter

“Measure twice, cut once. Or two
or three times, whatever works. Maybe five.”

Background: Soldier

Alignment: Chaotic Good

Armor Class: 18

Hit Points: 12 (Hit Dice 1d10)

Speed: 30 ft.

Abilities:

    Strength (STR): 16 (+3)
    Dexterity (DEX): 9 (-1)
    Constitution (CON): 15 (+2)
    Intelligence (INT): 13 (+1)
    Wisdom (WIS): 11 (0)
    Charisma (CHA): 14 (+2)

Proficiencies:

    Saving Throws: Strength (+5), Constitution (+4)
    Skills: Athletics (+5), History (+3), Intimidation (+4), Perception (+2)
    Armor: All, shields.
    Weapons: Simple, martial.
    Tools: Gaming dice, vehicles (land)
    Senses: Passive Perception 12
    Languages: Common, Orc

Background Features:

    You were a professional soldier. You traveled to foreign lands, led troops into danger, fought wars under the banners of different commanders. 
    Yet, you craved something more out of life, and resigned your commission. Now you are out on your own, living by your wits, taking orders from no one.

    Military Rank: 
    
        You were a low-ranked officer in a military organization. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank.

    Faction: 
        
        Member of the Order of the Gauntlet, a devout and vigilant group that seeks to protect others from the depredations of evildoers.

Personality Traits:

    You can stare down a hell hound without flinching.

Ideal:

    When people follow orders blindly, they embrace a kind of tyranny.

Bond:

    You fight for those who cannot fight for themselves.

Flaw:

    You’d rather eat your armor than admit when you’re wrong.

Fighter Features:

    Fighting Style: 

        Protection: 

            When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.

        Second Wind: 
        
            On your turn, you can use a bonus action to regain 1d10 + 1 hit points. Once you use this feature, you must finish a short or long rest before you can use it again.

Equipment:

    Longsword
    Pike
    Javelin (5)
    Chain mail
    Shield
    Dungeoneer’s pack
    Potion of healing
    Money (30 gp, 5 sp)

Actions:

    Attack: You can attack when you take this action, using the following:
    
        Longsword: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1d8 + 3 slashing damage.
    
        Pike: Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 1d10 + 3 piercing damage.

        Javelin: Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 1d6 + 3 piercing damage.

    Bonus Actions:

        Second Wind: Regain 1d10 + 1 hit points.

    Reactions:

        Protection: Impose disadvantage on an attack against a target within 5 feet of you.


    '''

    print(playerCharacterInfo)

elif playerCharacter == 2:

    playerSTRENGTH = 16
    playerDEXTERITY = 14
    playerCONSTITUTION = 15
    playerINTELLIGENCE = 9
    playerWISDOM = 13
    playerCHARISMA = 11


    playerCharacterInfo = '''

Race: Human

Class: Barbarian

“The wild is in my blood.”

Background: Outlander

Alignment: Chaotic Good

Armor Class: 14 (Unarmored Defense)

Hit Points: 14 (Hit Dice 1d12)

Speed: 30 ft.

Abilities:

    Strength (STR): 16 (+3)
    Dexterity (DEX): 14 (+2)
    Constitution (CON): 15 (+2)
    Intelligence (INT): 9 (-1)
    Wisdom (WIS): 13 (+1)
    Charisma (CHA): 11 (+0)

Proficiencies:

    Saving Throws: Strength (+5), Constitution (+4); see the Danger Sense barbarian feature
    Skills: Athletics (+5), Intimidation (+2), Perception (+3), Survival (+3)
    Armor: Light armor, medium armor, shields
    Weapons: Simple weapons, martial weapons
    Tools: Drum
    Senses: Passive Perception 13
    Languages: Common, Dwarvish, Giant

Background Features:

    You grew up among tribal nomads, far from civilization and its comforts. You’ve hunted great herds, survived extreme weather, 
    raided the trade of softer folk, and protected places sacred to your people. At times, you’ve enjoyed the solitude of being the 
    only sentient creature for miles in any direction. Even in places where the terrain is new, you know the ways of the wild.

    Wanderer: 
        
        You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, 
        and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, 
        provided that the land offers enough.

    Faction: 
    
        Member of the Emerald Enclave, wilderness survivalists who preserve the natural order while rooting out unnatural threats.

Personality Traits:

    You place no stock in refined manners or wealth.

Ideal:

    Life is constant change, and you must change with it to survive.

Bond:

    You take the despoiling of the wilderness and sacred sites as a personal insult.

Flaw:

    There’s no room for caution in a life lived to the fullest.

Barbarian Features:

    Rage (Recharges after You Finish a Long Rest): 
        
        You can enter a rage as a bonus action. While raging, you have advantages on Strength checks and 
        Strength saving throws, gain a +2 bonus to damage rolls for melee weapon attacks using Strength, 
        have resistance to bludgeoning, piercing, and slashing damage, but can't cast or concentrate 
        on spells. Your rage lasts for 1 minute.

    Unarmored Defense: 
    
        While wearing no armor but even if you’re using a shield, your Armor Class equals 10 + your 
        Dexterity modifier + your Constitution modifier.

Equipment:

    Backpack
    Bearskin cloak
    Bedroll
    Drum
    Greatsword
    Handaxes (2)
    Healer’s kit
    Javelins (3)
    Mess kit
    Pouch
    Tinderbox
    Torches (5)
    Traveler’s clothing
    Waterskin
    Money (15 gp)

Actions:

    Attack: You can make one of the following attacks (see Rage and Reckless Attack):

        Greatsword: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2d6 + 3 (or +5 if raging) slashing damage.

        Handaxe: Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 1d6 + 3 (or +5 if raging and used in melee) slashing damage.

        Javelin: Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 1d6 + 3 (or +5 if raging and used in melee) piercing damage.

    Bonus Actions:

        Rage: Barbarian feature
    

    '''

    print(playerCharacterInfo)

elif playerCharacter == 3:

    playerSTRENGTH = 10
    playerDEXTERITY = 16
    playerCONSTITUTION = 13
    playerINTELLIGENCE = 16
    playerWISDOM = 12
    playerCHARISMA = 8



    playerCharacterInfo = '''

Race: High Elf

Class: Fighter

“I apologize for cutting off your 
fascinating diatribe with my blade 
in your belly. Small talk was never 
my strong suit.”

Background: Sage

Alignment: Lawful Neutral

Armor Class: 17

Hit Points: 11 (Hit Dice 1d10)

Speed: 30 ft.

Abilities:

    Strength (STR): 10 (0)
    Dexterity (DEX): 16 (+3)
    Constitution (CON): 13 (+1)
    Intelligence (INT): 16 (+3)
    Wisdom (WIS): 12 (+1)
    Charisma (CHA): 8 (-1)

Proficiencies:

    Saving Throws: Strength (+2), Constitution (+3); advantage on saves against being charmed.
    Skills: Arcana (+5), Athletics (+2), History (+5), Insight (+3), Perception (+3), Survival (+3).
    Armor: All, shields.
    Weapons: Simple, martial.
    Senses: Darkvision, Passive Perception 13
    Languages: Common, Dwarvish, Draconic, Elvish, Halfling
    

Background Features:

    Researcher: 
        
        If you do not know a piece of information, you usually know where and from whom that knowledge can be obtained.

    Faction: 
        
        Member of the Lord’s Alliance, a group of allied political powers concerned with mutual security and prosperity.

Personality Traits:

    You use polysyllabic words that convey the impression of great erudition.

Ideal:

    The path to power and self-improvement is through knowledge.

Bond:

    Your life’s work is the Tome of Battle, a treatise related to your theories on combat.

Flaw:

    You speak without really thinking through your words, invariably insulting others.

High Elf Traits:

    Fey Ancestry: 
    
        You have advantage on saving throws against being charmed, and magic can’t put you to sleep.
    
    Darkvision: 
    
        You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.
    
    Trance: 
    
        You don’t require sleep. Instead, you meditate deeply, semiconscious, for 4 hours a day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.
    
    Cantrip: 
    
        You know the true strike cantrip.

Fighter Features:

    Fighting Style: 
    
        Dueling: 
        
            When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

        Second Wind: 
        
            On your turn, you can use a bonus action to regain 1d10 + 1 hit points. Once you use this feature, you must finish a short or long rest before you can use it again.

Equipment:

    Rapier
    Studded leather
    Dart (20)
    Shield
    Scholar’s pack
    Fishing tackle
    Book on fighting techniques
    Spellbook
    Money (64 gp, 8 sp)

Actions:

    Attack: You can attack when you take this action, using the following:

        Rapier: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1d8 + 5 piercing damage.

        Dart: Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 1d4 + 3 piercing damage.

    True Strike (Cantrip): 
    
        Range 30 ft., concentration up to 1 round. Gain advantage on your next attack against the target before the end of your next turn.

    Options:

        Fey Ancestry. Elf Trait.

        Trance. Elf Trait.


    '''

    print(playerCharacterInfo)

elif playerCharacter == 4:

    playerSTRENGTH = 8
    playerDEXTERITY = 17
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 10
    playerWISDOM = 14
    playerCHARISMA = 12



    playerCharacterInfo = '''



    '''

elif playerCharacter == 5:

    playerSTRENGTH = 8
    playerDEXTERITY = 16
    playerCONSTITUTION = 10
    playerINTELLIGENCE = 13
    playerWISDOM = 12
    playerCHARISMA = 16



    playerCharacterInfo = '''



    '''

elif playerCharacter == 6:

    playerSTRENGTH = 8
    playerDEXTERITY = 16
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 12
    playerWISDOM = 10
    playerCHARISMA = 16

    playerCharacterInfo = '''



    '''

elif playerCharacter == 7:

    playerSTRENGTH = 10
    playerDEXTERITY = 17
    playerCONSTITUTION = 13
    playerINTELLIGENCE = 14
    playerWISDOM = 12
    playerCHARISMA = 9

    playerCharacterInfo = '''


    
'''

elif playerCharacter == 8:

    playerSTRENGTH = 12
    playerDEXTERITY = 16
    playerCONSTITUTION = 13
    playerINTELLIGENCE = 10
    playerWISDOM = 16
    playerCHARISMA = 8

    playerCharacterInfo = '''



'''

elif playerCharacter == 9:

    playerSTRENGTH = 10
    playerDEXTERITY = 13
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 10
    playerWISDOM = 12
    playerCHARISMA = 16

    playerCharacterInfo = '''

    

'''

elif playerCharacter == 10:

    playerSTRENGTH = 10
    playerDEXTERITY = 16
    playerCONSTITUTION = 12
    playerINTELLIGENCE = 16
    playerWISDOM = 13
    playerCHARISMA = 8

    playerCharacterInfo = '''



'''

elif playerCharacter == 11:

    playerSTRENGTH = 9
    playerDEXTERITY = 15
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 11
    playerWISDOM = 16
    playerCHARISMA = 13

    playerCharacterInfo = '''



'''

elif playerCharacter == 12:

    playerSTRENGTH = 8
    playerDEXTERITY = 15
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 13
    playerWISDOM = 10
    playerCHARISMA = 16

    playerCharacterInfo = '''



'''

elif playerCharacter == 13:

    playerSTRENGTH = 14
    playerDEXTERITY = 8
    playerCONSTITUTION = 15
    playerINTELLIGENCE = 10
    playerWISDOM = 16
    playerCHARISMA = 12

    playerCharacterInfo = '''



'''

elif playerCharacter == 14:

    playerSTRENGTH = 16
    playerDEXTERITY = 10
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 8
    playerWISDOM = 12
    playerCHARISMA = 15

    playerCharacterInfo = '''



'''

elif playerCharacter == 15:

    playerSTRENGTH = 16
    playerDEXTERITY = 8
    playerCONSTITUTION = 13
    playerINTELLIGENCE = 10
    playerWISDOM = 16
    playerCHARISMA = 12

    playerCharacterInfo = '''



'''

elif playerCharacter == 16:

    playerSTRENGTH = 16
    playerDEXTERITY = 9
    playerCONSTITUTION = 14
    playerINTELLIGENCE = 11
    playerWISDOM = 13
    playerCHARISMA = 15

    playerCharacterInfo = '''



'''

else:

    pass




#Translating stats into modifiers which helps with character generation.


def playerStrCheck():


    if 1 <= playerSTRENGTH <= 19:

        playerStrMod = (playerSTRENGTH - 10) // 2
    else:

        playerStrMod = 5


    return playerStrMod


def playerDexCheck():

    if 1 <= playerDEXTERITY <= 19:

        playerDexMod = (playerDEXTERITY - 10) // 2

    else:

        playerDexMod = 5

    return playerDexMod


def playerConCheck():

    if 1 <= playerCONSTITUTION <= 19:

        playerConMod = (playerCONSTITUTION - 10) // 2

    else:

        playerConMod = 5

    return playerConMod

def playerIntCheck():


    if 1 <= playerINTELLIGENCE <= 19:

        playerIntMod = (playerINTELLIGENCE - 10) // 2

    else:

        playerIntMod = 5

    return playerIntMod


def playerWisCheck():


    if 1 <= playerWISDOM <= 19:

        playerWisMod = (playerWISDOM - 10) // 2

    else:

        playerWisMod = 5

    return playerWisMod

def playerChaCheck():


    if 1 <= playerCHARISMA <= 19:

        playerChaMod = (playerCHARISMA - 10) // 2

    else:

        playerChaMod = 5

    return playerChaMod






def strCheck():

    if 1 <= STRENGTH <= 29:

        strMod = (STRENGTH - 10) // 2

    else:

        strMod = 10


    return strMod


def dexCheck():

    if 1 <= DEXTERITY <= 29:

        dexMod = (DEXTERITY - 10) // 2

    else:

        dexMod = 10


    return dexMod


def conCheck():

    if 1 <= CONSTITUTION <= 29:

        conMod = (CONSTITUTION - 10) // 2

    else:

        conMod = 10


    return conMod


def intCheck():

    if 1 <= INTELLIGENCE <= 29:

        intMod = (INTELLIGENCE - 10) // 2

    else:

        intMod = 10


    return intMod


def wisCheck():

    if 1 <= WISDOM <= 29:

        wisMod = (WISDOM - 10) // 2

    else:

        wisMod = 10


    return wisMod


def chaCheck():

    if 1 <= CHARISMA <= 29:

        chaMod = (CHARISMA - 10) // 2

    else:

        chaMod = 10


    return chaMod





playerStrModNum = playerStrCheck()
playerDexModNum = playerDexCheck()
playerConModNum = playerConCheck()
playerIntModNum = playerIntCheck()
playerWisModNum = playerWisCheck()
playerChaModNum = playerChaCheck()


# How the player should control their character:
# Have the player write several statements as a paragraph for an input where the statements are seperated by /'s and then use an algorithm to try and discern what the player is asking of the system,
# Explain this lore wise by having the other people in the group going over a tutorial and then eventually as the game goes on give more freedom to the player to control the other party members (the
# warrior, the scoundrel, the mage, and/or the healer)
# This adds uniqueness and complexity to the game to allow me to display my coding skills :)

# To use the character sheets or to have the player make a character..... what to do






print("\n\nDeveloper / Dungeon Master Stuff (I.e. Various modifiers):\n\n", playerStrModNum, playerDexModNum, playerConModNum, playerIntModNum, playerWisModNum, playerChaModNum)
print("“Dungeons and Dragons: Online is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. Portions of the materials used are property of Wizards of the Coast. ©Wizards of the Coast LLC.”")
