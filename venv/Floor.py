from Elevator import*
from Floor import*
from People import*
from tkinter import *
class Floor:
    def __init__(self, num):
        self.numF = num
        self.numP = []
    def setnumP(self,people):
        self.numP.append(people)
        self.stupP()
    def getnumP(self):
        return len(self.numP)
    def getpeople(self):
        return self.numP.pop()
    def __str__(self):
        return "F"+str(self.numF) + " P:" + peopleprint(self.numP)
    def getnumF(self):
        return self.numF
    def stupP(self):
        for i in self.numP:
            if i.getFloor() == self.numF:
                self.numP.remove(i)
    def build1(self,build1,c):
        c.create_text(50, 20, text="Floor7")
        c.create_text(50, 50, text="Floor6")
        c.create_text(50, 80,  text="Floor5")
        c.create_text(50, 110, text="Floor4")
        c.create_text(50, 140,  text="Floor3")
        c.create_text(50, 170,  text="Floor2")
        c.create_text(50, 200,  text="Floor1")



