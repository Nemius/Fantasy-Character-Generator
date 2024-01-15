from funkcije import *
from variable import *
import easygui as g


class CharacterGenerator:

    def __init__ (self, *args, **kwargs):
        self.pathJson = pathJson
        self.name = name
        self.klass = klass
        self.race = race
        self.gender = gender
        self.textName = textName
        self.textClass = textClass
        self.textRace = textRace
        self.textGender = textGender
        self.title = title
        self.charClass = charClass
        self.charRace = charRace
        self.charGend = charGend

    def charNameF(self):
        outputName = g.enterbox(self.textName, self.title)
        return outputName

    def charGenderF(self):
        choiceGen = g.choicebox(self.textGender, self.title, self.charGend)
        return choiceGen

    def charRaceF(self):
        choiceRace = g.choicebox(self.textRace, self.title, self.charRace)
        return choiceRace

    def charClassF(self):
        choiceClass = g.choicebox(self.textClass, self.title, self.charClass)
        return choiceClass

class easyGuiGen:

    def __init__ (self, title, mainScreenChoices):
        self.title = title
        self.mainScreenChoices = mainScreenChoices

    def welcomeScreen(self):
        g.msgbox("Welcom to Fantasy Character Generator!", self.title)

    def mainMenu(self):
        msg = "Main Barracks"
        choice = g.choicebox(msg, self.title, self.mainScreenChoices)
        return choice
