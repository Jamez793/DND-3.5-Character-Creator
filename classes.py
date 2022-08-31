# classes divided into 3 strings for neat viewing in text based builder
classes1 = "1: Barbarian    5: Fighter    9: Rogue "
classes2 = "2: Bard         6: Monk       10: Sorcerer "
classes3 = "3: Cleric       7: Paladin    11: Wizard "
classes4 = "4: Druid        8: Ranger"
chosen_class = ""

# v have player confirm or deny class choice v


def confirm_class(choice):
    global chosen_class
    while True:
        confirm = input(f"\nIs {choice} the class you want to play? Y/N")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            print(f"\nYou have chosen to play {choice}")
            chosen_class = choice
            break
        elif confirm.lower() == "n" or confirm.lower() == "no":
            break
        else:
            print("\nInvalid input please type y or n to confirm or deny choice.")

# v have player choose class, give information about chosen class, and move to choice confirmation. v


def choose_class():
    global chosen_class
    while True:
        give_info = input(
            f"\nPlease choose which of the following classes to learn about:\n{classes1}\n{classes2}\n{classes3}\n{classes4}\nType name or number of choice: ")

        if give_info == "1" or give_info.lower() == "barbarian":
            print("\nplaceholder teaching about class")
            confirm_class("barbarian")
        elif give_info == "2" or give_info.lower() == "bard":
            print("\nplaceholder teaching about class")
            confirm_class("bard")
        elif give_info == "3" or give_info.lower() == "cleric":
            print("\nplaceholder teaching about class")
            confirm_class("cleric")
        elif give_info == "4" or give_info.lower() == "druid":
            print("\nplaceholder teaching about class")
            confirm_class("druid")
        elif give_info == "5" or give_info.lower() == "fighter":
            print("\nplaceholder teaching about class")
            confirm_class("fighter")
        elif give_info == "6" or give_info.lower() == "monk":
            print("\nplaceholder teaching about class")
            confirm_class("monk")
        elif give_info == "7" or give_info.lower() == "paladin":
            print("\nplaceholder teaching about class")
            confirm_class("paladin")
        elif give_info == "8" or give_info.lower() == "ranger":
            print("\nplaceholder teaching about class")
            confirm_class("ranger")
        elif give_info == "9" or give_info.lower() == "rogue":
            print("\nplaceholder teaching about class")
            confirm_class("rogue")
        elif give_info == "10" or give_info.lower() == "sorcerer":
            print("\nplaceholder teaching about class")
            confirm_class("sorcerer")
        elif give_info == "11" or give_info.lower() == "wizard":
            print("\nplaceholder teaching about class")
            confirm_class("wizard")
        else:
            print(
                "\nInvalid input. Please check your spelling or type the number of your choice.")
# v move to skills.py if choice above confirmed, got back to class selection if choice above denied. v
        if not chosen_class == "":
            return chosen_class
        else:
            continue
