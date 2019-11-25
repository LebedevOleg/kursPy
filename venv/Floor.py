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
    def build1(self,build1):
        lb1 = Label(build1, text="Floor7")
        lb1.place(x=80, y=20)
        lb2 = Label(build1, text="Floor6")
        lb2.place(x=80, y=50)
        lb3 = Label(build1, text="Floor5")
        lb3.place(x=80, y=80)
        lb4 = Label(build1, text="Floor4")
        lb4.place(x=80, y=110)
        lb5 = Label(build1, text="Floor3")
        lb5.place(x=80, y=140)
        lb6 = Label(build1, text="Floor2")
        lb6.place(x=80, y=170)
        lb7 = Label(build1, text="Floor1")
        lb7.place(x=80, y=200)



