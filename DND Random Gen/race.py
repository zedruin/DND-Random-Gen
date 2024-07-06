race_subrace_choice = []
race_speed = []
race_languages = []
race_darkvision = []
race_ability_score = []
race_age = []
race_alignment = []
race_resistance = []
race_spells = []
race_special = []

def aasimar(subrace):
    global race_subrace_choice, race_speed, race_languages, race_darkvision, race_ability_score, race_age, race_alignment, race_resistance, race_spells, race_special
    subrace = race_subrace_choice
    race_ability_score = ["Charisma +2"]
    race_age = ["Up to 160 years"]
    race_alignment = ["Typically Good, Outcasts are often Neutral or Evil"]
    race_speed = [30]
    race_darkvision = ["60 ft."]
    race_resistance = ["Necrotic", "Radiant"]
    race_languages = ["Common", "Celestial"]
    race_spells = ["Light"]
    race_special = ["Healing Hands"]
    subrace = ""
    
    if subrace == "Protector":
        race_ability_score.append("Wisdom +1")
    elif subrace == "Scourge":
        race_ability_score.append("Constitution +1")
    elif subrace == "Fallen":
        race_ability_score.append("Strength +1")

    return race_ability_score, race_age, race_alignment, race_speed, race_darkvision, race_resistance, race_languages, race_spells

