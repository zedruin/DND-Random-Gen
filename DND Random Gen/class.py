class_hit_dice = []
class_hit_points = []
class_armor = []
class_weapons = []
class_tools = []
class_saving_throws = []
class_skills = []
class_skills_2 = []
class_equipment_weapon = []
class_equipment_weapon_2 = []
class_equipment_weapon_3 = []
class_equipment_armor = []
class_equipment_pack = []
class_equipment_gold = []
class_optional = []
class_special = []
class_special_2 = []
class_spellcasting_cantrip = []
class_spellcasting_first = []
class_spellcasting_ability = []
class_spellcasting_dc = []
class_spellcasting_attack = []
class_profeciency = [2]
class_strength = []
class_dexterity = []
class_constitution = []
class_intelligence = []
class_wisdom = []
class_charisma = []
class_skill_modifier = []
class_strength_modifier = []
class_dexterity_modifier = []
class_constitution_modifier = []
class_intelligence_modifier = []
class_wisdom_modifier = []
class_charisma_modifier = []

def make_global():
    local_vars = {
        "class_hit_dice": class_hit_dice,
        "class_hit_points": class_hit_points,
        "class_armor": class_armor,
        "class_weapons": class_weapons,
        "class_tools": class_tools,
        "class_saving_throws": class_saving_throws,
        "class_skills": class_skills,
        "class_skills_2": class_skills_2,
        "class_equipment_weapon": class_equipment_weapon,
        "class_equipment_weapon_2": class_equipment_weapon_2,
        "class_equipment_weapon_3": class_equipment_weapon_3,
        "class_equipment_armor": class_equipment_armor,
        "class_equipment_pack": class_equipment_pack,
        "class_equipment_gold": class_equipment_gold,
        "class_optional": class_optional,
        "class_special": class_special,
        "class_special_2": class_special_2,
        "class_spellcasting_cantrip": class_spellcasting_cantrip,
        "class_spellcasting_first": class_spellcasting_first,
        "class_spellcasting_ability": class_spellcasting_ability,
        "class_spellcasting_dc": class_spellcasting_dc,
        "class_spellcasting_attack": class_spellcasting_attack,
        "class_profeciency": class_profeciency,
        "class_strength": class_strength,
        "class_strength_modifier": class_strength_modifier,
        "class_dexterity": class_dexterity,
        "class_dexterity_modifier": class_dexterity_modifier,
        "class_constitution": class_constitution,
        "class_constitution_modifier": class_constitution,
        "class_intelligence": class_intelligence,
        "class_intelligence_modifier": class_intelligence_modifier,
        "class_wisdom": class_wisdom,
        "class_wisdom_modifier": class_wisdom_modifier,
        "class_charisma": class_charisma,
        "class_charisma_modifier": class_charisma_modifier,
    }
    for name, value in local_vars.items():
        globals()[name] = value

def artificer():
    class_constitution_modifier = 5
    make_global()
    class_hit_dice = 8
    class_hit_points = class_hit_dice + class_constitution_modifier
    #class_armor.append("Light", "Medium", "Shields")
    class_weapons.append("Simple")
    #class_tools.append("Thieve's Tool", "Tinker's Tool", "One type of Artisan's Tool of your choice")
    #class_saving_throws.append("Constitution", "Intelligence")
#    class_skills.append("Arcana", "History", "Investigation", "Medicine", "Nature", "Perception", "Sleight of Hand")
 #   class_skills_2.append("Arcana", "History", "Investigation", "Medicine", "Nature", "Perception", "Sleight of Hand")
    class_equipment_weapon.append("Simple")
    class_equipment_weapon_2.append("Simple")
    class_equipment_weapon_3.append("Light Crossbow")
  #  class_equipment_armor.append("Studded Leather", "Scale Mail")
   # class_equipment_pack.append("Thieves' Tool", "Dungeoneer's Pack")
    class_equipment_gold.append("5d4 x 10")
    class_optional.append("Firearm Proficiency")
    class_special.append("Magical Tinkering")
    class_spellcasting_ability.append("Intelligence")
    return class_hit_points

print(artificer())



