class Race():
    def __init__(self, name, abilities, alignment, creature_type, size, walk_speed, fly_speed, darkvision, resistance, bonuses, languages):
        self.name = name
        self.abilities = abilities
        self.alignment = alignment
        self.creature_type = creature_type
        self.size = size
        self.walk_speed = walk_speed
        self.fly_speed = fly_speed
        self.darkvision = darkvision
        self.resistance = resistance
        self.bonuses = bonuses
        self.languages = languages

Aasimar_Protector = Race(
    "Aasimar - Protector", 
    {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     2,
    },
    ["Chaotic Good", "Neutral Good", "Lawful Good"],
    "Humanoid",
    "Medium",
    30,
    None,
    True,
    ["Necrotic", "Radiant"],
    ["Healing Hands", "Light Bearer"],
    ["Common", "Celestial"]
)
Aasimar_Scourge = Race(
    "Aasimar - Scourge", 
    {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 1,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     2,
    },
    ["Chaotic Good", "Neutral Good", "Lawful Good"],
    "Humanoid",
    "Medium",
    30,
    None,
    True,
    ["Necrotic", "Radiant"],
    ["Healing Hands", "Light Bearer"],
    ["Common", "Celestial"]
)
Aasimar_Fallen = Race(
    "Aasimar - Fallen", 
    {
        "Strength":     1,
        "Dexterity":    0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     2,
    },
    ["Chaotic Evil", "Neutral Evil", "Lawful Evil"],
    "Humanoid",
    "Medium",
    30,
    None,
    True,
    ["Necrotic", "Radiant"],
    ["Healing Hands", "Light Bearer"],
    ["Common", "Celestial"]
)
Animal_Hybrid = Race(
    "Animal Hybrid",
    {
        "Strength":     0,
        "Dexterity":    0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    },
    None,
    "Humanoid",
    "Medium",
    30,
    None,
    True,
    None,
    ["Manta Glide", "Nimble Climber", "Underwater Adaptation"],
    ["Common", "Elven or Vedalken"]
)
Birdfolk = Race(
    "Birdfolk",
    {
        "Strength":     0,
        "Dexterity":    2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       1,
        "Charisma":     0,
    },
    ["Lawful Good", "Chaotic Good"],
    "Humanoid",
    "Medium",
    25,
    50,
    False,
    None,
    "Talons",
    ["Common", "Aarakocra", "Auran"]
)
Bugbear = Race(
    "Bugbear",
    {
        "Strength":     2,
        "Dexterity":    1,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    },
    ["Chaotic Evil"],
    ["Humanoid", "Goblinoid"],
    "Medium",
    30,
    None,
    True,
    None,
    ["Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack"],
    ["Common", "Goblin"]
)
Centaur = Race(
    "Centaur",
    {
        "Strength":     2,
        "Dexterity":    1,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom":       0,
        "Charisma":     0,
    },
    ["Lawful Neutral", "Neutral Neutral", "Chaotic Neutral"],
    "Fey",
    "Medium",
    40,
    None,
    False,
    None,
    ["Charge", "Hooves", "Equine Build", "Survivor"],
    ["Common", "Sylvan"]
)

RACES = [
    
]