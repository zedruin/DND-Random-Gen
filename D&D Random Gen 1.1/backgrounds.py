class Background():
    def __init__(self, name, skills, tools, languages, equipment, gp, features_1, features_1_details, features_2, features_2_details, traits, ideals, bonds, flaws):
        self.name = name
        self.skills - skills
        self.tools = tools
        self.languages = languages
        self.equipment = equipment
        self.gp = gp
        self.features_1 = features_1
        self.features_1_details = features_1_details
        self.features_2 = features_2
        self.features_2_details = features_2_details
        self.traits = traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws

Acolyte = Background(
    "Acolyte",
    ["Insight", "Religion"],
    None,
    "Two of your Choice",
    [ # Equipment
        "A Holy Symbol", 
        "A Prayer Book or Prayer Wheel", 
        "5 Sticks of incense", 
        "Vestments", 
        "Set of Common Clothes", 
        "Pouch"
    ],
    15,
    None,
    None,
    "Shelter of the Faithful",
    "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. \nYou and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. \nThose who share your religion will support you (but only you) at a modest lifestyle. \nYou might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. \nThis could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. \nWhile near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.",
    [ # Traits #
        "I idolize a particular hero of my faith, and constantly refer to that person's deeds and example.",
        "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
        "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
        "Nothing can shake my optimistic attitude.",
        "I quote (or misquote) sacred texts and proverbs in almost every situation.",
        "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
        "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
        "I've spent so long in the temple that I have little practical experience dealing with people in the outside world."
    ],
    [ # Ideals #
        "Tradition - The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)",
        "Charity - I always try to help those in need, no matter what the personal cost. (Good)",
        "Change - We must help bring about the changes the gods are constantly working in the world. (Chaotic)",
        "Power - I hope to one day rise to the top of my faith's religious hierarchy. (Lawful)",
        "Faith - I trust that my deity will guide my actions. I have faith that if I work hard, things will go well. (Lawful)",
        "Aspiration - I seek to prove myself worthy of my god's favor by matching my actions against their teachings. (Any)"
    ],
    [ # Bonds #
        "I would die to recover an ancient relic of my faith that was lost long ago.",
        "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        "I owe my life to the priest who took me in when my parents died.",
        "Everything I do is for the common people.",
        "I will do anything to protect the temple where I served.",
        "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy."
    ],
    [ # Flaws #
        "I judge others harshly, and myself even more severely.",
        "I put too much trust in those who wield power within my temple's hierarchy.",
        "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "I am inflexible in my thinking.",
        "I am suspicious of strangers and expect the worst of them.",
        "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
    ]
)
Athlete = Background(
    "Athlete",
    ["Acrobatics", "Athletics"],
    ["Vehicles - Land"],
    "One of your choice",
    [ # Equipment
        "A Bronze Discus or Leather Ball",
        "A Lucky Charm or Past Trophy",
        "A Set of Traveler's Clothes",
        "Pouch"
    ],
    10,
    "Favored Event",
    [ # Roll or choose from the options in the Favored Events table to determine the athletic event in which you excel. #
        "Marathon",
        "Long-distance running",
        "Wrestling",
        "Boxing",
        "Chariot or horse race",
        "Pankration (mixed unarmed combat)",
        "Hoplite race (racing in full armor with a unit)",
        "Pentathlon (running, long jump, discus, javelin, wrestling)"
    ],
    "Echoes of Victory",
    "You have attracted admiration among spectators, fellow athletes, and trainers in the region that hosted your past athletic victories. \nWhen visiting any settlement within 100 miles of where you grew up, there is a 50 percent chance you can find someone there who admires you and is willing to provide information and temporary shelter. \nBetween adventures, you might compete in athletic events sufficient enough to maintain a comfortable lifestyle, as per the 'Practicing a Profession' downtime activity in chapter 8 of the Players Handbook.",
    [ # Traits #
        "I feel most at peace during physical exertion, whether exercise or battle.",
        "I don't like to sit idle.",
        "I have a daily exercise routine I refuse to break.",
        "Obstacles exist to be overcome.",
        "When I see others struggling, I offer to help.",
        "I love to trade banter and gibes.",
        "Anything worth doing is worth doing best.",
        "I get irritated if people praise someone else and not me."
    ],
    [ # Ideals #
        "Competition - I strive to test myself in all things. (Chaotic)",
        "Triumph - The best part of winning is seeing my rivals brought low. (Evil)",
        "Camaraderie - The strongest bonds are forged through struggle. (Good)",
        "People - I strive to inspire my spectators. (Neutral)",
        "Tradition - Every game has rules, and the playing field must be level. (Lawful)",
        "Growth - Lessons hide in victory and defeat. (Any)"
    ],
    [ # Bonds #
        "My teammates are my family.",
        "I will overcome a rival and prove myself their better.",
        "My mistake got someone hurt. Ill never make that mistake again.",
        "I will be the best for the honor and glory of my home.",
        "The person who trained me is the most important person in my world.",
        "I strive to live up to a specific hero's example."
    ],
    [ # Flaws #
        "I indulge in a habit that threatens my reputation or health.",
        "I'll do absolutely anything to win.",
        "I ignore anyone who doesn't compete and anyone who loses to me.",
        "I have lingering pain of old injuries.",
        "Any defeat or failure on my part is because my opponents cheated.",
        "I must be the captain of any group I join."
    ]
)
Charlatan = Background(
    "Charlatan",
    ["Deception", "Sleight of Hand"],
    ["Disguise Kit", "Forgery Kit"],
    "None",
    [ # Equipment #
        "A Set of Fine Clothes",
        "A Disguise Kit",
        "Tools of the Con of your choice: (10 stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke)",
        "Pouch"
    ],
    15,
    "Favorite Schemes",
    [ # Every charlatan has an angle they use in preference to other schemes. Choose a favorite scam or roll on the table below. #
        "I cheat at games of chance.",
        "I shave coins or forge documents.",
        "I insinuate myself into people's lives to prey on their weakness and secure their fortunes.",
        "I put on new identities like clothes.",
        "I run sleight-of-hand cons on street corners.",
        "I convince people that worthless junk is worth their hard-earned money."
    ],
    "False Identity",
    "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy.",
    [ # Traits #
        "I fall in and out of love easily, and am always pursuing someone.",
        "I have a joke for every occasion, especially occasions where humor is inappropriate.",
        "Flattery is my preferred trick for getting what I want.",
        "I'm a born gambler who can't resist taking a risk for a potential payoff.",
        "I lie about almost everything, even when there's no good reason to.",
        "Sarcasm and insults are my weapons of choice.",
        "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        "I pocket anything I see that might have some value."
    ],
    [ # Ideals #
        "Independence - I am a free spirit, no one tells me what to do. (Chaotic)",
        "Fairness - I never target people who can't afford to lose a few coins. (Lawful)",
        "Charity - I distribute the money I acquire to the people who really need it. (Good)",
        "Creativity - I never run the same con twice. (Chaotic)",
        "Friendship - Material goods come and go. Bonds of friendship last forever. (Good)",
        "Aspiration - I'm determined to make something of myself. (Any)"
    ],
    [ # Bonds #
        "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
        "I owe everything to my mentor; a horrible person who's probably rotting in jail somewhere.",
        "Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her.",
        "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
        "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
        "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able to forgive myself."
    ],
    [ # Flaws #
        "I can't resist a pretty face.",
        "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        "I'm convinced that no one could ever fool me the way I fool others.",
        "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
        "I can't resist swindling people who are more powerful than me.",
        "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough."
    ],
)
City_Watch = Background(
    "City Watch",
    ["Athletics", "Insight"],
    "None",
    ["Two of your Choice"],
    [ # Equipment #
        "A uniform in the style of your unit and indicative of your rank",
        "A Horn with which to summon help",
        "A set of Manacles",
        "Pouch"
    ],
    10,
    "Variant - Investigator",
    "Rarer than watch or patrol members are a community's investigators, who are responsible for solving crimes after the fact. \nThough such folk are seldom found in rural areas, nearly every settlement of decent size has at least one or two watch members who have the skill to investigate crime scenes and track down criminals. \nIf your prior experience is as an investigator, you have proficiency in Investigation rather than Athletics.",
    "Watcher's Eye",
    "Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. \nYou can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter.",
    [ # Traits # 
        "I'm always polite and respectful.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "I can stare down a hell hound without flinching.",
        "I enjoy being strong and like breaking things.",
        "I have a crude sense of humor.",
        "I face problems head-on. A simple, direct solution is the best path to success."
    ],
    [ # Ideals # 
        "Greater Good -  Our lot is to lay down our lives in defense of others. (Good)",
        "Responsibility - I do what I must and obey just authority. (Lawful)",
        "Independence - When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)",
        "Might - In life as in war, the stronger force wins. (Evil)",
        "Live and Let Live - Ideals aren't worth killing over or going to war for. (Neutral)",
        "Nation - My city, nation, or people are all that matter. (Any)"
    ],
    [ # Bonds #
        "I would still lay down my life for the people I served with.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "My honor is my life.",
        "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
        "Those who fight beside me are those worth dying for.",
        "I fight for those who cannot fight for themselves."
    ],
    [ # Flaws #
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I have little respect for anyone who is not a proven warrior.",
        "I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret.",
        "My hatred of my enemies is blind and unreasoning.",
        "I obey the law, even if the law causes misery.",
        "I'd rather eat my armor than admit when I'm wrong."
    ]
)
Clan_Crafter = Background(
    
)
Cloistered_Scholar = Background(
    
)
Courtier = Background(
    
)
Criminal = Background(
    
)
Custom = Background(
    
)
Entertainer = Background(
    
)
Faction_Agent = Background(
    
)
Far_Traveler = Background(
    
)
Fey_Lost = Background(
    
)
Fisher = Background(
    
)
Folk_Hero = Background(
    
)
Guild_Artisan = Background(
    
)
Haunted_One = Background(
    
)
Hermit = Background(
    
)
House_Agent = Background(
    
)
Inheritor = Background(
    
)
Investigator = Background(
    
)
Knight = Background(
    
)
Marine = Background(
    
)
Mercenary_Veteran = Background(
    
)
Noble = Background(
    
)
Outlander = Background(
    
)
Port_City_Noble = Background(
    
)
Sage = Background(
    
)
Sailor = Background(
    
)
Shipwright = Background(
    
)
Smuggler = Background(
    
)
Soldier = Background(
    
    [ # Traits # 
        "I'm always polite and respectful.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "I can stare down a hell hound without flinching.",
        "I enjoy being strong and like breaking things.",
        "I have a crude sense of humor.",
        "I face problems head-on. A simple, direct solution is the best path to success."
    ],
    [ # Ideals # 
        "Greater Good -  Our lot is to lay down our lives in defense of others. (Good)",
        "Responsibility - I do what I must and obey just authority. (Lawful)",
        "Independence - When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)",
        "Might - In life as in war, the stronger force wins. (Evil)",
        "Live and Let Live - Ideals aren't worth killing over or going to war for. (Neutral)",
        "Nation - My city, nation, or people are all that matter. (Any)"
    ],
    [ # Bonds #
        "I would still lay down my life for the people I served with.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "My honor is my life.",
        "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
        "Those who fight beside me are those worth dying for.",
        "I fight for those who cannot fight for themselves."
    ],
    [ # Flaws #
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I have little respect for anyone who is not a proven warrior.",
        "I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret.",
        "My hatred of my enemies is blind and unreasoning.",
        "I obey the law, even if the law causes misery.",
        "I'd rather eat my armor than admit when I'm wrong."
    ]
)
Urban_Bounty_Hunter = Background(
    
)
Urchin = Background(
    
)
Violent_Assassin = Background(
    
)
Witch_Carnival_Hand = Background(
    
)
