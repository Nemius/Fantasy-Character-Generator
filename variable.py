#---------------------------- razno
title = "FCG V0.1"
pathJson = "charJbase.json"
n = 1
#---------------------------- user input values
name = ""
klass = ""
race = ""
gender = ""
#---------------------------- char creator variable
textName = "Enter name of your character: "
textClass = "Chosse your class: "
textRace = "Chosse your race: "
textGender = "Chosse your gender: "
#---------------------------- main menu chose options
choseCreate = "Create new character"
choseList = "List all characters"
choseDelete = "Delete the character"
choseExit = "Exit"
mainScreenChoices = [choseCreate, choseList, choseDelete, choseExit]
#---------------------------- create char class args
chargenT = (pathJson, name, klass,race,textName,textClass, textRace, title)
charClass = ["Barbarian", "Bard", "Cleric", "Druid", "Paladin", "Ranger", "Rouge", "Sorceror", "Warlock", "Wizard", "Warrior"]
charRace = ["Human", "Elf", "Dwarf", "Half-Elf", "Half-Orc", "Gnome"]
charGend = ["Male", "Female"]
