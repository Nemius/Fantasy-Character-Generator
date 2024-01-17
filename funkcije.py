import os
import os.path
import easygui as g
import json
from klase import *
from variable import *
#Proverava da li ima Json
def checkJsonFile():
    chek_file = os.path.isfile(pathJson)
    return chek_file

#kreira Json ako je izbrisan
def createJsonFile():
    creatFile = open("charJbase.json", "w")
    creatFile.close

#potvrda izbora
def charInfo(name, gender, race, klass, title):
    msgCharInfo = "Your character by the name of {}, who is {} {}, and by ocupation is {}, is successfully created.".format(name, gender.lower(), race.lower(), klass)
    chInfo = g.msgbox(msgCharInfo, title)

#upisivanje u Json
def saveCharacter(name, gender, race, klass, pathJson):
    chInfo = {"Name": str(name), "Gender": str(gender), "Race": str(race), "Class": str(klass)}
    with open(pathJson, "a") as f:
        json.dump(chInfo, f, indent=4)

#ucitavanje is Json
def listCharacter():
    pass

#brisanje iz Json
def deleteCharacter():
    pass