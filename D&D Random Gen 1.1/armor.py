class Armor():
    def __init__(self, name, AC, strength, stealth_dis, weight):
        self.name = name
        self.AC = AC
        self.strength = strength
        self.stealth_dis = stealth_dis
        self.weight = weight

# Light
Padded = Armor(
    "Padded",
    11,
    None,
    True,
    8
)
Leather = Armor(
    "Leather",
    11,
    None,
    None,
    10
)
Studded_Leather = Armor(
    "Studded Leather",
    12,
    None,
    None,
    13
)

# Medium
Hide = Armor(
    "Hide",
    12,
    None,
    None,
    12
)
Chain_Shirt = Armor(
    "Chain Shirt",
    13,
    None,
    None,
    20
)
Scale_Mail = Armor(
    "Scale Mail",
    14,
    None,
    True,
    45
)
Spiked_Armor = Armor(
    "Spiked Armor",
    14,
    None,
    True,
    45
)
Breastplate = Armor(
    "Breastplate",
    14,
    None,
    None,
    20
)
Halfplate = Armor(
    "Halfplate",
    15,
    None,
    True,
    40
)

# Heavy
Ring_Mail = Armor(
    "Ring Mail",
    14,
    None,
    True,
    40
)
Chain_Mail = Armor(
    "Chain Mail",
    16,
    13,
    True,
    55
)
Splint = Armor(
    "Splint",
    17,
    15,
    True,
    60
)
Plate = Armor(
    "Plate",
    18,
    15,
    True,
    65
)

# Shield
Shield = Armor(
    "Shield",
    2,
    None,
    None,
    6
)

Light_Armor = [
    Padded, 
    Leather, 
    Studded_Leather
]
Medium_Armor = [
    Hide, 
    Chain_Shirt, 
    Spiked_Armor, 
    Scale_Mail, 
    Breastplate, 
    Halfplate
]
Heavy_Armor = [
    Ring_Mail, 
    Chain_Mail, 
    Splint, 
    Plate
]
Shield = [Shield]
Armors = [j for i in [Light_Armor, Medium_Armor, Heavy_Armor] for j in i]