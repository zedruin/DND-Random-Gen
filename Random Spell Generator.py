import webbrowser
import random
import tkinter as tk
from tkinter import font

# Artificer - 2 cantrips - 2 first level
artificer_cantrip = ["Acid Splash", "Booming Blade", "Create Bonfire", "Dancing Lights", "Fire Bolt", "Frostbite", "Green-Flame Blade", "Guidance", "Light", "Lightning Lure", "Mage Hand", "Magic Stone", "Mending", "Message", "Poison Spray", "Prestidigitation", "Ray of Frost", "Resistance", "Shocking Grasp", "Spare the Dying", "Sword Burst", "Thorn Whip", "Thunderclap"]
artificer_first = ["Asorb Elements", "Alarm", "Arcane Weapon", "Catapult", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump", "Longstrider", "Purify Food and Drink", "Sanctuary", "Snare", "Tasha's Caustic Brew"]
# Bard - 2 cantrips - 4 first level
bard_cantrip = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation", "Thunderclap", "True Strike", "Vicious Mockery"]
bard_first = [" Animal Friendship ", " Bane ", " Charm Person ", " Color Spray ", " Command ", " Comprehend Languages ", " Cure Wounds ", " Detect Magic ", " Disguise Self ", " Dissonant Whispers ", " Distort Value ", " Earth Tremor ", " Faerie Fire ", " Feather Fall ", " Guiding Hand ", " Healing Word ", " Heroism ", " Identify ", " Illusory Script ", " Longstrider ", " Puppet ", " Sense Emotion ", " Silent Image ", " Silvery Barbs ", " Sleep ", " Speak with Animals ", " Sudden Awakening ", " Tasha's Hideous Laughter ", " Thunderwave ", " Unearthly Chourus ", " Unseen Servant "]
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

##### Generate Spells #####
# Artificer Spells - 2 cantrip - 2 first
def generate_artificer_cantrip():
    artificers_cantrip = [random.sample(artificer_cantrip, 2)]
    return artificers_cantrip
def generate_artificer_first():
    artificers_first = [random.sample(artificer_first, 2)]
    return artificers_first
# Bard Spells - 2 cantrip - 4 first
def generate_bard_cantrip():
    bards_cantrip = [random.sample(bard_cantrip, 2)]
    return bards_cantrip
def generate_bard_first():
    bards_first = [random.sample(bard_first, 4)]
    return bards_first
# Cleric - 3 cantrips - Wisdom + Cleric Level (1)
def generate_cleric_cantrip():
    clerics_cantrip = [random.sample(cleric_cantrip, 3)]
    return clerics_cantrip
def generate_cleric_first():
    clerics_first = [random.sample(cleric_first, 1)]
    return clerics_first
def generate_cleric_first_2():
    clerics_first_2 = [random.sample(cleric_first, 2)]
    return clerics_first_2
def generate_cleric_first_3():
    clerics_first_3 = [random.sample(cleric_first, 3)]
    return clerics_first_3
def generate_cleric_first_4():
    clerics_first_4 = [random.sample(cleric_first, 4)]
    return clerics_first_4
def generate_cleric_first_5():
    clerics_first_5 = [random.sample(cleric_first, 5)]
    return clerics_first_5
def generate_cleric_first_6():
    clerics_first_6 = [random.sample(cleric_first, 6)]
    return clerics_first_6
# Druid - 2 cantrips - Wisdom + Druid Level (1)
def generate_druid_cantrip():
    druids_cantrip = [random.sample(druid_cantrip, 2)]
    return druids_cantrip
def generate_druid_first():
    druids_first = [random.sample(druid_first, 1)]
    return druids_first
def generate_druid_first_2():
    druid_first_2 = [random.sample(druid_first, 2)]
    return druid_first_2
def generate_druid_first_3():
    druid_first_3 = [random.sample(druid_first, 3)]
    return druid_first_3
def generate_druid_first_4():
    druid_first_4 = [random.sample(druid_first, 4)]
    return druid_first_4
def generate_druid_first_5():
    druid_first_5 = [random.sample(druid_first, 5)]
    return druid_first_5
def generate_druid_first_6():
    druid_first_6 = [random.sample(druid_first, 6)]
    return druid_first_6
# Sorcerer - 4 cantrips - 2 first
def generate_sorcerer_cantrip():
    sorcerers_cantrip = [random.sample(sorcerer_cantrip, 4)]
    return sorcerers_cantrip
def generate_sorcerer_first():
    sorcerers_first = [random.sample(sorcerer_first, 2)]
    return sorcerers_first
# Warlock - 1 cantrips + Eldritch Blast - 2 first level
def generate_warlock_cantrip():
    warlocks_cantrip = [random.sample(warlock_cantrip, 1)]
    return f"Eldritch Blast", warlocks_cantrip
def generate_warlock_first():
    warlocks_first = [random.sample(warlock_first, 2)]
    return warlocks_first
# Wizard - 3 cantrips - Intelligence + Wizard Level (1)
def generate_wizard_cantrip():
    wizards_cantrip = [random.sample(wizard_cantrip, 3)]
    return wizards_cantrip
def generate_wizard_first():
    wizards_first = [random.sample(wizard_first, 1)]
    return wizards_first
def generate_wizard_first_2():
    wizard_first_2 = [random.sample(wizard_first, 2)]
    return wizard_first_2
def generate_wizard_first_3():
    wizard_first_3 = [random.sample(wizard_first, 3)]
    return wizard_first_3
def generate_wizard_first_4():
    wizard_first_4 = [random.sample(wizard_first, 4)]
    return wizard_first_4
def generate_wizard_first_5():
    wizard_first_5 = [random.sample(wizard_first, 5)]
    return wizard_first_5
def generate_wizard_first_6():
    wizard_first_6 = [random.sample(wizard_first, 6)]
    return wizard_first_6
##### ######

def generate_spells(selection):
    if selection == "Artificer":
        artificer_c = generate_artificer_cantrip()
        artificer_f = generate_artificer_first()
        result = f"\nArtificer Cantrips: {artificer_c}\n\nArtificer First Level: {artificer_f}\n"
        result_var.set(result)
        return result_var

    elif selection == "Bard":
        bard_c = generate_bard_cantrip()
        bard_f = generate_bard_first()
        result = f"\nBard Cantrips: {bard_c}\n\nBard First Level: {bard_f}\n"
        result_var.set(result)
        return result_var
    
    elif selection == "Cleric":
        cleric_c = generate_cleric_cantrip()
        cleric_f = generate_cleric_first()
        cleric_f2 = generate_cleric_first_2()
        cleric_f3 = generate_cleric_first_3()
        cleric_f4 = generate_cleric_first_4()
        cleric_f5 = generate_cleric_first_5()
        cleric_f6 = generate_cleric_first_6()
        result = f"\nCleric Cantrips: {cleric_c}\n\nCleric First Level - Wisdom 1-11: {cleric_f}\n\nCleric First Level - Wisdom 12-13: {cleric_f2}\n\nCleric First Level - Wisdom 14-15: {cleric_f3}\n\nCleric First Level - Wisdom 16-17: {cleric_f4}\n\nCleric First Level - Wisdom 18-19: {cleric_f5}\n\nCleric First Level - Wisdom 20: {cleric_f6}\n"
        result_var.set(result)
        return result_var
    
    elif selection == "Druid":
        druid_c = generate_druid_cantrip()
        druid_f = generate_druid_first()
        druid_f2 = generate_druid_first_2()
        druid_f3 = generate_druid_first_3()
        druid_f4 = generate_druid_first_4()
        druid_f5 = generate_druid_first_5()
        druid_f6 = generate_druid_first_6()
        result = f"\nDruid Cantrips: {druid_c}\n\nDruid First Level - Wisdom 1-11: {druid_f}\n\nDruid First Level - Wisdom 12-13: {druid_f2}\n\nDruid First Level - Wisdom 14-15: {druid_f3}\n\nDruid First Level - Wisdom 16-17: {druid_f4}\n\nDruid First Level - Wisdom 18-19: {druid_f5}\n\nDruid First Level - Wisdom 20: {druid_f6}\n"
        result_var.set(result)
        return result_var
    
    elif selection == "Sorcerer":
        sorcerer_c = generate_sorcerer_cantrip()
        sorcerer_f = generate_sorcerer_first()
        result = f"\nSorcerer Cantrips: {sorcerer_c}\n\nSorcerer First Level: {sorcerer_f}"
        result_var.set(result)
        return result_var
    
    elif selection == "Warlock":
        warlock_c = generate_warlock_cantrip()
        warlock_f = generate_warlock_first()
        result = f"\nWarlock Cantrips: {warlock_c}\n\nWarlock First Level: {warlock_f}"
        result_var.set(result)
        return result_var
    
    elif selection == "Wizard":
        wizard_c = generate_wizard_cantrip()
        wizard_f = generate_wizard_first()
        wizard_f2 = generate_wizard_first_2()
        wizard_f3 = generate_wizard_first_3()
        wizard_f4 = generate_wizard_first_4()
        wizard_f5 = generate_wizard_first_5()
        wizard_f6 = generate_wizard_first_6()
        result = f"\nWizard Cantrips: {wizard_c}\n\nWizard First Level - Intelligence 1-11: {wizard_f}\n\nWizard First Level - Intelligence 12-13: {wizard_f2}\n\nWizard First Level - Intelligence 14-15: {wizard_f3}\n\nWizard First Level - Intelligence 16-17: {wizard_f4}\n\nWizard First Level - Intelligence 18-19: {wizard_f5}\n\nWizard First Level - Intelligence 20: {wizard_f6}\n"
        result_var.set(result)
        return result_var
    
    elif selection == "Choose your Class":
        result = f"\nPlease Select a Class\n"
        result_var.set(result)
        return result_var



#def generate_artificer():
    artificer_c = generate_artificer_cantrip()
    artificer_f = generate_artificer_first()
    result = f"\nArtificer Cantrips: {artificer_c}\n\nArtificer First Level: {artificer_f}\n"
    result_var.set(result)
    return result_var

#def generate_bard():
    bard_c = generate_bard_cantrip()
    bard_f = generate_bard_first()
    result = f"\nBard Cantrips: {bard_c}\n\nBard First Level: {bard_f}\n"
    result_var.set(result)
    return result_var

#def generate_cleric():
    cleric_c = generate_cleric_cantrip()
    cleric_f = generate_cleric_first()
    cleric_f2 = generate_cleric_first_2()
    cleric_f3 = generate_cleric_first_3()
    cleric_f4 = generate_cleric_first_4()
    cleric_f5 = generate_cleric_first_5()
    cleric_f6 = generate_cleric_first_6()
    result = f"\nCleric Cantrips: {cleric_c}\n\nCleric First Level - Wisdom 1-11: {cleric_f}\n\nCleric First Level - Wisdom 12-13: {cleric_f2}\n\nCleric First Level - Wisdom 14-15: {cleric_f3}\n\nCleric First Level - Wisdom 16-17: {cleric_f4}\n\nCleric First Level - Wisdom 18-19: {cleric_f5}\n\nCleric First Level - Wisdom 20: {cleric_f6}\n"
    result_var.set(result)
    return result_var

#def generate_druid():
    druid_c = generate_druid_cantrip()
    druid_f = generate_druid_first()
    druid_f2 = generate_druid_first_2()
    druid_f3 = generate_druid_first_3()
    druid_f4 = generate_druid_first_4()
    druid_f5 = generate_druid_first_5()
    druid_f6 = generate_druid_first_6()
    result = f"\nDruid Cantrips: {druid_c}\n\nDruid First Level - Wisdom 1-11: {druid_f}\n\nDruid First Level - Wisdom 12-13: {druid_f2}\n\nDruid First Level - Wisdom 14-15: {druid_f3}\n\nDruid First Level - Wisdom 16-17: {druid_f4}\n\nDruid First Level - Wisdom 18-19: {druid_f5}\n\nDruid First Level - Wisdom 20: {druid_f6}\n"
    result_var.set(result)
    return result_var

#def generate_sorcerer():
    sorcerer_c = generate_sorcerer_cantrip()
    sorcerer_f = generate_sorcerer_first()
    result = f"\nSorcerer Cantrips: {sorcerer_c}\n\nSorcerer First Level: {sorcerer_f}"
    result_var.set(result)
    return result_var

#def generate_warlock():
    warlock_c = generate_warlock_cantrip()
    warlock_f = generate_warlock_first()
    result = f"\nWarlock Cantrips: {warlock_c}\n\nWarlock First Level: {warlock_f}"
    result_var.set(result)
    return result_var

#def generate_wizard():
    wizard_c = generate_wizard_cantrip()
    wizard_f = generate_wizard_first()
    wizard_f2 = generate_wizard_first_2()
    wizard_f3 = generate_wizard_first_3()
    wizard_f4 = generate_wizard_first_4()
    wizard_f5 = generate_wizard_first_5()
    wizard_f6 = generate_wizard_first_6()
    result = f"\nWizard Cantrips: {wizard_c}\n\nWizard First Level - Intelligence 1-11: {wizard_f}\n\nWizard First Level - Intelligence 12-13: {wizard_f2}\n\nWizard First Level - Intelligence 14-15: {wizard_f3}\n\nWizard First Level - Intelligence 16-17: {wizard_f4}\n\nWizard First Level - Intelligence 18-19: {wizard_f5}\n\nWizard First Level - Intelligence 20: {wizard_f6}\n"
    result_var.set(result)
    return result_var


window = tk.Tk()
window.title("Random Spell Generator")

bold_font = font.Font(weight="bold")

result_var = tk.StringVar()
result_var.set("\nChoose your class to get your spells\n")

selected_class = tk.StringVar(value="Choose your Class")

dropdown_menu = tk.OptionMenu(window, selected_class, "Artificer", "Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard")
dropdown_menu.grid(row=0, column=1, padx=10)

button = tk.Button(window, text="Generate", command=lambda: generate_spells(selected_class.get()), font=bold_font)
button.grid(row=0, column=0, padx=10)

label = tk.Label(window, textvariable=result_var, font=("Hevetica", 16))
label.grid(row=3, column=0, columnspan=10, padx=10)
label.grid(sticky="ew")

window.mainloop()