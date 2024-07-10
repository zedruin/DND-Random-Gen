class Weapon():
    def __init__(self, name, damage, damage_type, distance, weight, properties, melee = True):
        self.name = name
        self.damage = damage
        self.damage_type = damage_type
        self.distance = distance
        self.weight = weight
        self.properties = properties
        self.melee = melee

# Simple - Melee
Club = Weapon(
    "Club",
    (1, 4),
    "bludgeoning", 
    None,
    2,
    ["Light"]
)
Dagger = Weapon(
    "Dagger",
    (1, 4),
    "piercing",
    [20, 60],
    1,
    ["Finesse", "Light", "Thrown - Range 20/60"]
)
Greatclub = Weapon(
    "Greatclub",
    (1, 8),
    "bludgeoning",
    None,
    10,
    ["Two-Handed"]
)
Handaxe = Weapon(
    "Handaxe",
    (1, 6),
    "slashing",
    [20, 60],
    2,
    ["Light", "Thrown - Range 20/60"]
)
Javelin = Weapon(
    "Javelin",
    (1, 6),
    "piercing",
    [30, 120],
    2,
    ["Thrown - Range 30/120"]
)
Light_Hammer = Weapon(
    "Light Hammer",
    (1, 4),
    "bludgeoning",
    [20, 60],
    2,
    ["Light", "Thrown - Range 20/60"]
)
Mace = Weapon(
    "Mace",
    (1, 6),
    "bludgeoning",
    None,
    4,
    None
)
Quarterstaff = Weapon(
    "Quarterstaff",
    (1, 6),
    "bludgeoning",
    None,
    4,
    ["Versatile - 1d8"]
)
Sickle = Weapon(
    "Sickle",
    (1, 4),
    "slashing",
    None,
    2,
    ["Light"]
)
Spear = Weapon(
    "Spear",
    (1, 6),
    "piercing",
    [20, 60],
    3,
    ["Thrown - Range 20/60", "Versatile - 1d8"]
)

# Simple - Ranged
Light_Crossbow = Weapon(
    "Light Crossbow",
    (1, 8),
    "piercing",
    [80, 320],
    5, 
    ["Ammunition - Range 80/320", "Loading", "Two-Handed"],
    melee= False
)
Dart = Weapon(
    "Dart",
    (1, 4),
    "piercing",
    [20, 60],
    0.25,
    ["Finesse", "Thrown - Range 20/60"],
    melee= False
)
Shortbow = Weapon(
    "Shortbow",
    (1, 6),
    "piercing",
    [80, 320],
    2,
    ["Ammunition - Range 80/320", "Two-Handed"],
    melee= False
)
Sling = Weapon(
    "Sling",
    (1, 4),
    "bludgeoning",
    [30, 120],
    0,
    ["Ammunition - Range 30/120"]
)

# Martial - Melee
Battleaxe = Weapon(
    "Battleaxe",
    (1, 8),
    "slashing",
    None,
    4,
    ["Versatile - 1d10"]
)
Flail = Weapon(
    "Flail",
    (1, 8),
    "bludgeoning",
    None,
    2,
    None
)
Glaive = Weapon(
    "Glaive",
    (1, 10),
    "slashing",
    None,
    6,
    ["Heavy", "Reach", "Two-Handed"]
)
Greataxe = Weapon(
    "Greataxe",
    (1, 12),
    "slashing",
    None,
    7,
    ["Heavy", "Two-Handed"]
)
Greatsword = Weapon(
    "Greatsword",
    (2, 6),
    "slashing",
    None,
    6,
    ["Heavy", "Two-Handed"]
)
Halberd = Weapon(
    "Halberd",
    (1, 10),
    "slashing",
    None,
    6,
    ["Heavy", "Reach", "Two-Handed"]
)
Lance = Weapon(
    "Lance",
    (1, 12),
    "piercing",
    None,
    6,
    ["Reach", "Special - Lance"]
)
Longsword = Weapon(
    "Longsword",
    (1, 8),
    "slashing",
    None,
    3,
    ["Versatile - 1d10"]
)
Maul = Weapon(
    "Maul", 
    (2, 6),
    "bludgeoning",
    None,
    10,
    ["Heavy", "Two-Handed"]
)
Morningstar = Weapon(
    "Morningstar",
    (1, 8),
    "piercing",
    None,
    4,
    None
)
Pike = Weapon(
    "Pike",
    (1, 10),
    "piercing",
    None,
    18,
    ["Heavy", "Reach", "Two-Handed"]

)
Rapier = Weapon(
    "Rapier",
    (1, 8),
    "piercing",
    None,
    2,
    ["Finesse"]
)
Scimitar = Weapon(
    "Scimitar",
    (1, 6),
    "slashing",
    None,
    3,
    ["Finesse", "Light"]
)
Shortsword = Weapon(
    "Shortsword",
    (1, 6),
    "piercing",
    None,
    2,
    ["Finesse", "Light"]
)
Trident = Weapon(
    "Trident",
    (1, 6),
    "piercing",
    [20, 60],
    4,
    ["Thrown - Range 20/60", "Versatile - 1d8"]
)
War_Pick = Weapon(
    "War Pick",
    (1, 8),
    "piercing",
    None,
    2,
    None
)
Warhammer = Weapon(
    "Warhammer",
    (1, 8),
    "bludgeoning",
    None,
    2,
    ["Versatile - 1d10"]
)
Whip = Weapon(
    "Whip",
    (1, 4),
    "slashing",
    None,
    3,
    ["Finesse", "Reach"]
)

# Martial - Ranged
Blowgun = Weapon(
    "Blowgun",
    1,
    "piercing",
    [25, 100],
    1,
    ["Ammunition - Range 25/100", "Loading"],
    melee= False
)
Hand_Crossbow = Weapon(
    "Hand Crossbow",
    (1, 6),
    "piercing", 
    [30, 120],
    3,
    ["Ammunition - Range 30/120", "Light", "Loading"],
    melee= False
)
Heavy_Crossbow = Weapon(
    "Heavy Crossbow", 
    (1, 10), 
    "piercing", 
    [100, 400],
    18,
    ["Ammunition - Range 100/400", "Heavy", "Loading", "Two-Handed"],
    melee= False
)
Longbow = Weapon(
    "Longbow",
    (1, 8),
    "piercing",
    [150, 600],
    2,
    ["Ammunition - Range 120/600", "Heavy", "Two-Handed"]
)
Net = Weapon(
    "Net",
    None,
    None,
    [5, 15],
    3,
    ["Thrown - Range 5/15", "Special - Net"]
)

Simple_Melee = [
    Club,
    Dagger,
    Greatclub,
    Handaxe,
    Javelin,
    Light_Hammer,
    Mace,
    Quarterstaff,
    Sickle,
    Spear
]
Simple_Ranged = [
    Light_Crossbow,
    Dart,
    Shortbow,
    Sling
]
Martial_Melee = [
    Battleaxe,
    Flail,
    Glaive,
    Greataxe,
    Greatsword,
    Halberd,
    Lance,
    Maul,
    Morningstar,
    Pike,
    Rapier,
    Scimitar,
    Shortsword,
    Trident,
    War_Pick,
    Whip
]
Martial_Ranged = [
    Blowgun,
    Hand_Crossbow,
    Heavy_Crossbow,
    Longbow,
    Net,
]
Simple = [j for i in [Simple_Melee, Simple_Ranged] for j in i]
Martial = [j for i in [Martial_Melee, Martial_Ranged] for j in i]
Ranged = [j for i in [Simple_Ranged, Martial_Ranged] for j in i]