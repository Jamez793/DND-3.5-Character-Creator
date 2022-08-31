# Base file where character creation starts
race = ""

# confirm_race is to confirm player race selection


def confirm_race(choice):
    global race
    while True:
        select = input(f"\n Is {choice} the Race you wish to choose? Y/N: ")
        if select.lower() == "y" or select.lower() == "yes":
            race = choice
            break
        elif select.lower() == "n" or select.lower() == "no":
            break
        else:
            print("\nInvalid input. Please type y or n to confirm or deny your choice.")

# give_race is to have player select a race which is then detailed with traits for the player to understand


def give_race():
    global race
    # Race choices spaced to look nice along 3 lines
    choices = "1: Human       2: Dwarf       3: Elf\n4: Gnome       5: Half-Elf\n6: Half-Orc    7: Halfling"
    # loop to bring player back to selection if they decide against first or subsequent choices
    while race == "":
        start = input(
            f"\nPlease select one of the following Races:\n{choices}\ntype the name or number of your choice: ")
        # if logic to give race information based on choice.
        if start.lower() == "human" or start == "1":
            print("\nThe shortest lived race of playable character, Humans reach adulthood at 15 and rarely live more than a century.")
            print("Being short lived, they are the most adaptable of the Races and are a good fit for just about any class.")
            print("Traits:\n+1 feat and +4 skill points at creation.\nSpeed: 30 ft\n+1 skill point at every level.\nLanguages: Common\nBonus Languages: Any non-secret language (e.g. Druidic)")
            confirm_race("human")
        elif start.lower() == "dwarf" or start == "2":
            print("Shorter and stouter than humans, Dwarves are burly underground citizens, considered adults at age 40, and can live to be more than 400 years old.")
            print("Given their thick structure, Dwarves make good tanks. they are best played as fighters, but can usually also make decent wizards, druids, and clerics.")
            print("Traits:\n+2 constitution and -2 charisma\nSpeed: 20 ft, but they are not slowed by armor or load like other races.\nDarkvision: 60 ft\n+2 racial bonus on noticing unusual stonework\ndwarven waraxes and dwarven urgoshes are considered martial weapons to dwarves\n+4 ability checks to resist bull rushing or tripping when standing firmly on the ground\n+2 racial bonus on saving throws against poison, spells, or spell-like abilities.\n+2 racial bonus on appraise or craft checks related to stone or metal.\n+4 dodge bonus to armor class against giant type (lost if dex bonus is also lost)\nautomatic languages: dwarven, common\nbonus languages: Giant, Gnome, Goblin, Orc, Terran, and undercommon")
            confirm_race("dwarf")
        elif start.lower() == "elf" or start == "3":
            print("slightly shorter than humans and slim, elves carry a grace brought by their long lives in tune with nature. They're considered adults around 110 years and can live past 700.")
            print("Given their natural dexterity and sense of the world around them, elves are best suited as rangers, druids, and wizards. But they can make excellent long range fighters.")
            print("Traits:\n+2 Dexterity and -2 Constitution\nSpeed: 30 ft\nImmune to magic sleep effects and +2 racialt bonus to saves against enchantment slepps and effects.\nLow-light-vision: doule seeing distance in poor illumination.\nRatial Proficiency in Longsword, Rapier, and all longbows and short bows.\n+2 bonus on listen search and spot checks (Elves are entitled to search checks for hidden doors within 5 ft of them).\nAutomatic languages: Common, Elven.\nBonus Languages: Draconic, Gnoll, Gnome, Gobline, Orc, Sylvan")
            confirm_race("elf")
        elif start.lower() == "gnome" or start == "4":
            print("A bit shorter than dwarves and slim as elves, gnomes are pranksters and tinkerers with inquisitive minds. They reach adulthood around 40 and live around 350-500 years.")
            print("Given their nature and shared fondness of nature itself with elves, gnomes are best suited as bards, druids, and wizards.")
            print("Traits:\n+2 Constitution and -2 strength.\nSmall:+1 to AC and attacks against medium characters, but smaller (weaker) weapons and lower carrying capacity.\nSpeed: 20 ft.\nlow-light-vision: 2x sight distance in poor lighting.\nGnome hooked hammers are considered martial weapons for gnomes.\n+2 bonus on saves against illusions, listen checks, and craft(alchemy) checks.\n+1 racial bonus on attack rolls against kobolds and goblinoids.\n+1 to saving dc on illusions cast by gnomes.\nAutomatic Languages: Common, Gnome.\nBonus Languages: Draconic")
            confirm_race("gnome")
        elif start.lower() == "half-elf" or start == "5":
            print("\nplaceholder for race introduction")
            print("placeholder for race lifespan")
            print("placeholder for racial traits")
            confirm_race("half-elf")
        elif start.lower() == "half-orc" or start == "6":
            print("\nplaceholder for race introduction")
            print("placeholder for race lifespan")
            print("placeholder for racial traits")
            confirm_race("half-orc")
        elif start.lower() == "halfling" or start == "7":
            print("\nplaceholder for race introduction")
            print("placeholder for race lifespan")
            print("placeholder for racial traits")
            confirm_race("halfling")
        else:
            print(
                "\ninvalid input. please check your spelling or type the corresponding number for a race.")

    return race
