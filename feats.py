import races
import skills
import abilities
import classes


class Feat:
    def __init__(self, name):
        self.name = name
        self.bonus = "placeholder"
        self.desc = "placeholder"
        self.met_prereq = True
        self.active = False
        self.parent = None
        self.ftr_bns = False


class Subfeat(Feat):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent


def linear_search_skills(skills, target):
    for x in skills:
        if x.name == target:
            return x
    print("Invalid input, please check your spelling and that the intended skill is in either of the skills lists.")
    return None

# v functionality for player to learn about and select feats. v


def choose_feats():
    race = races.race
    player_class = classes.chosen_class
    stats = abilities.abilities
    player_skills = skills.skills
    feats = ("acrobatic", "agile", "alertness", "animal_affinity", "light_armor_proficiency", "athletic", "augment_summoning", "blind_fight", "combat_casting", "combat_expertise", "combat_reflexes", "deceitful", "deft_hands", "diligent", "dodge", "endurance", "eschew_materials", "exotic_weapon_proficiency", "extra_turning", "great_fortitude", "improved_counterspell", "improved_initiative", "improved_turning", "improved_unarmed_strike", "investigator", "iron_Will",
             "lightning_reflexes", "magical_aptitude", "martial_weapon_proficiency", "mounted_combat", "negotiator", "nimble_fingers", "persuasive", "point_blank_shot", "power_attack", "quick_draw", "rapid_reload", "run", "self_sufficient", "shield_proficiency", "simple_weapon_proficiency", "simple_weapon_proficiency", "spell_focus", "spell_mastery", "spell_penetration", "stealthy", "toughness", "track", "two_weapon_fighting", "weapon_finesse", "weapon_focus", "scribe_scroll")
    subfeats = {"medium_armor_proficiency": "light_armor_proficiency", "heavy_armor_proficiency": "medium_armor_proficiency", "improved_disarm": "combat_expertise", "improved_feint": "combat_expertise", "improved_trip": "combat_expertise", "mobility": "dodge", "diehard": "endurance", "improved_grapple": "improved_unarmed_strike", "deflect_arrows": "improved_unarmed_strike", "snatch_arrows": "deflect_arrows", "mounted_archery": "mounted_combat", "ride_by_attack": "mounted_combat", "spirited_charge": "ride_by_attack",
                "trample": "mounted_combat", "far_shot": "point_blank_shot", "precise_shot": "point_blank_shot", "rapid_shot": "point_blank_shot", "cleave": "power_attack", "improved_bull_rush": "power_attack", "improved_overrun": "power_attack", "improved_sunder": "power_attack", "improved_shield_bash": "shield_proficiency", "tower_shield_proficiency": "shield_proficiency", "greater_spell_focus": "spell_focus", "greater_spell_penetration": "spell_penetration", "two_weapon_defense": "two_weapon_fighting"}
    fighter_feats = ("blind_fight", "combat_expertise", "improved_disarm", "improved_feint", "improved_trip", "combat_reflexes",
                     "dodge", "mobility", "exotic_weapon_proficiency", "improved_initiative", "improved_unarmed_strike", "improved_grapple")
    for feat in feats:
        globals()[feat] = Feat(feat)
    for feat, parent in subfeats.items():
        globals()[feat] = Subfeat(feat, globals()[parent])
    feat_points = 1
    if race == "human":
        feat_points += 1
