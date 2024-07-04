import webbrowser
import random
import tkinter as tk
from tkinter import font

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

urls = {
    "spells_c": {
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
    },
    "spells_f": {
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
    "Guiding Hands": "http://dnd5e.wikidot.com/spell:guiding-hand-ua",
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

def open_url(url):
    webbrowser.open_new(url)
##### Generate Spells #####

# Cleric - 3 cantrips - Wisdom + Cleric Level (1)
def generate_cleric_cantrip():
    clerics_cantrip = random.choice(cleric_cantrip)
    return clerics_cantrip
def generate_cleric_first():
    clerics_first = random.choice(cleric_first)
    return clerics_first

# Druid - 2 cantrips - Wisdom + Druid Level (1)
def generate_druid_cantrip():
    druids_cantrip = random.choice(druid_cantrip)
    return druids_cantrip
def generate_druid_first():
    druids_first = random.choice(druid_first)
    return druids_first

# Warlock - 1 cantrips + Eldritch Blast - 2 first level
def generate_warlock_cantrip():
    warlocks_cantrip = random.choice(warlock_cantrip)
    return f"Eldritch Blast", warlocks_cantrip
def generate_warlock_first():
    warlocks_first = random.choice(warlock_first)
    return warlocks_first

# Wizard - 3 cantrips - Intelligence + Wizard Level (1)
def generate_wizard_cantrip():
    wizards_cantrip = random.choice(wizard_cantrip)
    return wizards_cantrip
def generate_wizard_first():
    wizards_first = random.choice(wizard_first)
    return wizards_first

##### ######

def generate_spells(selection):
    if selection == "Artificer": # 2 Cantrips - 2 First #
        a_c_1, a_c_2 = random.sample(artificer_cantrip, 2)
        a_f_1, a_f_2 = random.sample(artificer_first, 2)
        
        details_text.config(state=tk.NORMAL)
        details_text.delete(1.0, tk.END)
        details_text.insert(tk.END, "\nArtificiers have 2 Cantrips and 2 First Level Spells ")

        details_text.insert(tk.END, "\n\nArtificer Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, a_c_1, ("a_c_1", a_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, a_c_2, ("a_c_2", a_c_2))

        details_text.insert(tk.END, "\n\nArtificer First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spells: ")
        details_text.insert(tk.END, a_f_1, ("a_f_1", a_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, a_f_2, ("a_f_2", a_f_2))

        details_text.tag_configure("a_c_1", foreground="blue", underline=True)
        details_text.tag_bind("a_c_1", "<Button-1>", lambda e: open_url(urls["spells_c"][a_c_1]))
        details_text.tag_configure("a_c_2", foreground="blue", underline=True)
        details_text.tag_bind("a_c_2", "<Button-1>", lambda e: open_url(urls["spells_c"][a_c_2]))

        details_text.tag_configure("a_f_1", foreground="blue", underline=True)
        details_text.tag_bind("a_f_1", "<Button-1>", lambda e: open_url(urls["spells_f"][a_f_1]))
        details_text.tag_configure("a_f_2", foreground="blue", underline=True)
        details_text.tag_bind("a_f_2", "<Button-1>", lambda e: open_url(urls["spells_f"][a_f_2]))

        details_text.config(state=tk.DISABLED)
        
    elif selection == "Bard": # 2 Cantrips - 4 First #
        b_c_1, b_c_2 = random.sample(bard_cantrip, 2)
        b_f_1, b_f_2, b_f_3, b_f_4 = random.sample(bard_first, 4)

        details_text.config(state=tk.NORMAL)
        details_text.delete(1.0, tk.END)
        
        details_text.insert(tk.END, "\nBards have 2 Cantrips and 4 First Level Spells: ")

        details_text.insert(tk.END, "\n\nBard Cantrips: ")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, b_c_1, ("b_c_1", b_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, b_c_2, ("b_c_2", b_c_2))
        
        details_text.insert(tk.END, "\n\nBard First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, b_f_1, ("b_f_1", b_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, b_f_2, ("b_f_2", b_f_2))
        details_text.insert(tk.END, "\n    3rd Spell: ")
        details_text.insert(tk.END, b_f_3, ("b_f_3", b_f_3))
        details_text.insert(tk.END, "\n    4th Spell: ")
        details_text.insert(tk.END, b_f_4, ("b_f_4", b_f_4))

        details_text.tag_configure("b_c_1", foreground="blue", underline=True)
        details_text.tag_bind("b_c_1", "<Button-1>", lambda e: open_url(urls["spells_c"][b_c_1]))
        details_text.tag_configure("b_c_2", foreground="blue", underline=True)
        details_text.tag_bind("b_c_2", "<Button-1>", lambda e: open_url(urls["spells_c"][b_c_2]))
        details_text.tag_configure("b_f_1", foreground="blue", underline=True)
        details_text.tag_bind("b_f_1", "<Button-1>", lambda e: open_url(urls["spells_f"][b_f_1]))
        details_text.tag_configure("b_f_2", foreground="blue", underline=True)
        details_text.tag_bind("b_f_2", "<Button-1>", lambda e: open_url(urls["spells_f"][b_f_2]))
        details_text.tag_configure("b_f_3", foreground="blue", underline=True)
        details_text.tag_bind("b_f_3", "<Button-1>", lambda e: open_url(urls["spells_f"][b_f_3]))
        details_text.tag_configure("b_f_4", foreground="blue", underline=True)
        details_text.tag_bind("b_f_4", "<Button-1>", lambda e: open_url(urls["spells_f"][b_f_4]))

        details_text.config(state=tk.DISABLED)
    
    elif selection == "Cleric": # 3 Cantrips - WIS+LVL First #
        cleric_c_1 = generate_cleric_cantrip()
        cleric_c_2 = generate_cleric_cantrip()
        cleric_c_3 = generate_cleric_cantrip()
        cleric_f_1 = generate_cleric_first()
        cleric_f_2_1 = generate_cleric_first()
        cleric_f_2_2 = generate_cleric_first()
        cleric_f_3_1 = generate_cleric_first()
        cleric_f_3_2 = generate_cleric_first()
        cleric_f_3_3 = generate_cleric_first()
        cleric_f_4_1 = generate_cleric_first()
        cleric_f_4_2 = generate_cleric_first()
        cleric_f_4_3 = generate_cleric_first()
        cleric_f_4_4 = generate_cleric_first()
        cleric_f_5_1 = generate_cleric_first()
        cleric_f_5_2 = generate_cleric_first()
        cleric_f_5_3 = generate_cleric_first()
        cleric_f_5_4 = generate_cleric_first()
        cleric_f_5_5 = generate_cleric_first()
        cleric_f_6_1 = generate_cleric_first()
        cleric_f_6_2 = generate_cleric_first()
        cleric_f_6_3 = generate_cleric_first()
        cleric_f_6_4 = generate_cleric_first()
        cleric_f_6_5 = generate_cleric_first()
        cleric_f_6_6 = generate_cleric_first()
        
        details_text.config(state=tk.NORMAL)
        details_text.delete(1.0, tk.END)
        details_text.insert(tk.END, "\nClerics have 3 Cantrips: ")
        details_text.insert(tk.END, "\nCantrip #1: ")
        details_text.insert(tk.END, cleric_c_1, ("cantrip_1", cleric_c_1))
        details_text.insert(tk.END, "\nCantrip #2: ")
        details_text.insert(tk.END, cleric_c_2, ("cantrip_2", cleric_c_2))
        details_text.insert(tk.END, "\nCantrip #3: ")
        details_text.insert(tk.END, cleric_c_3, ("cantrip_3", cleric_c_3))

        details_text.insert(tk.END, "\n\nClerics have 'WIS + Cleric LVL' First Level Spells:")
        details_text.insert(tk.END, "\nWisdom 1-11: 1 spell ")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_1, ("spells_1", cleric_f_1))
        details_text.insert(tk.END, "\nWisdom 12-13: 2 spells ")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_2_1, ("spells_2_1", cleric_f_2_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, cleric_f_2_2, ("spells_2_2", cleric_f_2_2))
        details_text.insert(tk.END, "\nWisdom 14-15: 3 spells ")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_3_1, ("spells_3_1", cleric_f_3_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, cleric_f_3_2, ("spells_3_2", cleric_f_3_2))
        details_text.insert(tk.END, "\n    3rd Spell: ")
        details_text.insert(tk.END, cleric_f_3_3, ("spells_3_3", cleric_f_3_3))
        details_text.insert(tk.END, "\nWisdom 16-17: 4 spells")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_4_1, ("spells_4_1", cleric_f_4_1))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_4_2, ("spells_4_2", cleric_f_4_2))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_4_3, ("spells_4_3", cleric_f_4_3))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_4_4, ("spells_4_4", cleric_f_4_4))
        details_text.insert(tk.END, "\nWisdom 18-19: 5 spells")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_5_1, ("spells_5_1", cleric_f_5_1))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_5_2, ("spells_5_2", cleric_f_5_2))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_5_3, ("spells_5_3", cleric_f_5_3))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_5_4, ("spells_5_4", cleric_f_5_4))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_5_5, ("spells_5_5", cleric_f_5_5))
        details_text.insert(tk.END, "\nWisdom 20: 6 spells")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_6_1, ("spells_6_1", cleric_f_6_1))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_6_2, ("spells_6_2", cleric_f_6_2))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_6_3, ("spells_6_3", cleric_f_6_3))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_6_4, ("spells_6_4", cleric_f_6_4))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_6_5, ("spells_6_5", cleric_f_6_5))
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, cleric_f_6_6, ("spells_6_6", cleric_f_6_6))

        details_text.tag_configure("cantrip_1", foreground="blue", underline=True)
        details_text.tag_bind("cantrip_1", "<Button-1>", lambda e: open_url(urls["spells_c"][cleric_c_1]))
        details_text.tag_configure("cantrip_2", foreground="blue", underline=True)
        details_text.tag_bind("cantrip_2", "<Button-1>", lambda e: open_url(urls["spells_c"][cleric_c_2]))
        details_text.tag_configure("cantrip_3", foreground="blue", underline=True)
        details_text.tag_bind("cantrip_3", "<Button-1>", lambda e: open_url(urls["spells_c"][cleric_c_3]))
        details_text.tag_configure("spells_1", foreground="blue", underline=True)
        details_text.tag_bind("spells_1", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_1]))
        details_text.tag_configure("spells_2_1", foreground="blue", underline=True)
        details_text.tag_bind("spells_2_1", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_2_1]))
        details_text.tag_configure("spells_2_2", foreground="blue", underline=True)
        details_text.tag_bind("spells_2_2", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_2_2]))
        details_text.tag_configure("spells_3_1", foreground="blue", underline=True)
        details_text.tag_bind("spells_3_1", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_3_1]))
        details_text.tag_configure("spells_3_2", foreground="blue", underline=True)
        details_text.tag_bind("spells_3_2", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_3_2]))
        details_text.tag_configure("spells_3_3", foreground="blue", underline=True)
        details_text.tag_bind("spells_3_3", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_3_3]))
        details_text.tag_configure("spells_4_1", foreground="blue", underline=True)
        details_text.tag_bind("spells_4_1", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_4_1]))
        details_text.tag_configure("spells_4_2", foreground="blue", underline=True)
        details_text.tag_bind("spells_4_2", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_4_2]))
        details_text.tag_configure("spells_4_3", foreground="blue", underline=True)
        details_text.tag_bind("spells_4_3", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_4_3]))
        details_text.tag_configure("spells_4_4", foreground="blue", underline=True)
        details_text.tag_bind("spells_4_4", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_4_4]))
        details_text.tag_configure("spells_5_1", foreground="blue", underline=True)
        details_text.tag_bind("spells_5_1", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_5_1]))
        details_text.tag_configure("spells_5_2", foreground="blue", underline=True)
        details_text.tag_bind("spells_5_2", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_5_2]))
        details_text.tag_configure("spells_5_3", foreground="blue", underline=True)
        details_text.tag_bind("spells_5_3", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_5_3]))
        details_text.tag_configure("spells_5_4", foreground="blue", underline=True)
        details_text.tag_bind("spells_5_4", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_5_4]))
        details_text.tag_configure("spells_5_5", foreground="blue", underline=True)
        details_text.tag_bind("spells_5_5", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_5_5]))
        details_text.tag_configure("spells_6_1", foreground="blue", underline=True)
        details_text.tag_bind("spells_6_1", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_6_1]))
        details_text.tag_configure("spells_6_2", foreground="blue", underline=True)
        details_text.tag_bind("spells_6_2", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_6_2]))
        details_text.tag_configure("spells_6_3", foreground="blue", underline=True)
        details_text.tag_bind("spells_6_3", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_6_3]))
        details_text.tag_configure("spells_6_4", foreground="blue", underline=True)
        details_text.tag_bind("spells_6_4", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_6_4]))
        details_text.tag_configure("spells_6_5", foreground="blue", underline=True)
        details_text.tag_bind("spells_6_5", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_6_5]))
        details_text.tag_configure("spells_6_6", foreground="blue", underline=True)
        details_text.tag_bind("spells_6_6", "<Button-1>", lambda e: open_url(urls["spells_f"][cleric_f_6_6]))
        

        details_text.config(state=tk.DISABLED)

    elif selection == "Druid": # 2 Cantrips - WIS+LVL First #
        druid_c = generate_druid_cantrip()
        druid_f = generate_druid_first()
        druid_f2 = generate_druid_first()
        druid_f3 = generate_druid_first()
        druid_f4 = generate_druid_first()
        druid_f5 = generate_druid_first()
        druid_f6 = generate_druid_first()
        result = f"\nDruid Cantrips: {druid_c}\n\nDruid First Level - Wisdom 1-11: {druid_f}\n\nDruid First Level - Wisdom 12-13: {druid_f2}\n\nDruid First Level - Wisdom 14-15: {druid_f3}\n\nDruid First Level - Wisdom 16-17: {druid_f4}\n\nDruid First Level - Wisdom 18-19: {druid_f5}\n\nDruid First Level - Wisdom 20: {druid_f6}\n"
        result_var.set(result)
        return result_var
    
    elif selection == "Sorcerer": # 4 Cantrips - 2 First #
        s_c_1, s_c_2, s_c_3, s_c_4 = random.sample(sorcerer_cantrip, 4)
        s_f_1, s_f_2 = random.sample(sorcerer_first, 2)

        details_text.config(state=tk.NORMAL)
        details_text.delete(1.0, tk.END)

        details_text.insert(tk.END, "\nSorcerers have 4 Cantrips and 2 First Level Spells")

        details_text.insert(tk.END, "\n\nSorcerer Cantrips:")
        details_text.insert(tk.END, "\n    1st Cantrip: ")
        details_text.insert(tk.END, s_c_1, ("s_c_1", s_c_1))
        details_text.insert(tk.END, "\n    2nd Cantrip: ")
        details_text.insert(tk.END, s_c_2, ("s_can_2", s_c_2))
        details_text.insert(tk.END, "\n    3rd Cantrip: ")
        details_text.insert(tk.END, s_c_3, ("s_can_3", s_c_3))
        details_text.insert(tk.END, "\n    4th Cantrip: ")
        details_text.insert(tk.END, s_c_4, ("s_can_4", s_c_4))
        
        details_text.insert(tk.END, "\n\nSorcerer First Level Spells:")
        details_text.insert(tk.END, "\n    1st Spell: ")
        details_text.insert(tk.END, s_f_1, ("s_first_1", s_f_1))
        details_text.insert(tk.END, "\n    2nd Spell: ")
        details_text.insert(tk.END, s_f_2, ("s_first_2", s_f_2))

        details_text.tag_configure("s_c_1", foreground="blue", underline=True)
        details_text.tag_bind("s_c_1", "<Button-1>", lambda e: open_url(urls["spells_c"][s_c_1]))
        details_text.tag_configure("s_can_2", foreground="blue", underline=True)
        details_text.tag_bind("s_can_2", "<Button-1>", lambda e: open_url(urls["spells_c"][s_c_2]))
        details_text.tag_configure("s_can_3", foreground="blue", underline=True)
        details_text.tag_bind("s_can_3", "<Button-1>", lambda e: open_url(urls["spells_c"][s_c_3]))
        details_text.tag_configure("s_can_4", foreground="blue", underline=True)
        details_text.tag_bind("s_can_4", "<Button-1>", lambda e: open_url(urls["spells_c"][s_c_4]))
        
        details_text.tag_configure("s_first_1", foreground="blue", underline=True)
        details_text.tag_bind("s_first_1", "<Button-1>", lambda e: open_url(urls["spells_f"][s_f_1]))
        details_text.tag_configure("s_first_2", foreground="blue", underline=True)
        details_text.tag_bind("s_first_2", "<Button-1>", lambda e: open_url(urls["spells_f"][s_f_2]))
        
        details_text.config(state=tk.DISABLED)
    
    elif selection == "Warlock": # 2 Cantrips - 2 First #
        warlock_c = generate_warlock_cantrip()
        warlock_f = generate_warlock_first()
        result = f"\nWarlock Cantrips: {warlock_c}\n\nWarlock First Level: {warlock_f}"
        result_var.set(result)
        return result_var
    
    elif selection == "Wizard": # 3 Cantrips - INT+LVL First #
        wizard_c = generate_wizard_cantrip()
        wizard_f = generate_wizard_first()
        wizard_f2 = generate_wizard_first()
        wizard_f3 = generate_wizard_first()
        wizard_f4 = generate_wizard_first()
        wizard_f5 = generate_wizard_first()
        wizard_f6 = generate_wizard_first()
        result = f"\nWizard Cantrips: {wizard_c}\n\nWizard First Level - Intelligence 1-11: {wizard_f}\n\nWizard First Level - Intelligence 12-13: {wizard_f2}\n\nWizard First Level - Intelligence 14-15: {wizard_f3}\n\nWizard First Level - Intelligence 16-17: {wizard_f4}\n\nWizard First Level - Intelligence 18-19: {wizard_f5}\n\nWizard First Level - Intelligence 20: {wizard_f6}\n"
        result_var.set(result)
        return result_var
    
    elif selection == "Choose your Class":
        result = f"\nPlease Select a Class\n"
        result_var.set(result)
        return result_var

window = tk.Tk()
window.title("Random Spell Generator")

bold_font = font.Font(weight="bold")

result_var = tk.StringVar()
result_var.set("\nChoose your class to get your spells\n")

selected_class = tk.StringVar(value="Choose your Class")

dropdown_menu = tk.OptionMenu(window, selected_class, "Artificer", "Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard")
dropdown_menu.pack()

button = tk.Button(window, text="Generate", command=lambda: generate_spells(selected_class.get()), font=bold_font)
button.pack()

details_text = tk.Text(window, font=("Helvetica", 16), width=65, height=17)
details_text.pack(pady=20, padx=20)
# Disable text
details_text.config(state=tk.DISABLED)

#label = tk.Label(window, textvariable=result_var, font=("Hevetica", 16))
#label.grid(row=3, column=0, columnspan=10, padx=10)
#label.grid(sticky="ew")

window.mainloop()


#    _c_1 = generate__cantrip()
 #       _c_2 = generate__cantrip()
  #      _f_1 = generate__first()
   #     _f_2 = generate__first()
    #    _f_3 = generate__first()
     #   _f_4 = generate__first()
      #  details_text.config(state=tk.NORMAL)
       # details_text.delete(1.0, tk.END)
        #details_text.insert(tk.END, "\n have 2 Cantrips: ")
#        details_text.insert(tk.END, "\nCantrip #1: ")
 #       details_text.insert(tk.END, _c_1, ("spells_1", _c_1))
  #      details_text.insert(tk.END, "\nCantrip #2: ")
   #     details_text.insert(tk.END, _c_2, ("spells_2", _c_2))
    #    details_text.insert(tk.END, "\n\n have 4 First Level Spells:")
     #   details_text.insert(tk.END, "\n1st Level Spells #1: ")
      #  details_text.insert(tk.END, _f_1, ("spells_3", _f_1))
       # details_text.insert(tk.END, "\n1st Level Spells #2: ")
        #details_text.insert(tk.END, _f_2, ("spells_4", _f_2))
#        details_text.insert(tk.END, "\n1st Level Spells #3: ")
 #       details_text.insert(tk.END, _f_3, ("spells_5", _f_3))
  #      details_text.insert(tk.END, "\n1st Level Spells #4: ")
   #     details_text.insert(tk.END, _f_4, ("spells_6", _f_4))

#        details_text.tag_configure("spells_1", foreground="blue", underline=True)
 #       details_text.tag_bind("spells_1", "<Button-1>", lambda e: open_url(urls["spells_c"][_c_1]))
  #      details_text.tag_configure("spells_2", foreground="blue", underline=True)
   #     details_text.tag_bind("spells_2", "<Button-1>", lambda e: open_url(urls["spells_c"][_c_2]))
    #    details_text.tag_configure("spells_3", foreground="blue", underline=True)
     #   details_text.tag_bind("spells_3", "<Button-1>", lambda e: open_url(urls["spells_f"][_f_1]))
      #  details_text.tag_configure("spells_4", foreground="blue", underline=True)
       # details_text.tag_bind("spells_4", "<Button-1>", lambda e: open_url(urls["spells_f"][_f_2]))
        #details_text.tag_configure("spells_5", foreground="blue", underline=True)
#        details_text.tag_bind("spells_5", "<Button-1>", lambda e: open_url(urls["spells_f"][_f_3]))
 #       details_text.tag_configure("spells_6", foreground="blue", underline=True)
  #      details_text.tag_bind("spells_6", "<Button-1>", lambda e: open_url(urls["spells_f"][_f_4]))

   #     details_text.config(state=tk.DISABLED)