import easygui as g
import json
import os
from funkcije import *
from klase import *
from variable import *

fcg = easyGuiGen(title, mainScreenChoices)
fcg.welcomeScreen()

chekJF = checkJsonFile()

if chekJF == False:
    createJsonFile()
else:
    pass

while n == 1:
    start = fcg.mainMenu()
    if start == choseExit:
        break
    elif start == choseCreate:
        name = CharacterGenerator(chargenT).charNameF()
        gender = CharacterGenerator(chargenT, charGend).charGenderF()
        race = CharacterGenerator(chargenT,charRace).charRaceF()
        klass = CharacterGenerator(chargenT, charClass).charClassF()
        charInfo(name, gender, race, klass, title)
        saveCharacter(name, gender, race, klass, pathJson)
    elif start == choseList:
        pass
    elif start == choseDelete:
        pass
    else:
        break



