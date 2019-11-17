import random
import msvcrt

import os
class Elevator:
    def __init__(self):
        self.maxP = 10
        self.nowP = 0
        self.floorNow = 0
        self.floorNext = 1
        self.person = []
    def enterP(self,Floor):
        while self.nowP != self.maxP and Floor.getnumP() > 0:
            self.person.append(Floor.getpeople())
            self.nowP+=1
        if self.nowP != 0:
            for i in self.person:
                if i.getFloor() == self.floorNow:
                    self.person.remove(i)
                    self.nowP-=1
        try:
            self.floorNext = self.person[0].getFloor()
        except:
            self.floorNext = 0

    def getfloorNow(self):
        return self.floorNow
    def getnowP(self):
        return self.nowP


    def trevel(self,floors):
        if self.nowP == self.maxP:
            self.floorNow = self.floorNext
        elif self.floorNow<len(floors)-1:
            self.floorNow +=1
        else:
            self.floorNow = self.floorNext



class Floor:
    def __init__(self, num):
        self.numF = num
        self.numP = []

    def setnumP(self,people):
        self.numP.append(people)

    def getnumP(self):
        return len(self.numP)
    def getpeople(self):
        return self.numP.pop()
    def __str__(self):
        return "F"+str(self.numF) + " P:" + peopleprint(self.numP)
    def getnumF(self):
        return self.numF



class People:
    def __init__(self, floorMax):
        self.needF = random.randint(1,floorMax)
    def __str__(self):
        return " ("+ str(self.needF)+ ") "
    def getFloor(self):
        return self.needF

elevator = Elevator()
Fl = []
people = []
def printe():
    for i in range(5):
        floor = Floor(i)
        p = People(4)
        floor.setnumP(p)
        Fl.append(floor)

def peopleprint(l):
    out = ""
    for i in l:
         out += str(i)
    return out
printe()

while True:
    for i in Fl:
        if elevator.getfloorNow() == i.getnumF():
            print(i, end= ' ')
            print("  ["+ str(elevator.getnowP()) + "]")
            elevator.enterP(i)
        else:
            print(i)
    elevator.trevel(Fl)
    print("\n\n")

