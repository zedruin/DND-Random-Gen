import random
import tkinter as tk
import webbrowser

# Races
races = ["Aasimar", "Animal Hybrid", "Birdfolk", "Bugbear", "Centaur", "Changeling", "Dhampir", "Dragonborn", "Dreamtouched", "Dwarf", "Elephantine", "Elf", "Fairy", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Half-Elf", "Half-Orc", "Halfling", "Harefolk", "Hobgoblin", "Human", "Kenku", "Kobold", "Leonine", "Lizardfolk", "Minotaur", "Orc", "Owlkin", "Satyr", "Shifter", "Tabaxi", "Tiefling", "Triton", "Turtle", "Violetken", "Warforged"]
# Classes
classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
# Backgrounds
backgrounds = ["Acolyte", "Athlete", "Charlatan", "City Watch", "Clan Crafter", "Cloistered Scholar", "Courtier", "Criminal", "Custom", "Entertainer", "Faction Agent", "Far Traveler", "Fey Lost", "Fisher", "Folk Hero", "Guild Artisan", "Haunted One", "Hermit", "House Agent", "Inheritor", "Investigator", "Knight", "Marine", "Mercenary Veteran", "Noble", "Outlander", "Port City Noble", "Sage", "Sailor", "Shipwright", "Smuggler", "Soldier", "Urban Bounty Hunter", "Urchin", "Violent Assassin", "Witch Carnival Hand"]
# Male Names
male = ["Ilint", "Nuwint", "Piltar", "Brodont", "Mauggair", "Vokrar", "Myrwinim", "Lalimin", "Celteeneil", "Cygoliam", "Vondrom", "Gulmiir", "Bhalgurn", "Darbek", "Theldahr", "Dulmor", "Bhaltharn", "Gimgram", "Ebrak", "Thornur", "Carris", "Zummenor", "Balbalar", "Nubby", "VanH", "CableKid", "Pnizzlez", "Arkeren", "DrFetus", "Eradan", "Dorsandoral", "Wranran", "Urifaren", "Carjeon", "Ervalur", "Wranlen", "Ulorin", "Vanlanann", "Zancraes", "Elfinas", "Riyeras", "Leophanis", "Yenzaren", "Hordithas", "Traword", "Walcoril", "Mezim", "Medam", "Nandur", "Roa", "Verder", "Nar", "Volderth", "Teth", "Suehkires", "Sat-Kor", "Vilmzousvok", "Mardisk", "Cha", "Chio", "Ornescol", "Zalur", "Thyneris", "Gueron", "Kilmong", "Akilius", "Morakos", "Thynevenom", "Horemon", "Casxikas", "Mavil", "Kavius"]
# Female Names
female = ["Varea", "Rili", "Odon", "Wama", "Ilar", "Eoma", "Worala", "Naslisau", "Ersesoum", "Zoleami", "Ranmyla", "Byllera", "Gemniss", "Reyntyn", "Brytnas", "Brendryn", "Bellela", "Dearglia", "Nesma", "Bronnura", "Sylcaryn", "Ulavyre", "Xyrphyra", "Faehana", "Yesralei", "Zindove", "Aragella", "Reymoira", "Keyzana", "Wynxisys", "Delqarin", "Gissie", "Hotice", "Floof", "Urilynn", "Madove", "Saelfine", "Galmalis", "Iroqarin", "Alymythe", "Hoviel", "Lesnalore", "Halyyra", "Fupisheil", "Eizeih", "Liroldra", "Kirrah", "Lirno", "Ce", "Bithiga", "Korhe", "Lazhuthe", "Nozes", "Duvrahi", "Yumma", "Jiao", "Pue", "Lontf", "Val", "Mithspira", "Zalypsis", "Valspira", "Marcira", "Cresis", "Datari", "Nithvine", "Phelypsis", "Phexori", "Iniyola"]
# Surnames
surname = ["Boldale", "Broodfinder", "Deepmantle", "Trollguard", "Boldfury", "Brangack", "Maroln", "Druhaveg", "Dubronack", "Hunkenurk", "Sterneye", "Lighthorn", "Wildforge", "Starkbane", "Strongboots", "Grazzihr", "Brenkam", "Cekuk", "Glurthirt", "Merdahun", "Oakensmile", "Rapidrest", "Azurelight", "Forestvale", "Oceanwalker", "Urinniphi", "Yurinne", "Nernadro", "Godrothro", "Gushennalkosh", "Cedarcrown", "Ambershine", "Woodmoon", "Cedarheel", "Nightlight", "Litholka", "Golithriith", "Ustral", "Lilphith", "Aldrennash", "Hosser", "Zaha", "Phoenixbreaker", "Marbletrack", "Bon", "Nimudz", "Stoutsun", "Lightningsnow", "Honskuchihk", "Lizdab", "Donumrildye", "Rarnetho", "Mieng", "Yay", "Ocinzo", "Culuzes", "Shammen", "Nannan", "Earthsnarl", "Phoenixpeak", "Vidz", "Glirdotsk", "Slateseeker", "Feathereyes", "Juezrinzed", "Dazdihd", "Digongotvi", "Stogaga", "Xum", "Puem", "Ivugar", "Ginzergi"]

# URLs for the Races, Classes, and Backgrounds
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
    }
}

def generate_character():
    random_race = random.choice(races)
    random_class = random.choice(classes)
    random_background = random.choice(backgrounds)
    random_male = random.choice(male)
    random_female = random.choice(female)
    random_surname = random.choice(surname)
    return random_race, random_class, random_background, random_male, random_female, random_surname

def roll_4d6_drop_lowest():
    # Roll 4d6
    rolls = [random.randint(1, 6) for _ in range(4)]
    lowest_roll = min(rolls)
    # Take lowest roll out
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
    random_race, random_class, random_background, random_male, random_female, random_surname = generate_character()
    roll_stat = generate_ability_scores()
    details_text.config(state=tk.NORMAL)
    details_text.delete(1.0, tk.END)
# Character Gen
    details_text.insert(tk.END, "\nRace: ")
    details_text.insert(tk.END, random_race, ("race", random_race))
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
    details_text.config(state=tk.DISABLED)
# URLs
    details_text.tag_configure("race", foreground="blue", underline=True)
    details_text.tag_bind("race", "<Button-1>", lambda e: open_url(urls["races"][random_race]))
    details_text.tag_configure("class", foreground="blue", underline=True)
    details_text.tag_bind("class", "<Button-1>", lambda e: open_url(urls["classes"][random_class]))
    details_text.tag_configure("background", foreground="blue", underline=True)
    details_text.tag_bind("background", "<Button-1>", lambda e: open_url(urls["backgrounds"][random_background]))

    details_text.config(state=tk.DISABLED)
# Make Window
window = tk.Tk()
window.title("Random Character Generator")
# Generate Button
button = tk.Button(window, text="Generate Character", font=("Helvetica", 16), command=display_character)
button.pack(pady=20)
# Blank Text
details_text = tk.Text(window, font=("Helvetica", 16), width=35, height=10)
details_text.pack(pady=20, padx=20)
# Disable text
details_text.config(state=tk.DISABLED)

window.mainloop()