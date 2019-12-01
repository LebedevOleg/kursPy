from Elevator import*
from Floor import*
from People import*
from tkinter import *
class Floor:
    def __init__(self, num):
        self.numF = num
        self.numP = []
        self.allsummt = 0  # Техническая переменная для счета среднего времени пребывания пассажира в лифте
        self.allP = 0
        self.twait = 0
    def setnumP(self,people):
        self.numP.append(people)
        self.stupP()
    def getnumP(self):
        return len(self.numP)
    def getpeople(self):
        p = self.numP.pop()
        p.settimeF()
        self.timer(p)
        return p
    def __str__(self):
        return "F"+str(self.numF) + " P:" + peopleprint(self.numP)
    def getnumF(self):
        return self.numF
    def stupP(self):
        for i in self.numP:
            if i.getFloor() == self.numF:
                self.numP.remove(i)
    def timer(self,i):
        self.allsummt += i.gettwaitF()
        self.allP += 1
        self.twait = self.allsummt / self.allP
    def getTwait(self):
        return str(self.twait)
    def getAllsumm(self):
        return self.allsummt
    def build1(self,build1,c):
        c.create_text(50, 20, text="Floor7")
        c.create_text(50, 50, text="Floor6")
        c.create_text(50, 80,  text="Floor5")
        c.create_text(50, 110, text="Floor4")
        c.create_text(50, 140,  text="Floor3")
        c.create_text(50, 170,  text="Floor2")
        c.create_text(50, 200,  text="Floor1")

    def build2(self, build2, c,numF):
        temp = 20
        for i in range(numF):
            c.create_text(50,temp + i*30,text = "Floor" + str(numF - i))


