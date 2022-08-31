import abilities
import classes
import races
# global skills variable for other modules
skills = []

# variables to short-hand class names
bbn = "barbarian"
brd = "bard"
clr = "cleric"
drd = "druid"
ftr = "fighter"
mnk = "monk"
pal = "paladin"
rgr = "ranger"
rog = "rogue"
sor = "sorcerer"
wiz = "wizard"
# variables to determine skill point base
skl_pts_2 = (clr, ftr, pal, sor, wiz)
skl_pts_4 = (bbn, drd, mnk)
skl_pts_6 = (brd, rgr)

# v base class for each skill v


class Skill:
    def __init__(self, name, abl, chr_cls, untrnd, rmr_chk):
        self.name = name
        self.ability = abl
        self.chr_cls = chr_cls
        self.untrnd = untrnd
        self.rmr_chk = rmr_chk
        self.ranks = 0
        self.desc = "placeholder"
        self.modifier = 0
        self.subskill = ""

# v search function when player types a skill to spend points on v


def linear_search_skills(skills, target):
    for x in skills:
        if x.name.lower() == target:
            return x
    print("Invalid input, please check your spelling and that the intended skill is in either of the skills lists.")
    return None


# v build skills and skill list V
def spend_skill_points():
    player_class = classes.chosen_class
    race = races.race
    stats = abilities.abilities
    global skills
    class_skill_names = []
    cc_skill_names = []

    def skl_crt(skill, abl, classes, untrnd, rmrchk):
        globals()[skill] = Skill(skill, abl, classes, untrnd, rmrchk)
        skills.append(globals()[skill])
    skl_crt("Appraise", "int", (brd, rog), True, False)
    skl_crt("Balance", "dex", (brd, mnk, rog), True, True)
    skl_crt("Bluff", "cha", (brd, rog, sor), True, False)
    skl_crt("Climb", "str", (bbn, brd, ftr, mnk, rgr, rog), True, True)
    skl_crt("Concentration", "con",
            (brd, clr, drd, mnk, pal, rgr, sor, wiz), True, False)
    skl_crt("Craft", "int", (), True, False)
    skl_crt("Decipher_Script", "int",
            (brd, rog, wiz), False, False)
    skl_crt("Diplomacy", "cha", (brd, clr,
                                 drd, mnk, pal, rog), True, False)
    skl_crt("Disable_Device", "int", (rog), False, False)
    skl_crt("Disguise", "cha", (brd, rog), True, False)
    skl_crt("Escape_Artist", "dex", (brd, mnk, rog), True, True)
    skl_crt("Forgery", "int", (rog), True, False)
    skl_crt(
        "Gather_Information", "cha", (brd, rog), True, False)
    skl_crt("Handle_Animal", "cha",
            (bbn, drd, ftr, pal, rgr), False, False)
    skl_crt("Heal", "wis", (clr, drd, pal, rgr), True, False)
    skl_crt("Hide", "dex", (brd, mnk, rgr, rog), True, True)
    skl_crt("Intimidate", "cha", (bbn, ftr, rog), True, False)
    skl_crt("Jump", "str", (bbn, brd, ftr, mnk, rgr, rog), True, True)
    skl_crt("Knowledge(Arcana)", "int",
            (brd, clr, mnk, sor, wiz), False, False)
    skl_crt(
        "Knowledge(Dungeoneering)", "int", (brd, rgr, wiz), False, False)
    skl_crt(
        "Knowledge(Geography)", "int", (brd, rgr, wiz), False, False)
    skl_crt("Knowledge(History)",
            "int", (brd, clr, wiz), False, False)
    skl_crt("Knowledge(Local)", "int",
            (brd, rog, wiz), False, False)
    skl_crt("Knowledge(Nature)", "int",
            (brd, drd, rgr, wiz), False, False)
    skl_crt(
        "Knowledge(Nobility and Royalty)", "int", (brd, pal, wiz), False, False)
    skl_crt(
        "Knowledge(Religion)", "int", (brd, clr, mnk, pal, wiz), False, False)
    skl_crt("Knowledge(the Planes)",
            "int", (brd, clr, wiz), False, False)
    skl_crt("Listen", "wis", (bbn, brd, drd,
                              mnk, rgr, rog), True, False)
    skl_crt("Move_Silently", "dex",
            (brd, mnk, rgr, rog), True, True)
    skl_crt("Open_Lock", "dex", (rog), True, False)
    skl_crt("Perform", "cha", (brd, mnk, rog), True, False)
    skl_crt("Profession", "wis", (brd, clr, drd,
                                  mnk, pal, rgr, rog, sor, wiz), False, False)
    skl_crt("Ride", "dex", (bbn, drd, ftr, pal, rgr), True, False)
    skl_crt("Search", "int", (rgr, rog), True, False)
    skl_crt("Sense_Motive", "wis",
            (brd, mnk, pal, rog), True, False)
    skl_crt("Sleight_of_Hand", "dex", (brd, rog), False, True)
    skl_crt("Speak_Language", "none", (brd), False, False)
    skl_crt("Spellcraft", "int",
            (brd, clr, drd, sor, wiz), False, False)
    skl_crt("Spot", "wis", (drd, mnk, rgr, rog), True, False)
    skl_crt("Survival", "wis", (bbn, drd, rgr), True, False)
    skl_crt("Swim", "str", (bbn, brd, drd,
                            ftr, mnk, rgr, rog), True, True)
    skl_crt("Tumble", "dex", (brd, mnk, rog), False, True)
    skl_crt("Use_Magic Device", "cha",
            (brd, rog), False, False)
    skl_crt("Use_Rope", "dex", (rgr, rog), True, False)

    # logic to determine points pool for skill points based on class, race, and intelligence modifier
    if race == "human":
        skill_points = 1
    else:
        skill_points = 0

    if player_class in skl_pts_2:
        skill_points += (2 + stats["int_modifier"])
    elif player_class in skl_pts_4:
        skill_points += (4 + stats["int_modifier"])
    elif player_class in skl_pts_6:
        skill_points += (6 + stats["int_modifier"])
    else:
        skill_points += ((8 + stats["int_modifier"]))

    skill_points *= 4

    for skill in skills:
        if player_class in skill.chr_cls or skill.name == "Craft":
            class_skill_names.append(skill.name)
        else:
            cc_skill_names.append(skill.name)

    craft_subskills = ["alchemy", "armorsmithing", "basketweaving", "bookbinding", "bowmaking", "blacksmithing", "calligraphy", "carpentry", "cobbling",
                       "gemcutting", "leatherworking", "locksmithing", "painting", "pottery", "sculpting", "shipmaking", "stonemasonry", "trapmaking", "weaponsmithing", "weaving"]
    perform_subskills = ["act", "comedy", "dance", "keyboard instruments", "oratory",
                         "percussion instruments", "string instruments", "wind instruments", "sing"]
    profession_subskills = ["apothecary", "boater", "bookkeeper", "brewer", "cook", "driver", "farmer", "fisher", "guide", "herbalist", "herder", "hunter",
                            "innkeeper", "lumberjack", "miller", "miner", "porter", "rancher", "sailor", "scribe", "seige engineer", "stablehand", "tanner", "teamster", "woodcutter"]
    print(f"Your class skills are {class_skill_names} and you have {skill_points} points to spend. if you want to spend points on cross-class skills, they will cost 2 points each. You may not spend more than 4 points in any skill.")
    while skill_points > 0:
        choice = input(f"You currently have {skill_points} skill points to spend.\nFor a list of your class_skills, type 'skill' and press enter.\nFor a list of cross-class skills, type 'ccskill' and press enter.\nPlease type the name of a skill to learn about and spend points in: ")
        if choice.lower() == "skill":
            print(f"your class skills are {class_skill_names}.")
        elif choice.lower() == "ccskill":
            print(f"your cross-class skills are {cc_skill_names}.")
        else:
            while True:
                skill = linear_search_skills(skills, choice.lower())
                if skill == None:
                    break
                elif skill.name in class_skill_names and skill.ranks >= 4 or skill.name in cc_skill_names and skill.ranks >= 2:
                    print(
                        f"You have already spent the maximum number of points in {skill.name}")
                else:
                    print(skill.desc)
                    loop = True
                    while loop == True:
                        if skill.name == "Craft" or skill.name == "Perform" or skill.name == "Profession":
                            subskill = input(
                                f"Please choose a specific aspect of {skill.name} to specialize in. If you need examples, type 'help' and press enter. If you don't want to continue, type 'back' and press enter. (note: this program does not support multiple types of this skill): ")
                            if subskill.lower() == "help":
                                if skill.name == "Craft":
                                    print(
                                        f"Here are some examples for the craft skill: {craft_subskills}")
                                elif skill.name == "Perform":
                                    print(
                                        f"Here are some examples for the craft skill: {perform_subskills}")
                                elif skill.name == "Profession":
                                    print(
                                        f"Here are some examples for the craft skill: {profession_subskills}")
                                else:
                                    print(
                                        "The system encountered an error, returning to skill selection.")
                                    break
                            elif subskill.lower() == "back":
                                break
                            elif skill.name == "Craft" and subskill.lower() in craft_subskills:
                                skill.subskill = subskill.lower()
                                loop = False
                            elif skill.name == "Perform" and subskill.lower() in perform_subskills:
                                skill.subskill = subskill.lower()
                                loop = False
                            elif skill.name == "Profession" and subskill.lower() in profession_subskills:
                                skill.subskill = subskill.lower()
                                loop = False
                            else:
                                while True:
                                    confirm = input(
                                        "You have typed a selection not mentioned in the D&D 3.5 players handbook. If you typed one of the examples, you may check your spelling and try again. Otherwise we will use your input as the subskill. Is what you typed accurate? Type 'y' to continue or 'n' to change your subskill choice.")
                                    if confirm.lower() == "y":
                                        skill.subskill = subskill.lower()
                                        loop = False
                                        break
                                    elif confirm.lower() == "n":
                                        break
                                    else:
                                        print(
                                            "input not recognized. please type y or n.")
                        else:
                            loop = False
                    loop = True
                    while loop == True:
                        if skill.name in class_skill_names:
                            points = input(
                                f"Please type how many points (up to 4) to spend on {skill.name} (type 0 to not spend any skill points): ")
                        else:
                            points = input(
                                f"{skill.name} is a cross-class skill, you may spend 2 points for one rank or 4 points for 2 ranks.\nPlease type how many points (2 or 4) to spend on {skill.name} (type 0 to not spend any skill points): ")
                        try:
                            points = int(points)
                        except ValueError:
                            print(
                                "invalid input, you may only type a whole number without any decimals.")
                        if points < 0 or skill.name in class_skill_names and (points + skill.ranks) > 4:
                            print(
                                f"Invalid Number. You may not type a negative number or spend more than 4 points in total. you have currently have {skill.ranks} ranks in {skill.name}.")
                        elif skill.name in cc_skill_names:
                            if skill.ranks * 2 + points > 4:
                                print(
                                    f"You may not spend more than 4 points total. You have currently spent{int(skill.ranks * 2)} points in {skill.name}")
                            elif points % 2 != 0:
                                print(
                                    "To spend skill points in cross class skills you must spend an even number of points. please choose either 0, 2, or 4 points to spend.")
                            else:
                                skill.ranks += int((points / 2))
                                skill_points -= points
                                loop = False
                        else:
                            skill.ranks += points
                            skill_points -= points
                            loop = False
                break
    for skill in skills:
        if skill.ability == "str":
            skill.modifier += (stats["str_modifier"])
        elif skill.ability == "dex":
            skill.modifier += (stats["dex_modifier"])
        elif skill.ability == "con":
            skill.modifier += (stats["con_modifier"])
        elif skill.ability == "int":
            skill.modifier += (stats["int_modifier"])
        elif skill.ability == "wis":
            skill.modifier += (stats["wis_modifier"])
        elif skill.ability == "cha":
            skill.modifier += (stats["cha_modifier"])
        skill.modifier += skill.ranks
        if race == "elf":
            if skill.name == "Listen" or skill.name == "Search" or skill.name == "Spot":
                skill.modifier += 2
        if race == "gnome":
            if skill.name == "craft" and skill.subskill == "alchemy" or skill.name == "listen":
                skill.modifier += 2
        if race == "half-elf":
            if skill.name == "Listen" or skill.name == "Search" or skill.name == "Spot":
                skill.modifier += 1
            if skill.name == "Diplomacy" or skill.name == "Gather Information":
                skill.modifier += 2
        if race == "half-elf":
            if skill.name == "Listen" or skill.name == "Climb" or skill.name == "Jump" or skill.name == "Move Silently":
                skill.modifier += 2
    return race, player_class, stats, skills
