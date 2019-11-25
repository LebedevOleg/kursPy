from Elevator import*
from Floor import*
from People import*
from tkinter import *
from queue import Queue
class Elevator:
    def __init__(self):
        self.maxP = 10
        self.nowP = 0
        self.floorNow = 0
        self.floorNext = 1
        self.floorQueue = Queue()
        self.person = []
    def enterP(self,Floor):
        while self.nowP != self.maxP and Floor.getnumP() > 0:
            self.person.append(Floor.getpeople())
            self.floorQueue.put(self.person[self.nowP -1].getFloor())
            self.nowP+=1
        if self.nowP != 0:
            for i in self.person:
                if i.getFloor() == self.floorNow:
                    self.person.remove(i)
                    self.nowP-=1
        try:
            self.floorNext = self.floorQueue.get()
        except:
            self.floorNext = 0

    def getfloorNow(self):
        return self.floorNow
    def getnowP(self):
        return self.nowP


    def trevel(self,floors):
        if self.nowP >0 and self.floorNext != 0:
            self.floorNow = self.floorNext
        elif self.floorNext == 0:
            for i in floors:
                if i.getnumP() != 0:
                    self.floorNext = i.getnumF()
                    break
            self.floorNow = self.floorNext

    def trevel(self,floors,el,fl):
        if self.nowP >0 and self.floorNext != 0:
            self.floorNow = self.floorNext
            el.configure(height = fl[self.floorNow])
        elif self.floorNext == 0:
            for i in floors:
                if i.getnumP() != 0:
                    self.floorNext = i.getnumF()
                    break
            self.floorNow = self.floorNext
            el.configure(height=fl[self.floorNow])
