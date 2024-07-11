import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkhtmlview import HTMLLabel
import requests
import webbrowser

# Races
races = ["Aasimar", "Animal Hybrid", "Birdfolk", "Bugbear", "Centaur", "Changeling", "Dhampir", "Dragonborn", "Dreamtouched", "Dwarf", "Elephantine", "Elf", "Fairy", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Half-Elf", "Half-Orc", "Halfling", "Harefolk", "Hobgoblin", "Human", "Kenku", "Kobold", "Leonine", "Lizardfolk", "Minotaur", "Orc", "Owlkin", "Satyr", "Shifter", "Tabaxi", "Tiefling", "Triton", "Turtle", "Violetken", "Warforged"]

race_bonus = {
    "Aasimar": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Animal Hybrid": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Birdfolk": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Bugbear": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Centaur": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Changeling": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Dhampir": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Dragonborn": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Dreamtouched": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Dwarf": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Elephantine": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Elf": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Fairy": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Firbolg": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Genasi": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Gith": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Gnome": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Goblin": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Goliath": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Half-Elf": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Half-Orc": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Halfling": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Harefolk": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Hobgoblin": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Human": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Kenku": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Kobold": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Leonine": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Lizardfolk": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Minotaur": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Orc": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Owlkin": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Satyr": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Shifter": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Tabaxi": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Tiefling": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Triton": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Turtle": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Violetken": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    "Warforged": {
        "Strength":     2,
        "Dexterity":    0,
        "Constitution": 1,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    },
}

# Sub-Races
sub_race = {
    "Aasimar": ["Protector", "Scourge", "Fallen"],
    "Animal Hybrid": ["", ""],
    "Birdfolk": ["", ""],
    "Bugbear": ["", ""],
    "Centaur": ["", ""],
    "Changeling": ["", ""],
    "Dhampir": ["", ""],
    "Dragonborn": ["Chromatic", "Gem", "Metallic"],
    "Dreamtouched": ["", ""],
    "Dwarf": ["Hill Dwarf", "Mountain Dwarf", ],
    "Elephantine": ["", ""],
    "Elf": ["Dark Elf", "High Elf", "Wood Elf", "Pallid Elf"],
    "Fairy": ["", ""],
    "Firbolg": ["", ""],
    "Genasi": ["Air", "Earth", "Fire", "Water"],
    "Gith":["", ""],
    "Gnome": ["Forest", "Rock"],
    "Goblin": ["", ""],
    "Goliath": ["", ""],
    "Half-Elf": ["", ""],
    "Half-Orc": ["", ""],
    "Halfling": ["Lightfoot", "Stout", "Ghostwise", "Lotusden"],
    "Harefolk": ["", ""],
    "Hobgoblin": ["", ""],
    "Human": ["", ""],
    "Kenku": ["", ""],
    "Kobold": ["", ""],
    "Leonine": ["", ""],
    "Lizardfolk": ["", ""],
    "Minotaur": ["", ""],
    "Orc": ["", ""],
    "Owlkin": ["", ""],
    "Satyr": ["", ""],
    "Shifter": ["", ""],
    "Tabaxi": ["", ""],
    "Tiefling": ["Asmodeus", "Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel", "Variant", "Abyssal"],
    "Triton": ["", ""],
    "Turtle": ["", ""],
    "Violetken": ["", ""],
    "Warforged": ["", ""],
}
# Classes
classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
class_skills = {
    "Artificer": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": "",
        "Stealth": None,
        # Int
        "Arcana": "",
        "History": "",
        "Investigation": "",
        "Nature": "",
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": "",
        "Perception": "",
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Barbarian": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Bard": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Cleric": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Druid": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Fighter": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Monk": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Paladin": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Ranger": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Rogue": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Sorcerer": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Warlock": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }, 
    "Wizard": {
        # Str
        "Athletics": None,
        # Dex
        "Acrobatics": None,
        "Sleight of Hand": None,
        "Stealth": None,
        # Int
        "Arcana": None,
        "History": None,
        "Investigation": None,
        "Nature": None,
        "Religion": None,
        # Wis
        "Animal Handeling": None, 
        "Insight": None,
        "Medicine": None,
        "Perception": None,
        "Survival": None,
        # Cha
        "Deception": None,
        "Intimidation": None,
        "Performance": None,
        "Persuasion": None,
    }
}
hit_dice = {
    "Artificer": 8, 
    "Barbarian": 12, 
    "Bard": 12, 
    "Cleric": 8, 
    "Druid": 8, 
    "Fighter": 10, 
    "Monk": 8, 
    "Paladin": 10, 
    "Ranger": 10, 
    "Rogue": 8, 
    "Sorcerer": 6, 
    "Warlock": 8, 
    "Wizard": 6
}
class_saving = {
    "Artificer": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 2,
        "Intelligence": 2,
        "Wisdom":       0,
        "Charisma":     0,
    }, 
    "Barbarian": {
        "Strength":     2,
        "Dexterity":    0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    }, 
    "Bard": {
        "Strength":     0,
        "Dexterity":    2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     2,
    }, 
    "Cleric": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       2,
        "Charisma":     2,
    }, 
    "Druid": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 2,
        "Wisdom":       2,
        "Charisma":     0,
    }, 
    "Fighter": {
        "Strength":     2,
        "Dexterity":    0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    }, 
    "Monk": {
        "Strength":     2,
        "Dexterity":    2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    }, 
    "Paladin": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       2,
        "Charisma":     2,
    }, 
    "Ranger": {
        "Strength":     2,
        "Dexterity":    2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    }, 
    "Rogue": {
        "Strength":     0,
        "Dexterity":    2,
        "Constitution": 0,
        "Intelligence": 2,
        "Wisdom":       0,
        "Charisma":     0,
    }, 
    "Sorcerer": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     2,
    }, 
    "Warlock": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       2,
        "Charisma":     2,
    }, 
    "Wizard": {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 2,
        "Wisdom":       2,
        "Charisma":     0,
    }
}
# Backgrounds
backgrounds = ["Acolyte", "Athlete", "Charlatan", "City Watch", "Clan Crafter", "Cloistered Scholar", "Courtier", "Criminal", "Custom", "Entertainer", "Faction Agent", "Far Traveler", "Fey Lost", "Fisher", "Folk Hero", "Guild Artisan", "Haunted One", "Hermit", "House Agent", "Inheritor", "Investigator", "Knight", "Marine", "Mercenary Veteran", "Noble", "Outlander", "Port City Noble", "Sage", "Sailor", "Shipwright", "Smuggler", "Soldier", "Urban Bounty Hunter", "Urchin", "Violent Assassin", "Witch Carnival Hand"]
# Male Names
male = ["Ilint", "Nuwint", "Piltar", "Brodont", "Mauggair", "Vokrar", "Myrwinim", "Lalimin", "Celteeneil", "Cygoliam", "Vondrom", "Gulmiir", "Bhalgurn", "Darbek", "Theldahr", "Dulmor", "Bhaltharn", "Gimgram", "Ebrak", "Thornur", "Carris", "Zummenor", "Balbalar", "Nubby", "VanH", "CableKid", "Pnizzlez", "Arkeren", "DrFetus", "Eradan", "Dorsandoral", "Wranran", "Urifaren", "Carjeon", "Ervalur", "Wranlen", "Ulorin", "Vanlanann", "Zancraes", "Elfinas", "Riyeras", "Leophanis", "Yenzaren", "Hordithas", "Traword", "Walcoril", "Mezim", "Medam", "Nandur", "Roa", "Verder", "Nar", "Volderth", "Teth", "Suehkires", "Sat-Kor", "Vilmzousvok", "Mardisk", "Cha", "Chio", "Ornescol", "Zalur", "Thyneris", "Gueron", "Kilmong", "Akilius", "Morakos", "Thynevenom", "Horemon", "Casxikas", "Mavil", "Kavius"]
# Female Names
female = ["Varea", "Rili", "Odon", "Wama", "Ilar", "Eoma", "Worala", "Naslisau", "Ersesoum", "Zoleami", "Ranmyla", "Byllera", "Gemniss", "Reyntyn", "Brytnas", "Brendryn", "Bellela", "Dearglia", "Nesma", "Bronnura", "Sylcaryn", "Ulavyre", "Xyrphyra", "Faehana", "Yesralei", "Zindove", "Aragella", "Reymoira", "Keyzana", "Wynxisys", "Delqarin", "Gissie", "Hotice", "Floof", "Urilynn", "Madove", "Saelfine", "Galmalis", "Iroqarin", "Alymythe", "Hoviel", "Lesnalore", "Halyyra", "Fupisheil", "Eizeih", "Liroldra", "Kirrah", "Lirno", "Ce", "Bithiga", "Korhe", "Lazhuthe", "Nozes", "Duvrahi", "Yumma", "Jiao", "Pue", "Lontf", "Val", "Mithspira", "Zalypsis", "Valspira", "Marcira", "Cresis", "Datari", "Nithvine", "Phelypsis", "Phexori", "Iniyola"]
# Surnames
surname = ["Boldale", "Broodfinder", "Deepmantle", "Trollguard", "Boldfury", "Brangack", "Maroln", "Druhaveg", "Dubronack", "Hunkenurk", "Sterneye", "Lighthorn", "Wildforge", "Starkbane", "Strongboots", "Grazzihr", "Brenkam", "Cekuk", "Glurthirt", "Merdahun", "Oakensmile", "Rapidrest", "Azurelight", "Forestvale", "Oceanwalker", "Urinniphi", "Yurinne", "Nernadro", "Godrothro", "Gushennalkosh", "Cedarcrown", "Ambershine", "Woodmoon", "Cedarheel", "Nightlight", "Litholka", "Golithriith", "Ustral", "Lilphith", "Aldrennash", "Hosser", "Zaha", "Phoenixbreaker", "Marbletrack", "Bon", "Nimudz", "Stoutsun", "Lightningsnow", "Honskuchihk", "Lizdab", "Donumrildye", "Rarnetho", "Mieng", "Yay", "Ocinzo", "Culuzes", "Shammen", "Nannan", "Earthsnarl", "Phoenixpeak", "Vidz", "Glirdotsk", "Slateseeker", "Feathereyes", "Juezrinzed", "Dazdihd", "Digongotvi", "Stogaga", "Xum", "Puem", "Ivugar", "Ginzergi"]

race_stat_show = ""
subrace_stat_show = ""
class_stat_show = ""
background_stat_show = ""
male_stat_show = ""
female_stat_show = ""
surname_stat_show = ""
class_spread = ""
stat_roll = ""

Strength = ""
Str_Mod = ""
Str_Save = ""
Dexterity = ""
Dex_Mod = ""
Dex_Save = ""
Constitution = ""
Con_Mod = ""
Con_Save = ""
Intelligence = ""
Int_Mod = ""
Int_Save = ""
Wisdom = ""
Wis_Mod = ""
Wis_Save = ""
Charisma = ""
Cha_Mod = ""
Cha_Save = ""
hit_points = ""


# Spells
# Artificer - 2 cantrips - 2 first level
artificer_cantrip = ["Acid Splash", "Booming Blade", "Create Bonfire", "Dancing Lights", "Fire Bolt", "Frostbite", "Green-Flame Blade", "Guidance", "Light", "Lightning Lure", "Mage Hand", "Magic Stone", "Mending", "Message", "Poison Spray", "Prestidigitation", "Ray of Frost", "Resistance", "Shocking Grasp", "Spare the Dying", "Sword Burst", "Thorn Whip", "Thunderclap"]
artificer_first = ["Asorb Elements", "Alarm", "Arcane Weapon", "Catapult", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump", "Longstrider", "Purify Food and Drink", "Sanctuary", "Snare", "Tasha's Caustic Brew"]
# Bard - 2 cantrips - 4 first level
bard_cantrip = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation", "Thunderclap", "True Strike", "Vicious Mockery"]
bard_first = ["Animal Friendship", "Bane", "Charm Person", "Color Spray", "Command", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Dissonant Whispers", "Distort Value", "Earth Tremor", "Faerie Fire", "Feather Fall", "Guiding Hand", "Healing Word", "Heroism", "Identify", "Illusory Script", "Longstrider", "Puppet", "Sense Emotion", "Silent Image", "Silvery Barbs", "Sleep", "Speak with Animals", "Sudden Awakening", "Tasha's Hideous Laughter", "Thunderwave", "Unearthly Chourus", "Unseen Servant"]
# Cleric - 3 cantrips - Wisdom + Cleric Level (1)
cleric_cantrip = ["Decompose", "Guidance", "Hand of Radiance", "Light", "Mending", "Resistance", "Sacred Flame", "Spare the Dying", "Thaumaturgy", "Toll the Dead", "Virtue", "Word of Radiance"]
cleric_first = ["Bane", "Bless", "Ceremony", "Command", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Guiding Bolt", "Guiding Hand", "Healing Word", "Inflict Wounds", "Protection from Evil and Good", "Purify Food and Drink", "Sanctuary", "Shield of Faith"]
# Druid - 2 cantrips - Wisdom + Druid Level (1)
druid_cantrip = ["Control Flames", "Create Bonfire", "Druidcraft", "Frostbite", "Guidance", "Gust", "Infestation", "Magic Stone", "Mending", "Mold Earth", "Poison Spray", "Primal Savagery", "Produce Flame", "Resistance", "Shape Water", "Shillelagh", "Thorn Whip", "Thunderclap"]
druid_first = ["Asorb Elements", "Animal Friendship", "Beast Bond", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Earth Tremor", "Entangle", "Faerie Fire", "Fog Cloud", "Goodberry", "Guiding Hand", "Healing Word", "Ice Knife", "Jump", "Longstrider", "Protection from Evil and Good", "Purify Food and Drink", "Snare", "Speak with Animals", "Thunderwave", "Wild Cunning"]
# Sorcerer - 4 cantrips - 2 first
sorcerer_cantrip = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Gust", "Infestation", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Mind Sliver", "Minor Illusion", "Mold Earth", "On/Off", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shape Water", "Sword Burst", "Thunderclap", "True Strike"]
sorcerer_first = ["Asorb Elements", "Acid Stream", "Burning Hands", "Catapult", "Chaos Bolt", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Distort Value", "Earth Tremor", "Expeditious Retreat", "False Life", "Feather Fall", "Fog Cloud", "Grease", "Ice Knife", "Id Insinuation", "Infallible Relay", "Jump", "Mage Armor", "Magic Missle", "Ray of Sickness", "Remote Access", "Shield", "Silent Image", "Silvery Barbs", "Sleep", "Sudden Awakening", "Tasha's Caustic Brew", "Thunderwave", "Witch Bolt"]
# Warlock - 1 cantrips + Eldritch Blast - 2 first level
warlock_cantrip = ["Blade Ward", "Booming Blade", "Chill Touch", "Create Bonfire", "Friends", "Frostbite", "Green-Flame Blade", "Infestation", "Lightning Lure", "Mage Hand", "Magic Stone", "Mind Sliver", "Minor Illusion", "On/Off", "Poison Spray", "Prestidigitation", "Sword Burst", "Thunderclap", "Toll the Dead", "True Strike"]
warlock_first = ["Armor of Agathys", "Arms of Hadar", "Cause Fear", "Charm Person", "Comprehend Languages", "Distort Value", "Expeditious Retreat", "Healing Elixir", "Hellish Rebuke", "Hex", "Id Insinuation", "Illusory Script", "Infallible Relay", "Protection from Evil and Good", "Puppet", "Remote Access", "Sense Emotion", "Unseen Servant", "Witch Bolt"]
# Wizard - 3 cantrips - Intelligence + Wizard Level (1)
wizard_cantrip = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights", "Encode Thoughts", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Gust", "Infestation", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Mind Sliver", "Minor Illusion", "Mold Earth", "On/Off", "Poison Spray", "Prestidigitation", "Ray of Frost", "Sapping Sting", "Shape Water", "Shocking Grasp", "Sword Burst", "Thunderclap", "Toll the Dead", "True Strike"]
wizard_first = ["Asorb Elements", "Acid Stream", "Alarm", "Burning Hands", "Catapult", "Cause Fear", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Distort Value", "Earth Tremor", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Frost Fingers", "Gift of Alacrity", "Grease", "Healing Elixir", "Ice Knife", "Id Insinuation", "Identify", "Illusory Script", "Infallible Relay", "Jim's Magic Missle", "Jump", "Longstrider", "Mage Armor", "Magic Missle", "Magnify Gravity", "Protection from Evil and Good", "Puppet", "Ray of Sickness", "Remote Access", "Sense Emotion", "Shield", "Silent Image", "Silvery Barbs", "Sleep", "Snare", "Sudden Awakening", "Tasha's Caustic Brew", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"]

# URLs for the Races, Classes, Backgrounds, and Spells
urls = {
    "races": {
        "Aasimar": "http://dnd5e.wikidot.com/lineage:aasimar",
        "Animal Hybrid": "http://dnd5e.wikidot.com/lineage:simic-hybrid",
        "Birdfolk": "http://dnd5e.wikidot.com/lineage:aarakocra",
        "Bugbear": "http://dnd5e.wikidot.com/lineage:bugbear",
        "Centaur": "http://dnd5e.wikidot.com/lineage:centaur",
        "Changeling": "http://dnd5e.wikidot.com/lineage:changeling",
        "Dhampir": "http://dnd5e.wikidot.com/lineage:dhampir",
        "Dragonborn": "http://dnd5e.wikidot.com/lineage:dragonborn",
        "Dwarf": "http://dnd5e.wikidot.com/lineage:dwarf",
        "Elephantine": "https://www.skullsplitterdice.com/blogs/dnd/loxodon-5e",
        "Elf": "http://dnd5e.wikidot.com/lineage:elf",
        "Fairy": "http://dnd5e.wikidot.com/lineage:fairy",
        "Firbolg": "http://dnd5e.wikidot.com/lineage:firbolg",
        "Genasi": "https://www.dndbeyond.com/races/23-genasi",
        "Gith": "http://dnd5e.wikidot.com/lineage:githyanki",
        "Gnome": "http://dnd5e.wikidot.com/lineage:gnome",
        "Goblin": "http://dnd5e.wikidot.com/lineage:goblin",
        "Goliath": "http://dnd5e.wikidot.com/lineage:goliath",
        "Half-Elf": "http://dnd5e.wikidot.com/lineage:half-elf",
        "Half-Orc": "http://dnd5e.wikidot.com/lineage:half-orc",
        "Halfling": "http://dnd5e.wikidot.com/lineage:halfling",
        "Harefolk": "http://dnd5e.wikidot.com/lineage:harengon",
        "Hobgoblin": "http://dnd5e.wikidot.com/lineage:hobgoblin",
        "Human": "http://dnd5e.wikidot.com/lineage:human",
        "Kenku": "http://dnd5e.wikidot.com/lineage:kenku",
        "Kobold": "http://dnd5e.wikidot.com/lineage:kobold",
        "Leonine": "http://dnd5e.wikidot.com/lineage:leonin",
        "Lizardfolk": "http://dnd5e.wikidot.com/lineage:lizardfolk",
        "Minotaur": "http://dnd5e.wikidot.com/lineage:minotaur",
        "Orc": "http://dnd5e.wikidot.com/lineage:orc",
        "Owlkin": "http://dnd5e.wikidot.com/lineage:owlin",
        "Satyr": "http://dnd5e.wikidot.com/lineage:satyr",
        "Shifter": "http://dnd5e.wikidot.com/lineage:shifter",
        "Tabaxi": "http://dnd5e.wikidot.com/lineage:tabaxi",
        "Tiefling": "http://dnd5e.wikidot.com/lineage:tiefling",
        "Triton": "http://dnd5e.wikidot.com/lineage:triton",
        "Turtle": "http://dnd5e.wikidot.com/lineage:tortle",
        "Violetken": "http://dnd5e.wikidot.com/lineage:vedalken",
        "Warforged": "http://dnd5e.wikidot.com/lineage:warforged"
    },
    "classes": {
        "Artificer": "http://dnd5e.wikidot.com/artificer", 
        "Barbarian": "http://dnd5e.wikidot.com/barbarian", 
        "Bard": "http://dnd5e.wikidot.com/bard",
        "Cleric": "http://dnd5e.wikidot.com/cleric",
        "Druid": "http://dnd5e.wikidot.com/druid",
        "Fighter": "http://dnd5e.wikidot.com/fighter",
        "Monk": "http://dnd5e.wikidot.com/monk",
        "Paladin": "http://dnd5e.wikidot.com/paladin",
        "Ranger": "http://dnd5e.wikidot.com/ranger",
        "Rogue": "http://dnd5e.wikidot.com/rogue",
        "Sorcerer": "http://dnd5e.wikidot.com/sorcerer",
        "Warlock": "http://dnd5e.wikidot.com/warlock",
        "Wizard": "http://dnd5e.wikidot.com/wizard"
    },
    "backgrounds": {
        "Acolyte": "http://dnd5e.wikidot.com/background:acolyte",
        "Athlete": "http://dnd5e.wikidot.com/background:athlete",
        "Charlatan": "http://dnd5e.wikidot.com/background:charlatan",
        "City Watch": "http://dnd5e.wikidot.com/background:city-watch",
        "Clan Crafter": "http://dnd5e.wikidot.com/background:clan-crafter",
        "Cloistered Scholar": "http://dnd5e.wikidot.com/background:cloistered-scholar",
        "Courtier": "http://dnd5e.wikidot.com/background:courtier",
        "Criminal": "http://dnd5e.wikidot.com/background:criminal",
        "Custom": "https://www.dndbeyond.com/sources/basic-rules/personality-and-background",
        "Entertainer": "http://dnd5e.wikidot.com/background:entertainer",
        "Faction Agent": "http://dnd5e.wikidot.com/background:faction-agent",
        "Far Traveler": "http://dnd5e.wikidot.com/background:far-traveler",
        "Fey Lost": "http://dnd5e.wikidot.com/background:feylost",
        "Fisher": "http://dnd5e.wikidot.com/background:fisher",
        "Folk Hero": "http://dnd5e.wikidot.com/background:folk-hero",
        "Guild Artisan": "http://dnd5e.wikidot.com/background:guild-artisan",
        "Haunted One": "http://dnd5e.wikidot.com/background:haunted-one",
        "Hermit": "http://dnd5e.wikidot.com/background:hermit",
        "House Agent": "http://dnd5e.wikidot.com/background:house-agent",
        "Inheritor": "http://dnd5e.wikidot.com/background:inheritor",
        "Investigator": "http://dnd5e.wikidot.com/background:investigator",
        "Knight": "http://dnd5e.wikidot.com/background:knight-of-the-order",
        "Marine": "http://dnd5e.wikidot.com/background:marine",
        "Mercenary Veteran": "http://dnd5e.wikidot.com/background:mercenary-veteran",
        "Noble": "http://dnd5e.wikidot.com/background:noble",
        "Outlander": "http://dnd5e.wikidot.com/background:outlander",
        "Port City Noble": "http://dnd5e.wikidot.com/background:waterdhavian-noble",
        "Sage": "http://dnd5e.wikidot.com/background:sage",
        "Sailor": "http://dnd5e.wikidot.com/background:sailor",
        "Shipwright": "http://dnd5e.wikidot.com/background:shipwright",
        "Smuggler": "http://dnd5e.wikidot.com/background:smuggler",
        "Soldier": "http://dnd5e.wikidot.com/background:soldier",
        "Urban Bounty Hunter": "http://dnd5e.wikidot.com/background:urban-bounty-hunter",
        "Urchin": "http://dnd5e.wikidot.com/background:urchin",
        "Violent Assassin": "https://www.dandwiki.com/wiki/Professional_Assassin_(5e_Background)",
        "Witch Carnival Hand": "https://dnd5e.wikidot.com/background:witchlight-hand"
    },
    "spells": {
        "Acid Splash": "http://dnd5e.wikidot.com/spell:acid-splash",
        "Blade Ward": "http://dnd5e.wikidot.com/spell:blade-ward",
        "Booming Blade": "http://dnd5e.wikidot.com/spell:booming-blade",
        "Chill Touch": "http://dnd5e.wikidot.com/spell:chill-touch",
        "Control Flames": "http://dnd5e.wikidot.com/spell:control-flames",
        "Create Bonfire": "http://dnd5e.wikidot.com/spell:create-bonfire",
        "Dancing Lights": "http://dnd5e.wikidot.com/spell:dancing-lights",
        "Decompose": "http://dnd5e.wikidot.com/spell:decompose",
        "Druidcraft": "http://dnd5e.wikidot.com/spell:druidcraft",
        "Eldritch Blast": "http://dnd5e.wikidot.com/spell:encode-thoughts",
        "Encode Thoughts": "http://dnd5e.wikidot.com/spell:encode-thoughts",
        "Fire Bolt": "http://dnd5e.wikidot.com/spell:fire-bolt",
        "Friends": "http://dnd5e.wikidot.com/spell:friends",
        "Frostbite": "http://dnd5e.wikidot.com/spell:frostbite",
        "Green-Flame Blade": "http://dnd5e.wikidot.com/spell:green-flame-blade",
        "Guidance": "http://dnd5e.wikidot.com/spell:guidance",
        "Gust": "http://dnd5e.wikidot.com/spell:gust",
        "Hand of Radiance": "http://dnd5e.wikidot.com/spell:hand-of-radiance",
        "Infestation": "http://dnd5e.wikidot.com/spell:infestation",
        "Light": "http://dnd5e.wikidot.com/spell:light",
        "Lightning Lure": "http://dnd5e.wikidot.com/spell:lightning-lure",
        "Mage Hand": "http://dnd5e.wikidot.com/spell:mage-hand",
        "Magic Stone": "http://dnd5e.wikidot.com/spell:magic-stone",
        "Mending": "http://dnd5e.wikidot.com/spell:mending",
        "Message": "http://dnd5e.wikidot.com/spell:message",
        "Mind Sliver": "http://dnd5e.wikidot.com/spell:mind-sliver",
        "Minor Illusion": "http://dnd5e.wikidot.com/spell:minor-illusion",
        "Mold Earth": "http://dnd5e.wikidot.com/spell:mold-earth",
        "On/Off": "http://dnd5e.wikidot.com/spell:on-off",
        "Poison Spray": "http://dnd5e.wikidot.com/spell:poison-spray",
        "Prestidigitation": "http://dnd5e.wikidot.com/spell:prestidigitation",
        "Primal Savagery": "http://dnd5e.wikidot.com/spell:primal-savagery",
        "Produce Flame": "http://dnd5e.wikidot.com/spell:produce-flame",
        "Ray of Frost": "http://dnd5e.wikidot.com/spell:ray-of-frost",
        "Resistance": "http://dnd5e.wikidot.com/spell:resistance",
        "Sacred Flame": "http://dnd5e.wikidot.com/spell:sacred-flame",
        "Sapping Sting": "http://dnd5e.wikidot.com/spell:sapping-sting",
        "Shape Water": "http://dnd5e.wikidot.com/spell:shape-water",
        "Shillelagh": "http://dnd5e.wikidot.com/spell:shillelagh",
        "Shocking Grasp": "http://dnd5e.wikidot.com/spell:shocking-grasp",
        "Spare the Dying": "http://dnd5e.wikidot.com/spell:spare-the-dying",
        "Sword Burst": "http://dnd5e.wikidot.com/spell:sword-burst",
        "Thaumaturgy": "http://dnd5e.wikidot.com/spell:thaumaturgy",
        "Thorn Whip": "http://dnd5e.wikidot.com/spell:thorn-whip",
        "Thunderclap": "http://dnd5e.wikidot.com/spell:thunderclap",
        "Toll the Dead": "http://dnd5e.wikidot.com/spell:toll-the-dead",
        "True Strike": "http://dnd5e.wikidot.com/spell:true-strike",
        "Vicious Mockery": "http://dnd5e.wikidot.com/spell:vicious-mockery",
        "Virtue": "http://dnd5e.wikidot.com/spell:virtue",
        "Word of Radiance": "http://dnd5e.wikidot.com/spell:word-of-radiance",
        "Absorb Elements": "http://dnd5e.wikidot.com/spell:absorb-elements",
        "Acid Stream": "http://dnd5e.wikidot.com/spell:acid-stream",
        "Alarm": "http://dnd5e.wikidot.com/spell:alarm",
        "Animal Friendship": "http://dnd5e.wikidot.com/spell:animal-friendship",
        "Arcane Weapon": "http://dnd5e.wikidot.com/spell:arcane-weapon",
        "Armor of Agathys": "http://dnd5e.wikidot.com/spell:armor-of-agathys",
        "Arms of Hadar": "http://dnd5e.wikidot.com/spell:arms-of-hadar",
        "Bane": "http://dnd5e.wikidot.com/spell:bane",
        "Beast Bond": "http://dnd5e.wikidot.com/spell:beast-bond",
        "Bless": "http://dnd5e.wikidot.com/spell:bless",
        "Burning Hands": "http://dnd5e.wikidot.com/spell:burning-hands",
        "Catapult": "http://dnd5e.wikidot.com/spell:catapult",
        "Cause Fear": "http://dnd5e.wikidot.com/spell:cause-fear",
        "Ceremony": "http://dnd5e.wikidot.com/spell:ceremony",
        "Chaos Bolt": "http://dnd5e.wikidot.com/spell:chaos-bolt",
        "Charm Person": "http://dnd5e.wikidot.com/spell:charm-person",
        "Chromatic Orb": "http://dnd5e.wikidot.com/spell:chromatic-orb",
        "Color Spray": "http://dnd5e.wikidot.com/spell:color-spray",
        "Command": "http://dnd5e.wikidot.com/spell:command",
        "Compelled Duel": "http://dnd5e.wikidot.com/spell:compelled-duel",
        "Comprehend Languages": "http://dnd5e.wikidot.com/spell:comprehend-languages",
        "Create or Destroy Water": "http://dnd5e.wikidot.com/spell:create-or-destroy-water",
        "Cure Wounds": "http://dnd5e.wikidot.com/spell:cure-wounds",
        "Detect Evil and Good": "http://dnd5e.wikidot.com/spell:detect-evil-and-good",
        "Detect Magic": "http://dnd5e.wikidot.com/spell:detect-magic",
        "Detect Poison and Disease": "http://dnd5e.wikidot.com/spell:detect-poison-and-disease",
        "Disguise Self": "http://dnd5e.wikidot.com/spell:disguise-self",
        "Dissonant Whispers": "http://dnd5e.wikidot.com/spell:dissonant-whispers",
        "Distort Value": "http://dnd5e.wikidot.com/spell:distort-value",
        "Divine Favor": "http://dnd5e.wikidot.com/spell:divine-favor",
        "Earth Tremor": "http://dnd5e.wikidot.com/spell:earth-tremor",
        "Ensnaring Strike": "http://dnd5e.wikidot.com/spell:ensnaring-strike",
        "Entangle": "http://dnd5e.wikidot.com/spell:entangle",
        "Expeditious Retreat": "http://dnd5e.wikidot.com/spell:expeditious-retreat",
        "Faerie Fire": "http://dnd5e.wikidot.com/spell:faerie-fire",
        "False Life": "http://dnd5e.wikidot.com/spell:false-life",
        "Feather Fall": "http://dnd5e.wikidot.com/spell:feather-fall",
        "Find Familiar": "http://dnd5e.wikidot.com/spell:find-familiar",
        "Fog Cloud": "http://dnd5e.wikidot.com/spell:fog-cloud",
        "Frost Finger": "http://dnd5e.wikidot.com/spell:frost-fingers",
        "Gift of Alacrity": "http://dnd5e.wikidot.com/spell:gift-of-alacrity",
        "Goodberry": "http://dnd5e.wikidot.com/spell:goodberry",
        "Grease": "http://dnd5e.wikidot.com/spell:grease",
        "Guiding Bolt": "http://dnd5e.wikidot.com/spell:guiding-bolt",
        "Guiding Hand": "http://dnd5e.wikidot.com/spell:guiding-hand-ua",
        "Hall of Thorns": "http://dnd5e.wikidot.com/spell:hail-of-thorns",
        "Healing Elixir": "http://dnd5e.wikidot.com/spell:healing-elixir-ua",
        "Healing Word": "http://dnd5e.wikidot.com/spell:healing-word",
        "Hellish Rebuke": "http://dnd5e.wikidot.com/spell:hellish-rebuke",
        "Heroism": "http://dnd5e.wikidot.com/spell:heroism",
        "Hex": "http://dnd5e.wikidot.com/spell:hex",
        "Hunter's Mark": "http://dnd5e.wikidot.com/spell:hunters-mark",
        "Ice Knife": "http://dnd5e.wikidot.com/spell:ice-knife",
        "Id Insinuation": "http://dnd5e.wikidot.com/spell:id-insinuation",
        "Identify": "http://dnd5e.wikidot.com/spell:identify",
        "Illusory Script": "http://dnd5e.wikidot.com/spell:illusory-script",
        "Infallible Relay": "http://dnd5e.wikidot.com/spell:infallible-relay",
        "Inflict Wounds": "http://dnd5e.wikidot.com/spell:inflict-wounds",
        "Jim's Magic Missle": "http://dnd5e.wikidot.com/spell:jims-magic-missile",
        "Jump": "http://dnd5e.wikidot.com/spell:jump",
        "Longstrider": "http://dnd5e.wikidot.com/spell:longstrider",
        "Mage Armor": "http://dnd5e.wikidot.com/spell:mage-armor",
        "Magic Missle": "http://dnd5e.wikidot.com/spell:magic-missile",
        "Magnify Gravity": "http://dnd5e.wikidot.com/spell:magnify-gravity",
        "Protection from Evil and Good": "http://dnd5e.wikidot.com/spell:protection-from-evil-and-good",
        "Puppet": "http://dnd5e.wikidot.com/spell:puppet",
        "Purify Food and Drink": "http://dnd5e.wikidot.com/spell:purify-food-and-drink",
        "Ray of Sickness": "http://dnd5e.wikidot.com/spell:ray-of-sickness",
        "Remote Access": "http://dnd5e.wikidot.com/spell:remote-access",
        "Sanctuary": "http://dnd5e.wikidot.com/spell:sanctuary",
        "Searing Strike": "http://dnd5e.wikidot.com/spell:searing-smite",
        "Sense Emotion": "http://dnd5e.wikidot.com/spell:sense-emotion",
        "Shield": "http://dnd5e.wikidot.com/spell:shield",
        "Shield of Faith": "http://dnd5e.wikidot.com/spell:shield-of-faith",
        "Silent Image": "http://dnd5e.wikidot.com/spell:silent-image",
        "Silvery Barbs": "http://dnd5e.wikidot.com/spell:silvery-barbs",
        "Sleep": "http://dnd5e.wikidot.com/spell:sleep",
        "Snare": "http://dnd5e.wikidot.com/spell:snare",
        "Speak with Animals": "http://dnd5e.wikidot.com/spell:speak-with-animals",
        "Sudden Awakening": "http://dnd5e.wikidot.com/spell:sudden-awakening",
        "Tasha's Caustic Brew": "http://dnd5e.wikidot.com/spell:tashas-caustic-brew",
        "Tasha's Hideous Laughter": "http://dnd5e.wikidot.com/spell:tashas-hideous-laughter",
        "Tenser's Floating Disk": "http://dnd5e.wikidot.com/spell:tensers-floating-disk",
        "Thunderous Smite": "http://dnd5e.wikidot.com/spell:thunderous-smite",
        "Thunderwave": "http://dnd5e.wikidot.com/spell:thunderwave",
        "Unearthly Chorus": "http://dnd5e.wikidot.com/spell:unearthly-chorus",
        "Unseen Servant": "http://dnd5e.wikidot.com/spell:unseen-servant",
        "Wild Cunning": "http://dnd5e.wikidot.com/spell:wild-cunning",
        "Witch Bolt": "http://dnd5e.wikidot.com/spell:witch-bolt",
        "Wrathful Smite": "http://dnd5e.wikidot.com/spell:wrathful-smite",
        "Zephyr Strike": "http://dnd5e.wikidot.com/spell:zephyr-strike",
    }
}

def load_races_webpage(url):
    response = requests.get(url)
    return response.text

def generate_character():
    global race_stat_show
    global subrace_stat_show
    global class_stat_show
    global background_stat_show
    global male_stat_show
    global female_stat_show
    global surname_stat_show
    global class_spread
    global stat_roll

    random_race = tk.StringVar()
    if selected_race.get() == "Random Race":
        random_race = random.choice(races)
    else:
        random_race = selected_race.get() 
    random_class = tk.StringVar()
    if selected_class.get() == "Random Class":
        random_class = random.choice(classes)
    else:
        random_class = selected_class.get()
    random_background = tk.StringVar()
    if selected_background.get() == "Random Background":
        random_background = random.choice(backgrounds)
    else:
        random_background = selected_background.get()
    
    subraces = sub_race[random_race]
    random_subrace = random.choice(subraces)
    random_male = random.choice(male)
    random_female = random.choice(female)
    random_surname = random.choice(surname)
    race_stat_show = f"{random_race}"
    class_stat_show = f"{random_class}"
    background_stat_show = f"{random_background}"
    male_stat_show = f"{random_male}"
    female_stat_show = f"{random_female}"
    surname_stat_show = f"{random_surname}"
    return random_race, random_subrace, random_class, random_background, random_male, random_female, random_surname

def reset_selected():
    selected_race.set("Random Race")
    selected_class.set("Random Class")
    selected_background.set("Random Background")

def roll_4d6_drop_lowest():
    rolls = [random.randint(1, 6) for _ in range(4)]
    lowest_roll = min(rolls)
    rolls.remove(lowest_roll)
    total = sum(rolls)
    return total

def generate_ability_scores():
    scores = []
    for _ in range(6):
        score = roll_4d6_drop_lowest()
        scores.append(score)
    return scores

def open_url(url):
    webbrowser.open_new(url)

def display_character():
    global class_spread
    global stat_roll
    global Strength, Str_Mod, Str_Save, Dexterity, Dex_Mod, Dex_Save, Constitution, Con_Mod, Con_Save, Intelligence, Int_Mod, Int_Save, Wisdom, Wis_Mod, Wis_Save, Charisma, Cha_Mod, Cha_Save, hit_points
    random_race, random_subrace, random_class, random_background, random_male, random_female, random_surname = generate_character()
    roll_stat = generate_ability_scores()
    roll_stat.sort(reverse=True)
    stat_roll = roll_stat
    
    details_text.config(state=tk.NORMAL)
    details_text.delete(1.0, tk.END)
    # Character Gen
    details_text.insert(tk.END, "\nRace: ")
    details_text.insert(tk.END, random_race, ("race", random_race))
    details_text.insert(tk.END, " - ")
    details_text.insert(tk.END, random_subrace)
    details_text.insert(tk.END, "\nClass: ")
    details_text.insert(tk.END, random_class, ("class", random_class))
    details_text.insert(tk.END, "\nBackground: ")
    details_text.insert(tk.END, random_background, ("background", random_background))
    details_text.insert(tk.END, "\nMale Name: ")
    details_text.insert(tk.END, random_male)
    details_text.insert(tk.END, "\nFemale Name: ")
    details_text.insert(tk.END, random_female)
    details_text.insert(tk.END, "\nSurname: ")
    details_text.insert(tk.END, random_surname)
    details_text.insert(tk.END, "\n\n")
    # Dice roll
    details_text.insert(tk.END, "Here are your stats: ")
    details_text.insert(tk.END, roll_stat)
    details_text.insert(tk.END, "\n")
    details_text.insert(tk.END, "\nSuggested Stats: \n")

    if random_class == "Artificer":
        # Assign Stats
        Intelligence = (f"{roll_stat[0] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[0] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[0] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")

        Dexterity = f"{roll_stat[1] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"

        Constitution = f"{roll_stat[2] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"

        Wisdom = f"{roll_stat[3] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"

        Charisma = f"{roll_stat[4] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"

        hit_points = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod}) - ({Int_Save})\n")
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod}) - ({Dex_Save})\n")
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod}) - ({Con_Save})\n")
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod}) - ({Wis_Save})\n")
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod}) - ({Cha_Save})\n")
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod}) - ({Str_Save})\n")
        # Generate Spells
        a_c_1, a_c_2 = random.sample(artificer_cantrip, 2)
        a_f_1, a_f_2 = random.sample(artificer_first, 2)
        
        details_text.config(state=tk.NORMAL)

        details_text.insert(tk.END, "\n\nArtificiers have 2 Cantrips and 2 First Level Spells ")
        # Cantrips
        details_text.insert(tk.END, "\n\nArtificer Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, a_c_1, ("a_c_1", a_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, a_c_2, ("a_c_2", a_c_2))
        # First Level Spells
        details_text.insert(tk.END, "\n\nArtificer First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spells: ")
        details_text.insert(tk.END, a_f_1, ("a_f_1", a_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, a_f_2, ("a_f_2", a_f_2))
        # Cantrip URL
        details_text.tag_configure("a_c_1", foreground="blue", underline=True)
        details_text.tag_bind("a_c_1", "<Button-1>", lambda e: open_url(urls["spells"][a_c_1]))
        details_text.tag_configure("a_c_2", foreground="blue", underline=True)
        details_text.tag_bind("a_c_2", "<Button-1>", lambda e: open_url(urls["spells"][a_c_2]))
        # First URL
        details_text.tag_configure("a_f_1", foreground="blue", underline=True)
        details_text.tag_bind("a_f_1", "<Button-1>", lambda e: open_url(urls["spells"][a_f_1]))
        details_text.tag_configure("a_f_2", foreground="blue", underline=True)
        details_text.tag_bind("a_f_2", "<Button-1>", lambda e: open_url(urls["spells"][a_f_2]))

        details_text.config(state=tk.DISABLED)

    elif random_class == "Barbarian":
        # Assign Stats
        Strength = f"{roll_stat[0] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Dexterity = f"{roll_stat[2] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Wisdom = f"{roll_stat[3] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Charisma = f"{roll_stat[4] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Intelligence = (f"{roll_stat[5] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[5] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[5] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        details_text.config(state=tk.DISABLED)

    elif random_class == "Bard":
        # Assign Stats
        Charisma = f"{roll_stat[0] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Dexterity = f"{roll_stat[1] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Constitution = f"{roll_stat[2] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Wisdom = f"{roll_stat[3] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Intelligence = (f"{roll_stat[4] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        hit_points = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        # Generate Spells
        b_c_1, b_c_2 = random.sample(bard_cantrip, 2)
        b_f_1, b_f_2, b_f_3, b_f_4 = random.sample(bard_first, 4)

        details_text.config(state=tk.NORMAL)
        
        details_text.insert(tk.END, "\nBards have 2 Cantrips and 4 First Level Spells: ")
        # Cantrips
        details_text.insert(tk.END, "\n\nBard Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, b_c_1, ("b_c_1", b_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, b_c_2, ("b_c_2", b_c_2))
        # First Level Spells
        details_text.insert(tk.END, "\n\nBard First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, b_f_1, ("b_f_1", b_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, b_f_2, ("b_f_2", b_f_2))
        details_text.insert(tk.END, "\n    3rd Spell: ")
        details_text.insert(tk.END, b_f_3, ("b_f_3", b_f_3))
        details_text.insert(tk.END, "\n    4th Spell: ")
        details_text.insert(tk.END, b_f_4, ("b_f_4", b_f_4))
        # Cantrip URL
        details_text.tag_configure("b_c_1", foreground="blue", underline=True)
        details_text.tag_bind("b_c_1", "<Button-1>", lambda e: open_url(urls["spells"][b_c_1]))
        details_text.tag_configure("b_c_2", foreground="blue", underline=True)
        details_text.tag_bind("b_c_2", "<Button-1>", lambda e: open_url(urls["spells"][b_c_2]))
        # First URL
        details_text.tag_configure("b_f_1", foreground="blue", underline=True)
        details_text.tag_bind("b_f_1", "<Button-1>", lambda e: open_url(urls["spells"][b_f_1]))
        details_text.tag_configure("b_f_2", foreground="blue", underline=True)
        details_text.tag_bind("b_f_2", "<Button-1>", lambda e: open_url(urls["spells"][b_f_2]))
        details_text.tag_configure("b_f_3", foreground="blue", underline=True)
        details_text.tag_bind("b_f_3", "<Button-1>", lambda e: open_url(urls["spells"][b_f_3]))
        details_text.tag_configure("b_f_4", foreground="blue", underline=True)
        details_text.tag_bind("b_f_4", "<Button-1>", lambda e: open_url(urls["spells"][b_f_4]))

        details_text.config(state=tk.DISABLED)

    elif random_class == "Cleric":
        # Assign Stats
        stat_spread = ['Wisdom', 'Constitution', 'Dexterity', 'Strength', 'Intelligence', "Charisma"]
        Wisdom = f"{roll_stat[0] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Dexterity = f"{roll_stat[2] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Strength = f"{roll_stat[3] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        Intelligence = (f"{roll_stat[4] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")
        
        Charisma = f"{roll_stat[5] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"
        
        # Generate Spells
        c_c_1, c_c_2, c_c_3 = random.sample(cleric_cantrip, 3)
        c_f_1 = random.choice(cleric_first)
        c_f_2_1, c_f_2_2 = random.sample(cleric_first, 2)
        c_f_3_1, c_f_3_2, c_f_3_3 = random.sample(cleric_first, 3)
        c_f_4_1, c_f_4_2, c_f_4_3, c_f_4_4 = random.sample(cleric_first, 4)
        c_f_5_1, c_f_5_2, c_f_5_3, c_f_5_4, c_f_5_5 =random.sample(cleric_first, 5)
        c_f_6_1, c_f_6_2, c_f_6_3, c_f_6_4, c_f_6_5, c_f_6_6 =random.sample(cleric_first, 6)
        
        details_text.config(state=tk.NORMAL)

        details_text.insert(tk.END, "\nClerics have 3 cantrips and 'WIS+LVL' First Level Spells")
        # Cantrips
        details_text.insert(tk.END, "\n\nCleric Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, c_c_1, ("c_c_1", c_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, c_c_2, ("c_c_2", c_c_2))
        details_text.insert(tk.END, "\n    3rd Cantrip: ")
        details_text.insert(tk.END, c_c_3, ("c_c_3", c_c_3))
        # First Level - 1 Spell
        details_text.insert(tk.END, "\n\nCleric First Level Spells:")
        details_text.insert(tk.END, "\n    Wisdom 1-11: 1 spell ")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, c_f_1, ("c_f_1", c_f_1))
        # First Level - 2 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 12-13: 2 spells ")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, c_f_2_1, ("c_f_2_1", c_f_2_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, c_f_2_2, ("c_f_2_2", c_f_2_2))
        # First Level - 3 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 14-15: 3 spells ")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, c_f_3_1, ("c_f_3_1", c_f_3_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, c_f_3_2, ("c_f_3_2", c_f_3_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, c_f_3_3, ("c_f_3_3", c_f_3_3))
        # First Level - 4 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 16-17: 4 spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, c_f_4_1, ("c_f_4_1", c_f_4_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, c_f_4_2, ("c_f_4_2", c_f_4_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, c_f_4_3, ("c_f_4_3", c_f_4_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, c_f_4_4, ("c_f_4_4", c_f_4_4))
        # First Level - 5 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 18-19: 5 spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, c_f_5_1, ("c_f_5_1", c_f_5_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, c_f_5_2, ("c_f_5_2", c_f_5_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, c_f_5_3, ("c_f_5_3", c_f_5_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, c_f_5_4, ("c_f_5_4", c_f_5_4))
        details_text.insert(tk.END, "\n        5th Spell: ")
        details_text.insert(tk.END, c_f_5_5, ("c_f_5_5", c_f_5_5))
        # First Level - 6 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 20: 6 spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, c_f_6_1, ("c_f_6_1", c_f_6_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, c_f_6_2, ("c_f_6_2", c_f_6_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, c_f_6_3, ("c_f_6_3", c_f_6_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, c_f_6_4, ("c_f_6_4", c_f_6_4))
        details_text.insert(tk.END, "\n        5th Spell: ")
        details_text.insert(tk.END, c_f_6_5, ("c_f_6_5", c_f_6_5))
        details_text.insert(tk.END, "\n        6th Spell: ")
        details_text.insert(tk.END, c_f_6_6, ("c_f_6_6", c_f_6_6))
        # Cantrip URLs
        details_text.tag_configure("c_c_1", foreground="blue", underline=True)
        details_text.tag_bind("c_c_1", "<Button-1>", lambda e: open_url(urls["spells"][c_c_1]))
        details_text.tag_configure("c_c_2", foreground="blue", underline=True)
        details_text.tag_bind("c_c_2", "<Button-1>", lambda e: open_url(urls["spells"][c_c_2]))
        details_text.tag_configure("c_c_3", foreground="blue", underline=True)
        details_text.tag_bind("c_c_3", "<Button-1>", lambda e: open_url(urls["spells"][c_c_3]))
        # 1 URL
        details_text.tag_configure("c_f_1", foreground="blue", underline=True)
        details_text.tag_bind("c_f_1", "<Button-1>", lambda e: open_url(urls["spells"][c_f_1]))
        # 2 URL
        details_text.tag_configure("c_f_2_1", foreground="blue", underline=True)
        details_text.tag_bind("c_f_2_1", "<Button-1>", lambda e: open_url(urls["spells"][c_f_2_1]))
        details_text.tag_configure("c_f_2_2", foreground="blue", underline=True)
        details_text.tag_bind("c_f_2_2", "<Button-1>", lambda e: open_url(urls["spells"][c_f_2_2]))
        # 3 URL
        details_text.tag_configure("c_f_3_1", foreground="blue", underline=True)
        details_text.tag_bind("c_f_3_1", "<Button-1>", lambda e: open_url(urls["spells"][c_f_3_1]))
        details_text.tag_configure("c_f_3_2", foreground="blue", underline=True)
        details_text.tag_bind("c_f_3_2", "<Button-1>", lambda e: open_url(urls["spells"][c_f_3_2]))
        details_text.tag_configure("c_f_3_3", foreground="blue", underline=True)
        details_text.tag_bind("c_f_3_3", "<Button-1>", lambda e: open_url(urls["spells"][c_f_3_3]))
        # 4 URL
        details_text.tag_configure("c_f_4_1", foreground="blue", underline=True)
        details_text.tag_bind("c_f_4_1", "<Button-1>", lambda e: open_url(urls["spells"][c_f_4_1]))
        details_text.tag_configure("c_f_4_2", foreground="blue", underline=True)
        details_text.tag_bind("c_f_4_2", "<Button-1>", lambda e: open_url(urls["spells"][c_f_4_2]))
        details_text.tag_configure("c_f_4_3", foreground="blue", underline=True)
        details_text.tag_bind("c_f_4_3", "<Button-1>", lambda e: open_url(urls["spells"][c_f_4_3]))
        details_text.tag_configure("c_f_4_4", foreground="blue", underline=True)
        details_text.tag_bind("c_f_4_4", "<Button-1>", lambda e: open_url(urls["spells"][c_f_4_4]))
        # 5 URL
        details_text.tag_configure("c_f_5_1", foreground="blue", underline=True)
        details_text.tag_bind("c_f_5_1", "<Button-1>", lambda e: open_url(urls["spells"][c_f_5_1]))
        details_text.tag_configure("c_f_5_2", foreground="blue", underline=True)
        details_text.tag_bind("c_f_5_2", "<Button-1>", lambda e: open_url(urls["spells"][c_f_5_2]))
        details_text.tag_configure("c_f_5_3", foreground="blue", underline=True)
        details_text.tag_bind("c_f_5_3", "<Button-1>", lambda e: open_url(urls["spells"][c_f_5_3]))
        details_text.tag_configure("c_f_5_4", foreground="blue", underline=True)
        details_text.tag_bind("c_f_5_4", "<Button-1>", lambda e: open_url(urls["spells"][c_f_5_4]))
        details_text.tag_configure("c_f_5_5", foreground="blue", underline=True)
        details_text.tag_bind("c_f_5_5", "<Button-1>", lambda e: open_url(urls["spells"][c_f_5_5]))
        # 6 URL
        details_text.tag_configure("c_f_6_1", foreground="blue", underline=True)
        details_text.tag_bind("c_f_6_1", "<Button-1>", lambda e: open_url(urls["spells"][c_f_6_1]))
        details_text.tag_configure("c_f_6_2", foreground="blue", underline=True)
        details_text.tag_bind("c_f_6_2", "<Button-1>", lambda e: open_url(urls["spells"][c_f_6_2]))
        details_text.tag_configure("c_f_6_3", foreground="blue", underline=True)
        details_text.tag_bind("c_f_6_3", "<Button-1>", lambda e: open_url(urls["spells"][c_f_6_3]))
        details_text.tag_configure("c_f_6_4", foreground="blue", underline=True)
        details_text.tag_bind("c_f_6_4", "<Button-1>", lambda e: open_url(urls["spells"][c_f_6_4]))
        details_text.tag_configure("c_f_6_5", foreground="blue", underline=True)
        details_text.tag_bind("c_f_6_5", "<Button-1>", lambda e: open_url(urls["spells"][c_f_6_5]))
        details_text.tag_configure("c_f_6_6", foreground="blue", underline=True)
        details_text.tag_bind("c_f_6_6", "<Button-1>", lambda e: open_url(urls["spells"][c_f_6_6]))
        
        details_text.config(state=tk.DISABLED)

    elif random_class == "Druid":
        # Assign Stats
        stat_spread = ['Wisdom', 'Constitution', 'Dexterity', 'Intelligence', "Charisma", 'Strength']
        Wisdom = f"{roll_stat[0] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Dexterity = f"{roll_stat[2] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Intelligence = (f"{roll_stat[3] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Charisma = f"{roll_stat[4] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"
        
        # Generate Spells
        d_c_1, d_c_2 = random.sample(druid_cantrip, 2)
        d_f_1 = random.choice(druid_first)
        d_f_2_1, d_f_2_2 = random.sample(druid_cantrip, 2)
        d_f_3_1, d_f_3_2, d_f_3_3 = random.sample(druid_cantrip, 3)
        d_f_4_1, d_f_4_2, d_f_4_3, d_f_4_4 = random.sample(druid_cantrip, 4)
        d_f_5_1, d_f_5_2, d_f_5_3, d_f_5_4, d_f_5_5 = random.sample(druid_cantrip, 5)
        d_f_6_1, d_f_6_2, d_f_6_3, d_f_6_4, d_f_6_5, d_f_6_6 = random.sample(druid_cantrip, 6)
    
        details_text.config(state=tk.NORMAL)

        details_text.insert(tk.END, "\nDruids have 2 Cantrips and 'WIS+LVL' First Level Spells: ")
        # Cantrips
        details_text.insert(tk.END, "\n\nDruid Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, d_c_1, ("d_c_1", d_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, d_c_2, ("d_c_2", d_c_2))
        # First Level - 1 Spell
        details_text.insert(tk.END, "\n\nDruid First Level Spells: ")
        details_text.insert(tk.END, "\n    Wisdom 1-11: 1 Spell")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, d_f_1, ("d_f_1", d_f_1))
        # First Level - 2 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 12-13: 2 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, d_f_2_1, ("d_f_2_1", d_f_2_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, d_f_2_2, ("d_f_2_2", d_f_2_2))
        # First Level - 3 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 14-15: 3 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, d_f_3_1, ("d_f_3_1", d_f_3_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, d_f_3_2, ("d_f_3_2", d_f_3_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, d_f_3_3, ("d_f_3_3", d_f_3_3))
        # First Level - 4 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 14-17: 4 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, d_f_4_1, ("d_f_4_1", d_f_4_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, d_f_4_2, ("d_f_4_2", d_f_4_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, d_f_4_3, ("d_f_4_3", d_f_4_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, d_f_4_4, ("d_f_4_4", d_f_4_4))
        # First Level - 5 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 16-19: 5 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, d_f_5_1, ("d_f_5_1", d_f_5_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, d_f_5_2, ("d_f_5_2", d_f_5_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, d_f_5_3, ("d_f_5_3", d_f_5_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, d_f_5_4, ("d_f_5_4", d_f_5_4))
        details_text.insert(tk.END, "\n        5th Spell: ")
        details_text.insert(tk.END, d_f_5_5, ("d_f_5_5", d_f_5_5))
        # First Level - 6 Spells
        details_text.insert(tk.END, "\n\n    Wisdom 20: 6 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, d_f_6_1, ("d_f_6_1", d_f_6_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, d_f_6_2, ("d_f_6_2", d_f_6_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, d_f_6_3, ("d_f_6_3", d_f_6_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, d_f_6_4, ("d_f_6_4", d_f_6_4))
        details_text.insert(tk.END, "\n        5th Spell: ")
        details_text.insert(tk.END, d_f_6_5, ("d_f_6_5", d_f_6_5))
        details_text.insert(tk.END, "\n        6th Spell: ")
        details_text.insert(tk.END, d_f_6_6, ("d_f_6_6", d_f_6_6))
        # Cantrip URL
        details_text.tag_configure("d_c_1", foreground="blue", underline=True)
        details_text.tag_bind("d_c_1", "<Button-1>", lambda e: open_url(urls["spells"][d_c_1]))
        details_text.tag_configure("d_c_2", foreground="blue", underline=True)
        details_text.tag_bind("d_c_2", "<Button-1>", lambda e: open_url(urls["spells"][d_c_2]))
        # 1 URL
        details_text.tag_configure("d_f_1", foreground="blue", underline=True)
        details_text.tag_bind("d_f_1", "<Button-1>", lambda e: open_url(urls["spells"][d_f_1]))
        # 2 URL
        details_text.tag_configure("d_f_2_1", foreground="blue", underline=True)
        details_text.tag_bind("d_f_2_1", "<Button-1>", lambda e: open_url(urls["spells"][d_f_2_2]))
        details_text.tag_configure("d_f_2_2", foreground="blue", underline=True)
        details_text.tag_bind("d_f_2_2", "<Button-1>", lambda e: open_url(urls["spells"][d_f_2_2]))
        # 3 URL
        details_text.tag_configure("d_f_3_1", foreground="blue", underline=True)
        details_text.tag_bind("d_f_3_1", "<Button-1>", lambda e: open_url(urls["spells"][d_f_3_1]))
        details_text.tag_configure("d_f_3_2", foreground="blue", underline=True)
        details_text.tag_bind("d_f_3_2", "<Button-1>", lambda e: open_url(urls["spells"][d_f_3_2]))
        details_text.tag_configure("d_f_3_3", foreground="blue", underline=True)
        details_text.tag_bind("d_f_3_3", "<Button-1>", lambda e: open_url(urls["spells"][d_f_3_3]))
        # 4 URL
        details_text.tag_configure("d_f_4_1", foreground="blue", underline=True)
        details_text.tag_bind("d_f_4_1", "<Button-1>", lambda e: open_url(urls["spells"][d_f_4_1]))
        details_text.tag_configure("d_f_4_2", foreground="blue", underline=True)
        details_text.tag_bind("d_f_4_2", "<Button-1>", lambda e: open_url(urls["spells"][d_f_4_2]))
        details_text.tag_configure("d_f_4_3", foreground="blue", underline=True)
        details_text.tag_bind("d_f_4_3", "<Button-1>", lambda e: open_url(urls["spells"][d_f_4_3]))
        details_text.tag_configure("d_f_4_4", foreground="blue", underline=True)
        details_text.tag_bind("d_f_4_4", "<Button-1>", lambda e: open_url(urls["spells"][d_f_4_4]))
        # 5 URL
        details_text.tag_configure("d_f_5_1", foreground="blue", underline=True)
        details_text.tag_bind("d_f_5_1", "<Button-1>", lambda e: open_url(urls["spells"][d_f_5_1]))
        details_text.tag_configure("d_f_5_2", foreground="blue", underline=True)
        details_text.tag_bind("d_f_5_2", "<Button-1>", lambda e: open_url(urls["spells"][d_f_5_2]))
        details_text.tag_configure("d_f_5_3", foreground="blue", underline=True)
        details_text.tag_bind("d_f_5_3", "<Button-1>", lambda e: open_url(urls["spells"][d_f_5_3]))
        details_text.tag_configure("d_f_5_4", foreground="blue", underline=True)
        details_text.tag_bind("d_f_5_4", "<Button-1>", lambda e: open_url(urls["spells"][d_f_5_4]))
        details_text.tag_configure("d_f_5_5", foreground="blue", underline=True)
        details_text.tag_bind("d_f_5_5", "<Button-1>", lambda e: open_url(urls["spells"][d_f_5_5]))
        # 6 URL
        details_text.tag_configure("d_f_6_1", foreground="blue", underline=True)
        details_text.tag_bind("d_f_6_1", "<Button-1>", lambda e: open_url(urls["spells"][d_f_6_1]))
        details_text.tag_configure("d_f_6_2", foreground="blue", underline=True)
        details_text.tag_bind("d_f_6_2", "<Button-1>", lambda e: open_url(urls["spells"][d_f_6_2]))
        details_text.tag_configure("d_f_6_3", foreground="blue", underline=True)
        details_text.tag_bind("d_f_6_3", "<Button-1>", lambda e: open_url(urls["spells"][d_f_6_3]))
        details_text.tag_configure("d_f_6_4", foreground="blue", underline=True)
        details_text.tag_bind("d_f_6_4", "<Button-1>", lambda e: open_url(urls["spells"][d_f_6_4]))
        details_text.tag_configure("d_f_6_5", foreground="blue", underline=True)
        details_text.tag_bind("d_f_6_5", "<Button-1>", lambda e: open_url(urls["spells"][d_f_6_5]))
        details_text.tag_configure("d_f_6_6", foreground="blue", underline=True)
        details_text.tag_bind("d_f_6_6", "<Button-1>", lambda e: open_url(urls["spells"][d_f_6_6]))

        details_text.config(state=tk.DISABLED)

    elif random_class == "Fighter":
        # Assign Stats
        stat_spread = ['Strength', 'Constitution', 'Wisdom', "Charisma", 'Intelligence', 'Dexterity']
        Strength = f"{roll_stat[0] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Wisdom = f"{roll_stat[2] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Charisma = f"{roll_stat[3] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Intelligence = (f"{roll_stat[4] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Dexterity = f"{roll_stat[5] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        details_text.config(state=tk.DISABLED)

    elif random_class == "Monk":
        # Assign Stats
        stat_spread = ['Dexterity', 'Constitution', 'Wisdom', 'Strength', 'Intelligence', "Charisma"]
        Dexterity = f"{roll_stat[0] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Wisdom = f"{roll_stat[2] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Strength = f"{roll_stat[3] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        Intelligence = (f"{roll_stat[4] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")
        
        Charisma = f"{roll_stat[5] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"
        
        details_text.config(state=tk.DISABLED)

    elif random_class == "Paladin":
        # Assign Stats
        stat_spread = ['Strength', "Charisma", 'Constitution', 'Wisdom', 'Intelligence', 'Dexterity']
        Strength = f"{roll_stat[0] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        Charisma = f"{roll_stat[1] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")
        
        Constitution = f"{roll_stat[2] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Wisdom = f"{roll_stat[3] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Intelligence = (f"{roll_stat[4] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")
        
        Dexterity = f"{roll_stat[5] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        hit_points = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        details_text.config(state=tk.DISABLED)

    elif random_class == "Ranger":
        # Assign Stats
        stat_spread = ['Dexterity', 'Wisdom', 'Constitution', 'Intelligence', 'Strength', "Charisma"]
        Dexterity = f"{roll_stat[0] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Wisdom = f"{roll_stat[1] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Constitution = f"{roll_stat[2] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Intelligence = (f"{roll_stat[3] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Strength = f"{roll_stat[4] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        Charisma = f"{roll_stat[5] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        hit_points = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        details_text.config(state=tk.DISABLED)

    elif random_class == "Rogue":
        # Assign Stats
        stat_spread = ['Dexterity', 'Constitution', 'Wisdom', "Charisma", 'Intelligence', 'Strength']
        Dexterity = f"{roll_stat[0] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Wisdom = f"{roll_stat[2] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Charisma = f"{roll_stat[3] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Intelligence = (f"{roll_stat[4] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[4] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        details_text.config(state=tk.DISABLED)

    elif random_class == "Sorcerer":
        # Assign Stats
        stat_spread = ["Charisma", 'Constitution', 'Dexterity', 'Intelligence', 'Wisdom', 'Strength']
        Charisma = f"{roll_stat[0] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[0] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Dexterity = f"{roll_stat[2] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Intelligence = (f"{roll_stat[3] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Wisdom = f"{roll_stat[4] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        # Generate Spells
        s_c_1, s_c_2, s_c_3, s_c_4 = random.sample(sorcerer_cantrip, 4)
        s_f_1, s_f_2 = random.sample(sorcerer_first, 2)

        details_text.config(state=tk.NORMAL)

        details_text.insert(tk.END, "\nSorcerers have 4 Cantrips and 2 First Level Spells")
        # Cantrips
        details_text.insert(tk.END, "\n\nSorcerer Cantrips:")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, s_c_1, ("s_c_1", s_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, s_c_2, ("s_c_2", s_c_2))
        details_text.insert(tk.END, "\n    3rd Cantrip: ")
        details_text.insert(tk.END, s_c_3, ("s_c_3", s_c_3))
        details_text.insert(tk.END, "\n    4th Cantrip: ")
        details_text.insert(tk.END, s_c_4, ("s_c_4", s_c_4))
        # First Level Spells
        details_text.insert(tk.END, "\n\nSorcerer First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, s_f_1, ("s_f_1", s_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, s_f_2, ("s_f_2", s_f_2))
        # Cantrip URL
        details_text.tag_configure("s_c_1", foreground="blue", underline=True)
        details_text.tag_bind("s_c_1", "<Button-1>", lambda e: open_url(urls["spells"][s_c_1]))
        details_text.tag_configure("s_c_2", foreground="blue", underline=True)
        details_text.tag_bind("s_c_2", "<Button-1>", lambda e: open_url(urls["spells"][s_c_2]))
        details_text.tag_configure("s_c_3", foreground="blue", underline=True)
        details_text.tag_bind("s_c_3", "<Button-1>", lambda e: open_url(urls["spells"][s_c_3]))
        details_text.tag_configure("s_c_4", foreground="blue", underline=True)
        details_text.tag_bind("s_c_4", "<Button-1>", lambda e: open_url(urls["spells"][s_c_4]))
        # First Level URL
        details_text.tag_configure("s_f_1", foreground="blue", underline=True)
        details_text.tag_bind("s_f_1", "<Button-1>", lambda e: open_url(urls["spells"][s_f_1]))
        details_text.tag_configure("s_f_2", foreground="blue", underline=True)
        details_text.tag_bind("s_f_2", "<Button-1>", lambda e: open_url(urls["spells"][s_f_2]))
        
        details_text.config(state=tk.DISABLED)

    elif random_class == "Warlock":
        # Assign Stats
        stat_spread = ["Charisma", 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Strength']
        Charisma = f"{roll_stat[0] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[0] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Dexterity = f"{roll_stat[1] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Constitution = f"{roll_stat[2] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Intelligence = (f"{roll_stat[3] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[3] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Wisdom = f"{roll_stat[4] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        hit_points = f"{(((roll_stat[2] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"

        # Generate Spells
        w_c_1, w_c_2 = random.sample(warlock_cantrip, 2)
        w_f_1, w_f_2 = random.sample(warlock_first, 2)

        details_text.config(state=tk.NORMAL)

        details_text.insert(tk.END, "\nWarlocks have 2 Cantrips and 2 First Level Spells ")
        # Cantrips
        details_text.insert(tk.END, "\n\nWarlock Cantrips: Be honest, we know Eldritch Blast is going to be one of them ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, w_c_1, ("w_c_1", w_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, w_c_2, ("w_c_2", w_c_2))
        # First Level Spells
        details_text.insert(tk.END, "\n\nWarlock First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spells: ")
        details_text.insert(tk.END, w_f_1, ("w_f_1", w_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, w_f_2, ("w_f_2", w_f_2))
        # Cantrip URL
        details_text.tag_configure("w_c_1", foreground="blue", underline=True)
        details_text.tag_bind("w_c_1", "<Button-1>", lambda e: open_url(urls["spells"][w_c_1]))
        details_text.tag_configure("w_c_2", foreground="blue", underline=True)
        details_text.tag_bind("w_c_2", "<Button-1>", lambda e: open_url(urls["spells"][w_c_2]))
        # First URL
        details_text.tag_configure("w_f_1", foreground="blue", underline=True)
        details_text.tag_bind("w_f_1", "<Button-1>", lambda e: open_url(urls["spells"][w_f_1]))
        details_text.tag_configure("w_f_2", foreground="blue", underline=True)
        details_text.tag_bind("w_f_2", "<Button-1>", lambda e: open_url(urls["spells"][w_f_2]))

        details_text.config(state=tk.DISABLED)
            
    elif random_class == "Wizard":
        # Assign Stats
        stat_spread = ['Intelligence', 'Constitution', 'Dexterity', 'Wisdom', "Charisma", 'Strength']
        Intelligence = (f"{roll_stat[0] + race_bonus[random_race]['Intelligence']}")
        Int_Mod = (f"{((roll_stat[0] + race_bonus[random_race]['Intelligence']) - 10) // 2}")
        Int_Save = (f"{(((roll_stat[0] + race_bonus[random_race]['Intelligence']) - 10) // 2) + class_saving[random_class]['Intelligence']}")
        details_text.insert(tk.END, f"    Intelligence: {Intelligence} - ({Int_Mod})\n")

        Constitution = f"{roll_stat[1] + race_bonus[random_race]['Constitution']}"
        Con_Mod = f"{((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2}"
        Con_Save = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + class_saving[random_class]['Constitution']}"
        details_text.insert(tk.END, f"    Constitution: {Constitution} - ({Con_Mod})\n")

        Dexterity = f"{roll_stat[2] + race_bonus[random_race]['Dexterity']}"
        Dex_Mod = f"{((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2}"
        Dex_Save = f"{(((roll_stat[2] + race_bonus[random_race]['Dexterity']) - 10) // 2) + class_saving[random_class]['Dexterity']}"
        details_text.insert(tk.END, f"    Dexterity: {Dexterity} - ({Dex_Mod})\n")

        Wisdom = f"{roll_stat[3] + race_bonus[random_race]['Wisdom']}"
        Wis_Mod = f"{((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2}"
        Wis_Save = f"{(((roll_stat[3] + race_bonus[random_race]['Wisdom']) - 10) // 2) + class_saving[random_class]['Wisdom']}"
        details_text.insert(tk.END, f"    Wisdom: {Wisdom} - ({Wis_Mod})\n")

        Charisma = f"{roll_stat[4] + race_bonus[random_race]['Charisma']}"
        Cha_Mod = f"{((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2}"
        Cha_Save = f"{(((roll_stat[4] + race_bonus[random_race]['Charisma']) - 10) // 2) + class_saving[random_class]['Charisma']}"
        details_text.insert(tk.END, f"    Charisma: {Charisma} - ({Cha_Mod})\n")

        Strength = f"{roll_stat[5] + race_bonus[random_race]['Strength']}"
        Str_Mod = f"{((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2}"
        Str_Save = f"{(((roll_stat[5] + race_bonus[random_race]['Strength']) - 10) // 2) + class_saving[random_class]['Strength']}"
        details_text.insert(tk.END, f"    Strength: {Strength} - ({Str_Mod})\n")

        hit_points = f"{(((roll_stat[1] + race_bonus[random_race]['Constitution']) - 10) // 2) + hit_dice[random_class]}"
        
        # Generate Spells
        z_c_1, z_c_2, z_c_3 = random.sample(wizard_cantrip, 3)
        z_f_1 = random.choice(wizard_first)
        z_f_2_1, z_f_2_2 = random.sample(wizard_first, 2)
        z_f_3_1, z_f_3_2, z_f_3_3, = random.sample(wizard_first, 3)
        z_f_4_1, z_f_4_2, z_f_4_3, z_f_4_4 = random.sample(wizard_first, 4)
        z_f_5_1, z_f_5_2, z_f_5_3, z_f_5_4, z_f_5_5 = random.sample(wizard_first, 5)
        z_f_6_1, z_f_6_2, z_f_6_3, z_f_6_4, z_f_6_5, z_f_6_6 =random.sample(wizard_first, 6)

        details_text.config(state=tk.NORMAL)

        details_text.insert(tk.END, "\nWizards have 2 Cantrips and 'INT+LVL' First Level Spells: ")
        # Cantrips
        details_text.insert(tk.END, "\n\nWizard Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, z_c_1, ("z_c_1", z_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, z_c_2, ("z_c_2", z_c_2))
        details_text.insert(tk.END, "\n    3rd Cantrip: ")
        details_text.insert(tk.END, z_c_3, ("z_c_3", z_c_3))
        # First Level - 1 Spell
        details_text.insert(tk.END, "\n\nWizard First Level Spells: ")
        details_text.insert(tk.END, "\n    Intelligence 1-11: 1 Spell")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, z_f_1, ("z_f_1", z_f_1))
        # First Level - 2 Spells
        details_text.insert(tk.END, "\n\n    Intelligence 12-13: 2 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, z_f_2_1, ("z_f_2_1", z_f_2_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, z_f_2_2, ("z_f_2_2", z_f_2_2))
        # First Level - 3 Spells
        details_text.insert(tk.END, "\n\n    Intelligence 14-15: 3 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, z_f_3_1, ("z_f_3_1", z_f_3_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, z_f_3_2, ("z_f_3_2", z_f_3_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, z_f_3_3, ("z_f_3_3", z_f_3_3))
        # First Level - 4 Spells
        details_text.insert(tk.END, "\n\n    Intelligence 16-17: 4 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, z_f_4_1, ("z_f_4_1", z_f_4_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, z_f_4_2, ("z_f_4_2", z_f_4_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, z_f_4_3, ("z_f_4_3", z_f_4_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, z_f_4_4, ("z_f_4_4", z_f_4_4))
        # First Level - 5 Spells
        details_text.insert(tk.END, "\n\n    Intelligence 18-19: 5 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, z_f_5_1, ("z_f_5_1", z_f_5_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, z_f_5_2, ("z_f_5_2", z_f_5_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, z_f_5_3, ("z_f_5_3", z_f_5_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, z_f_5_4, ("z_f_5_4", z_f_5_4))
        details_text.insert(tk.END, "\n        5th Spell: ")
        details_text.insert(tk.END, z_f_5_5, ("z_f_5_5", z_f_5_5))
        # First Level - 6 Spells
        details_text.insert(tk.END, "\n\n    Intelligence 20: 6 Spells")
        details_text.insert(tk.END, "\n        1st Spell: ")
        details_text.insert(tk.END, z_f_6_1, ("z_f_6_1", z_f_6_1))
        details_text.insert(tk.END, "\n        2nd Spell: ")
        details_text.insert(tk.END, z_f_6_2, ("z_f_6_2", z_f_6_2))
        details_text.insert(tk.END, "\n        3rd Spell: ")
        details_text.insert(tk.END, z_f_6_3, ("z_f_6_3", z_f_6_3))
        details_text.insert(tk.END, "\n        4th Spell: ")
        details_text.insert(tk.END, z_f_6_4, ("z_f_6_4", z_f_6_4))
        details_text.insert(tk.END, "\n        5th Spell: ")
        details_text.insert(tk.END, z_f_6_5, ("z_f_6_5", z_f_6_5))
        details_text.insert(tk.END, "\n        6th Spell: ")
        details_text.insert(tk.END, z_f_6_6, ("z_f_6_6", z_f_6_6))
        # Cantrip URL
        details_text.tag_configure("z_c_1", foreground="blue", underline=True)
        details_text.tag_bind("z_c_1", "<Button-1>", lambda e: open_url(urls["spells"][z_c_1]))
        details_text.tag_configure("z_c_2", foreground="blue", underline=True)
        details_text.tag_bind("z_c_2", "<Button-1>", lambda e: open_url(urls["spells"][z_c_2]))
        details_text.tag_configure("z_c_3", foreground="blue", underline=True)
        details_text.tag_bind("z_c_3", "<Button-1>", lambda e: open_url(urls["spells"][z_c_3]))
        # 1 URL
        details_text.tag_configure("z_f_1", foreground="blue", underline=True)
        details_text.tag_bind("z_f_1", "<Button-1>", lambda e: open_url(urls["spells"][z_f_1]))
        # 2 URL
        details_text.tag_configure("z_f_2_1", foreground="blue", underline=True)
        details_text.tag_bind("z_f_2_1", "<Button-1>", lambda e: open_url(urls["spells"][z_f_2_1]))
        details_text.tag_configure("z_f_2_2", foreground="blue", underline=True)
        details_text.tag_bind("z_f_2_2", "<Button-1>", lambda e: open_url(urls["spells"][z_f_2_2]))
        # 3 URL
        details_text.tag_configure("z_f_3_1", foreground="blue", underline=True)
        details_text.tag_bind("z_f_3_1", "<Button-1>", lambda e: open_url(urls["spells"][z_f_3_1]))
        details_text.tag_configure("z_f_3_2", foreground="blue", underline=True)
        details_text.tag_bind("z_f_3_2", "<Button-1>", lambda e: open_url(urls["spells"][z_f_3_2]))
        details_text.tag_configure("z_f_3_3", foreground="blue", underline=True)
        details_text.tag_bind("z_f_3_3", "<Button-1>", lambda e: open_url(urls["spells"][z_f_3_3]))
        # 4 URL
        details_text.tag_configure("z_f_4_1", foreground="blue", underline=True)
        details_text.tag_bind("z_f_4_1", "<Button-1>", lambda e: open_url(urls["spells"][z_f_4_1]))
        details_text.tag_configure("z_f_4_2", foreground="blue", underline=True)
        details_text.tag_bind("z_f_4_2", "<Button-1>", lambda e: open_url(urls["spells"][z_f_4_2]))
        details_text.tag_configure("z_f_4_3", foreground="blue", underline=True)
        details_text.tag_bind("z_f_4_3", "<Button-1>", lambda e: open_url(urls["spells"][z_f_4_3]))
        details_text.tag_configure("z_f_4_4", foreground="blue", underline=True)
        details_text.tag_bind("z_f_4_4", "<Button-1>", lambda e: open_url(urls["spells"][z_f_4_4]))
        # 5 URL
        details_text.tag_configure("z_f_5_1", foreground="blue", underline=True)
        details_text.tag_bind("z_f_5_1", "<Button-1>", lambda e: open_url(urls["spells"][z_f_5_1]))
        details_text.tag_configure("z_f_5_2", foreground="blue", underline=True)
        details_text.tag_bind("z_f_5_2", "<Button-1>", lambda e: open_url(urls["spells"][z_f_5_2]))
        details_text.tag_configure("z_f_5_3", foreground="blue", underline=True)
        details_text.tag_bind("z_f_5_3", "<Button-1>", lambda e: open_url(urls["spells"][z_f_5_3]))
        details_text.tag_configure("z_f_5_4", foreground="blue", underline=True)
        details_text.tag_bind("z_f_5_4", "<Button-1>", lambda e: open_url(urls["spells"][z_f_5_4]))
        details_text.tag_configure("z_f_5_5", foreground="blue", underline=True)
        details_text.tag_bind("z_f_5_5", "<Button-1>", lambda e: open_url(urls["spells"][z_f_5_5]))
        # 6 URL
        details_text.tag_configure("z_f_6_1", foreground="blue", underline=True)
        details_text.tag_bind("z_f_6_1", "<Button-1>", lambda e: open_url(urls["spells"][z_f_6_1]))
        details_text.tag_configure("z_f_6_2", foreground="blue", underline=True)
        details_text.tag_bind("z_f_6_2", "<Button-1>", lambda e: open_url(urls["spells"][z_f_6_2]))
        details_text.tag_configure("z_f_6_3", foreground="blue", underline=True)
        details_text.tag_bind("z_f_6_3", "<Button-1>", lambda e: open_url(urls["spells"][z_f_6_3]))
        details_text.tag_configure("z_f_6_4", foreground="blue", underline=True)
        details_text.tag_bind("z_f_6_4", "<Button-1>", lambda e: open_url(urls["spells"][z_f_6_4]))
        details_text.tag_configure("z_f_6_5", foreground="blue", underline=True)
        details_text.tag_bind("z_f_6_5", "<Button-1>", lambda e: open_url(urls["spells"][z_f_6_5]))
        details_text.tag_configure("z_f_6_6", foreground="blue", underline=True)
        details_text.tag_bind("z_f_6_6", "<Button-1>", lambda e: open_url(urls["spells"][z_f_6_6]))

        details_text.config(state=tk.DISABLED)
    
# Character Gen URLs
    details_text.tag_configure("race", foreground="blue", underline=True)
    details_text.tag_bind("race", "<Button-1>", lambda e: open_url(urls["races"][random_race]))
    details_text.tag_configure("class", foreground="blue", underline=True)
    details_text.tag_bind("class", "<Button-1>", lambda e: open_url(urls["classes"][random_class]))
    details_text.tag_configure("background", foreground="blue", underline=True)
    details_text.tag_bind("background", "<Button-1>", lambda e: open_url(urls["backgrounds"][random_background]))
    

# Commands for Menu Buttons

def display_race_info():
    race_details = race_stat_show
    race_stats = Toplevel(window)
    race_stats.title(f"{race_details} Details")
    race_stats.geometry("800x600")
    
    if race_details == "":
        race_stats.destroy()
        messagebox.showerror("Error", "Please generate a character!")

    races_html = HTMLLabel(race_stats, html="<h1>Loading...</h1>")
    races_html.pack(fill="both", expand=True)

    url = urls["races"][race_details]
    races_html_content = load_races_webpage(url)
    races_html.set_html(races_html_content)
    
    race_stats.mainloop()

def display_class_info():
    class_details = class_stat_show
    class_stats = Toplevel(window)
    class_stats.title(f"{class_details} Details")
    class_stats.geometry("800x600")
    
    if class_details == "":
        class_stats.destroy()
        messagebox.showerror("Error", "Please generate a character!")

    class_html = HTMLLabel(class_stats, html="<h1>Loading...</h1>")
    class_html.pack(fill="both", expand=True)

    url = urls["classes"][class_details]
    class_html_content = load_races_webpage(url)
    class_html.set_html(class_html_content)
    
    class_stats.mainloop()

def display_background_info():
    background_details = background_stat_show
    background_stats = Toplevel(window)
    background_stats.title(f"{background_details} Details")
    background_stats.geometry("800x600")

    if background_details == "":
        background_stats.destroy()
        messagebox.showerror("Error", "Please generate a character!")

    background_html = HTMLLabel(background_stats, html="<h1>Loading...</h1>")
    background_html.pack(fill="both", expand=True)

    url = urls["backgrounds"][background_details]
    background_html_content = load_races_webpage(url)
    background_html.set_html(background_html_content)
    
    background_stats.mainloop()

def display_character_sheet():
    global race_stat_show, class_stat_show, background_stat_show, male_stat_show, female_stat_show, surname_stat_show, class_spread, stat_roll
    global Strength, Str_Mod, Dexterity, Dex_Mod, Constitution, Con_Mod, Intelligence, Int_Mod, Wisdom, Wis_Mod, Charisma, Cha_Mod, class_saving, hit_points
    equipment_stats = Toplevel(window)
    equipment_stats.title("Character Sheet")
    equipment_stats.geometry("300x300")

    #if class_stat_show == "Artificer":
    equip_label = tk.Label(equipment_stats, text="Artificers can choose 2 of these skills").pack()
    equip_frame = tk.Frame(equipment_stats, bd=2, relief=SUNKEN)
    equip_frame.pack(fill=X)
    



    char_sheet_stats = Toplevel(window)
    char_sheet_stats.title("Character Sheet")
    char_sheet_stats.geometry("800x600")
    name_race_class = tk.Frame(char_sheet_stats, bd=2, relief=tk.SUNKEN)
    name_race_class.pack(side=TOP, fill=X)
    char_name = tk.Label(name_race_class, text=f"Character Name: {male_stat_show} ({female_stat_show}) {surname_stat_show}").pack(side=tk.LEFT)
    class_background = tk.Label(name_race_class, text=f"Class: {class_stat_show} - Background: {background_stat_show}\nRace: {race_stat_show} - Alignment: Lawful Neutral").pack(side=tk.RIGHT)
    #race_alignment = tk.Label(name_race_class, text=f"Race: {race_stat_show} - Alignment: Lawful Neutral").pack()
    int_hp_speed = tk.Frame(char_sheet_stats, bd=2, relief=tk.SUNKEN)
    int_hp_speed.pack(fill=X)
    initative = tk.Label(int_hp_speed, text=f"Initative: \n{Dex_Mod}   ").pack(side=LEFT)
    hp = tk.Label(int_hp_speed, text=f"HP: \n{hit_points}   ").pack(side=LEFT)
    speed = tk.Label(int_hp_speed, text="Speed: \n30   ").pack(side=LEFT)
    hitdice = tk.Label(int_hp_speed, text=f"Hit Dice: \n1d{hit_dice[class_stat_show]}").pack(side=RIGHT)
    armor_class = tk.Label(int_hp_speed, text=f"AC: \ntbd").pack(side=RIGHT)
    prof_bonus = tk.Label(int_hp_speed, text="Profeciency: \n+2").pack(side=RIGHT)
    stats_frame = tk.Frame(char_sheet_stats, bd=2, relief=tk.SUNKEN)
    stats_frame.pack(fill=Y, side=LEFT)
    str_stat = tk.Label(stats_frame, text=f"Strength: \nScore: {Strength} \nModifier: {Str_Mod} \nSave: {Str_Save}\n\nDexterity: \nScore: {Dexterity} \nModifier: {Dex_Mod} \nSave: {Dex_Save}\n\nConstitution: \nScore: {Constitution} \nModifier: {Con_Mod} \nSave: {Con_Save}\n\nIntelligence: \nScore: {Intelligence} \nModifier: {Int_Mod} \nSave: {Int_Save}\n\nWisdom: \nScore: {Wisdom} \nModifier: {Wis_Mod} \nSave: {Wis_Save}\n\nCharisma: \nScore: {Charisma} \nModifier: {Cha_Mod} \nSave: {Cha_Save}").pack(side=LEFT)
    skills_frame = tk.Frame(char_sheet_stats, bd=2, relief=tk.SUNKEN)
    skills_frame.pack(fill=Y, side=LEFT)
    skills = tk.Label(skills_frame, text=f"Acrobatics\n").pack(side=LEFT)
    

# Make Window
window = tk.Tk()
window.title("Random Character Generator")
bold_font = font.Font(weight="bold")

    #Menu Bar
my_menu_bar = tk.Frame(window, relief="raised", bd=2)
my_menu_bar.pack(fill=tk.X)
    # Race Menu Button
race_menu_button = tk.Menubutton(my_menu_bar, text="Race")
race_menu_button.pack(side=tk.LEFT)
race_menu = tk.Menu(race_menu_button, tearoff=0)
race_menu_button['menu'] = race_menu
race_menu.add('command', label='Show Race Stats', command=display_race_info)
    # Class Menu Button
class_menu_button = tk.Menubutton(my_menu_bar, text="Class")
class_menu_button.pack(side=tk.LEFT)
class_menu = tk.Menu(class_menu_button, tearoff=0)
class_menu_button['menu'] = class_menu
class_menu.add('command', label='Show Class Stats', command=display_class_info)
    # Background Menu Button
background_menu_button = tk.Menubutton(my_menu_bar, text="Background")
background_menu_button.pack(side=tk.LEFT)
background_menu = tk.Menu(background_menu_button, tearoff=0)
background_menu_button['menu'] = background_menu
background_menu.add('command', label='Show Background Stats', command=display_background_info)
    # Generate Character Sheet Button
character_sheet_button = tk.Menubutton(my_menu_bar, text="Character Sheet")
character_sheet_button.pack(side=tk.RIGHT)
character_sheet = tk.Menu(character_sheet_button, tearoff=0)
character_sheet_button['menu'] = character_sheet
character_sheet.add('command', label='Generate Character Sheet', command=display_character_sheet)

stat_vars = []
button_frame = tk.Frame(window, relief="raised", bd=2)
button_frame.pack(fill="x")
    # Race Dropdown
selected_race = tk.StringVar(value="Random Race")
race_dropdown_menu = tk.OptionMenu(button_frame, selected_race, "Random Race", *races)
race_dropdown_menu.pack(side=LEFT, padx=5)
    # Class Dropdown
selected_class = tk.StringVar(value="Random Class")
class_dropdown_menu = tk.OptionMenu(button_frame, selected_class, "Random Class", *classes)
class_dropdown_menu.pack(side=LEFT, padx=5)
    # Background Dropdown
selected_background = tk.StringVar(value="Random Background")
background_dropdown_menu = tk.OptionMenu(button_frame, selected_background, "Random Background", *backgrounds)
background_dropdown_menu.pack(side=LEFT, padx=5)
    # Reset Button
reset_button = tk.Button(button_frame, text="Reset", command=reset_selected)
reset_button.pack(side=RIGHT, ipadx=20, padx=5)

    # Generate Button
button = tk.Button(window, text="Generate Character", font=("Helvetica", 16), command=display_character)
button.pack(pady=15)
# Blank Text
details_text = tk.Text(window, font=("Helvetica", 16), width=75, height=50)
details_text.pack(pady=5, padx=20)
# Disable text
details_text.config(state=tk.DISABLED)


window.mainloop()