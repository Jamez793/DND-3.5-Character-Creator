import random
import races

# dictionary of scores and modifiers to be passed to skills.py and on.
abilities = {"str_score": 0, "str_modifier": 0, "dex_score": 0, "dex_modifier": 0, "con_score": 0, "con_modifier": 0,
             "int_score": 0, "int_modifier": 0, "wis_score": 0, "wis_modifier": 0, "cha_score": 0, "cha_modifier": 0}

# empty list for score rolls
rolls = []
remaining_rolls = []
# dictionary to build the "+" prefix when listing score modifiers that are positive
stat_prefix = {"str_modifier": "", "dex_modifier": "", "con_modifier": "",
               "int_modifier": "", "wis_modifier": "", "cha_modifier": ""}


def choose_method():
    global abilities
    print("in Dungeons and Dragons, you can either roll random ability scores or you can follow what is called a 'points buy' system.\n\nIf you choose to roll your scores, this system will roll 4d6(dropping the lowest of the 4) 7 times(dropping the lowest of those 7). from there, you will assign each score to the ability of your choice.\n\nIf you decide to follow the points buy system, your abilities will start at 8 and you will have a set amount of points to spend to increase each ability to higher levels.")
    while True:
        choice = input(
            "1) Roll Scores\n2) Points Buy\nPlease choose which way to set your abilities by typing the corresponding number and pressing enter: ")
        if choice == "1":
            forward = apply_scores()
            return forward
        elif choice == "2":
            forward = points_buy()
            return forward
        else:
            print("Invalid response. please type either 1 or 2 and press enter")


def points_buy():
    scores = {"1": 8, "2": 8, "3": 8, "4": 8, "5": 8, "6": 8}
    names = {"1": "strength", "2": "Dexterity", "3": "Constitution",
             "4": "Intelligence", "5": "Wisdom", "6": "Charisma"}
    print("In points-buy, by default each score is set to 8 and you are given 25 points to spend among the 6 stats: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma\n(NOTE: your ability scores are modified by your chosen race after you finish spending points).\n\nthe first 6 points in any ability cost 1 point each, after which each ability point will cost 2 points.")
    check_default = input("Do you want to use the default settings or did your DM give you a custom amount of points to use?(note, this system does not support modified points costs other than what was stated above)\n1) default\n2) custom\nType your choice and press enter: ")
    if check_default == "1" or check_default.lower() == "default":
        points_pool = 25
    elif check_default == "2" or check_default.lower() == "custom":
        while True:
            points_pool = input(
                "please type the number of points you are allowed to use: ")
            try:
                points_pool = int(points_pool)
            except ValueError:
                print(
                    "You may only type a numerical value without decimals. letters and special characters will not work.")
                continue
            if points_pool > 30 and (points_pool % 2) > 0:
                print("Either your input was invalid or your DM is trolling you, with these points you will be stuck with a remainder of one point to spend. please enter a different number.")
            else:
                break

    while points_pool > 0:
        print(f"\n you currently have {points_pool} points left to spend.")
        skill_spend = input(
            f'\nCurrent Scores:\n1: Strength: ({scores["1"]})        2: Dexterity: ({scores["2"]})    3: Constitution: ({scores["3"]})\n4: Intelligence: ({scores["4"]})    5: Wisdom: ({scores["5"]})       6: Charisma: ({scores["6"]})\nType the corresponding number of an ability to spend points on and press enter: ')
        if skill_spend == "1" or skill_spend == "2" or skill_spend == "3" or skill_spend == "4" or skill_spend == "5" or skill_spend == "6":
            while True:
                spend = input(
                    f"\ntype the number of points you want to put into {names[skill_spend]} and press enter: ")
                try:
                    spend = int(spend)
                except ValueError:
                    print("you may only type round numbers without decimals.")
                    continue
                if spend > points_pool:
                    print(f"you do not have enough points.")
                else:
                    break
            if scores[skill_spend] < 14:
                if spend <= (14 - scores[skill_spend]):
                    scores[skill_spend] += spend
                    points_pool -= spend
                else:
                    temp = (14 - scores[skill_spend])
                    scores[skill_spend] += temp
                    spend -= temp
                    if (spend % 2) == 0:
                        scores[skill_spend] += (int(spend / 2))
                        points_pool -= spend
                    else:
                        print("you chose to spend a number of points that would have resulted in your score having a half point, as such we have capped it off at 14 for now.\nYou can spend more points on this ability as long as you spend an even number of points.")
                        points_pool -= temp
            else:
                if (spend % 2) == 0:
                    scores[skill_spend] += (int(spend / 2))
                    points_pool -= spend
                else:
                    print("you chose to spend a number of points that would have resulted in your score having a half point, as such we can not spend those points on this ability.\nYou can spend more points on this ability as long as you spend an even number of points.")
        else:
            print("\nInvalid input.")
            continue
    abilities["str_score"] = scores["1"]
    abilities["dex_score"] = scores["2"]
    abilities["con_score"] = scores["3"]
    abilities["int_score"] = scores["4"]
    abilities["wis_score"] = scores["5"]
    abilities["cha_score"] = scores["6"]
    build_scores()
    calc_all()
    show_scores()
    return abilities


def calc_all():
    calc_modifier(abilities, "str_score", "str_modifier")
    calc_modifier(abilities, "dex_score", "dex_modifier")
    calc_modifier(abilities, "con_score", "con_modifier")
    calc_modifier(abilities, "int_score", "int_modifier")
    calc_modifier(abilities, "wis_score", "wis_modifier")
    calc_modifier(abilities, "cha_score", "cha_modifier")

    # v rolls 4d6 and drops the lowest roll 7 times dropping the lowest of those 7 values v


def roll_score():
    b = 0
    while b < 7:
        ability_roll = []
        i = 0
        while i < 4:
            i += 1
            ability_roll.append(random.randint(1, 6))
        ability_roll.remove(min(ability_roll))
        ability_calc = ability_roll[0] + ability_roll[1] + ability_roll[2]
        rolls.append(ability_calc)
        remaining_rolls.append(ability_calc)
        b += 1
    rolls.remove(min(rolls))
    remaining_rolls.remove(min(remaining_rolls))
    return rolls

# v Calculate ability modifier based on score applied v


def calc_modifier(ability, s, m):
    # edited ability score modifier to be an integer for compatibility in skills.py
    if ability[s] < 10:
        ability[m] = int(((ability[s] - 10) / 2)) - 1
    else:
        ability[m] = (int((ability[s] - 10) / 2))
        stat_prefix[m] = "+"


# v Assign each of the 6 rolled scores to chosen abilities and show results. v


def apply_scores():
    def remove_sel():
        del available_selection[choice]
        del remaining_rolls[0]
    print(f"your rolled scores are {roll_score()}")
    available_selection = {"1": "Strength", "2": "Dexterity",
                           "3": "Constitution", "4": "Intelligence", "5": "Wisdom", "6": "Charisma"}
    for roll in rolls:
        while True:
            print(
                f"\nremaining rolls: {remaining_rolls}\navailable abilities: {available_selection}")
            choice = input(
                f"\n\nplease type the corresponding number of the ability to assign {roll} to: ")
            if choice == "1" and abilities["str_score"] == 0:
                abilities["str_score"] = roll
                remove_sel()
                break
            elif choice == "2" and abilities["dex_score"] == 0:
                abilities["dex_score"] = roll
                remove_sel()
                break
            elif choice == "3" and abilities["con_score"] == 0:
                abilities["con_score"] = roll
                remove_sel()
                break
            elif choice == "4" and abilities["int_score"] == 0:
                remove_sel()
                abilities["int_score"] = roll
                break
            elif choice == "5" and abilities["wis_score"] == 0:
                abilities["wis_score"] = roll
                remove_sel()
                break
            elif choice == "6" and abilities["cha_score"] == 0:
                abilities["cha_score"] = roll
                remove_sel()
                break
            else:
                print(
                    "Either your input was invalid or that option has already been assigned a value.")
    build_scores()
    calc_all()
    show_scores()
    return abilities


def build_scores():
    race = races.race
    if race == "half-orc":
        abilities["str_score"] += 2
    if race == "halfling" or race == "gnome":
        abilities["str_score"] -= 2
    if race == "elf" or race == "halfling":
        abilities["dex_score"] += 2
    if race == "dwarf" or race == "gnome":
        abilities["con_score"] += 2
    if race == "elf":
        abilities["con_score"] -= 2
    if race == "half-orc":
        abilities["int_score"] -= 2
    if race == "dwarf" or race == "half-orc":
        abilities["cha_score"] -= 2


def show_scores():
    done = input(
        f'Great! please copy down your ability scores as shown!\n\nStrength: {abilities["str_score"]}  Modifier: {stat_prefix["str_modifier"]}{abilities["str_modifier"]}\nDexterity: {abilities["dex_score"]}  Modifier: {stat_prefix["dex_modifier"]}{abilities["dex_modifier"]}\nConstitution: {abilities["con_score"]}  Modifier: {stat_prefix["con_modifier"]}{abilities["con_modifier"]}\nIntelligence: {abilities["int_score"]}  Modifier: {stat_prefix["int_modifier"]}{abilities["int_modifier"]}\nWisdom: {abilities["wis_score"]}  Modifier: {stat_prefix["wis_modifier"]}{abilities["wis_modifier"]}\nCharisma: {abilities["cha_score"]}  Modifier: {stat_prefix["cha_modifier"]}{abilities["cha_modifier"]}\n\nPress enter to continue')
    if done == "":
        return abilities
    else:
        print("\nYou didn't need to type anything.")
