import os
import os.path
import easygui as g
from klase import *
from variable import *
#from main import name, gender, race, klass

def checkJsonFile():
    chek_file = os.path.isfile(pathJson)
    return chek_file

def createJsonFile():
    creatFile = open("charJbase.json", "w")
    creatFile.close

def charInfo(name, gender, race, klass, title):
    msgCharInfo = "Your character by the name of {}, who is {} {}, and by ocupation is {}, is successfully created.".format(name, gender, race, klass)
    chInfo = g.msgbox(msgCharInfo, title)

def saveCharacter():
    pass

def listCharacter():
    pass

def deleteCharacter():
    pass
