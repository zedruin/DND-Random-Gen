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
    ["light"]
)