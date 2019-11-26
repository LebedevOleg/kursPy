from Elevator import*
from Floor import*
from People import*
from tkinter import *
from queue import Queue
import time
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


    def trevelt(self,floors):
        if self.nowP >0 and self.floorNext != 0:
            self.floorNow = self.floorNext
        elif self.floorNext == 0:
            for i in floors:
                if i.getnumP() != 0:
                    self.floorNext = i.getnumF()
                    break
            self.floorNow = self.floorNext

    def trevel(self,floors,el,fl,c,elt):
        if self.nowP >0 and self.floorNext != 0:
            for i in range(0,abs(self.floorNext-self.floorNow)):
                time.sleep(0.3)
            c.move(el, 0, fl[self.floorNow] - fl[self.floorNext])
            c.move(elt, 0, fl[self.floorNow] - fl[self.floorNext])
            self.floorNow = self.floorNext
        elif self.floorNext == 0:
            for i in floors:
                if i.getnumP() != 0:
                    self.floorNext = i.getnumF()
                    break
            for i in range(0,abs(self.floorNext-self.floorNow)):
                time.sleep(0.3)
            c.move(el, 0, fl[self.floorNow] - fl[self.floorNext])
            c.move(elt, 0, fl[self.floorNow] - fl[self.floorNext])
            self.floorNow = self.floorNext

