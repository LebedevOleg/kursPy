from Elevator import*
from Floor import*
from People import*
from tkinter import *
from queue import Queue
from fakeQueue import fakeQueue
import time

class Elevator:
    def __init__(self):
        self.allsummt = 0 #Техническая переменная для счета среднего времени пребывания пассажира в лифте
        self.allP = 0
        self.allPL = []
        self.allPL.append(0)
        self.twait = 0
        self.maxP = 10
        self.nowP = 0
        self.floorNow = 0
        self.floorNext = 1
        self.floorQueue = fakeQueue()
        self.person = []
        self.type = 1
        self.cheak = 0
    def enterP(self,Floor,numF,Floors,elevators):
        while self.nowP != self.maxP and Floor.getnumP() > 0:
            self.person.append(Floor.getpeople())
            self.floorQueue.add(self.person[len(self.person)-1].getFloor())
            self.nowP+=1
        self.delete()
        time.sleep(1)
        if self.type == 1:
            self.nextfloor1(numF)
        elif self.type == 2:
            self.nextfloor2(numF)
        elif self.type ==3:
            self.nextfloor3(numF,Floors)
        elif self.type == 4:
            self.nextfloor4()
       # if len(elevators) > 0:
        #    for i in elevators:
         #       if i.getfloornext() == self.getfloornext() and i.get != self.getTwait():
          #          self.floorNext +=1
    def nextfloor1(self,numF):
        self.floorNext = self.floorQueue.dequeue(numF)
    def nextfloor2(self, numF):
        self.floorNext = self.floorQueue.maxcount(numF)
    def nextfloor3(self,numF,floors):
        if self.nowP<6:
            trash =[]
            for i in floors:
                trash.append(i.getnumP())
            if self.floorNow != trash.index(max(trash)):
                self.floorNext = trash.index(max(trash))
        else:
            self.floorNext = self.floorQueue.maxcount(numF)




    def getfloorNow(self):
        return self.floorNow
    def getnowP(self):
        return self.nowP
    def strgetnowP(self):
        return str(self.nowP)
    def clean(self):
        self.allsummt = 0  # Техническая переменная для счета среднего времени пребывания пассажира в лифте
        self.allP = 0
        self.allPL = []
        self.twait = 0
        self.maxP = 10
        self.nowP = 0
        self.floorNow = 0
        self.floorNext = 1
        self.floorQueue.clear()
        self.person = []
        self.cheak = 0
    def cheakt(self):
        return self.cheak
    def setcheak(self,cheak):
        self.cheak = cheak
    def trevelt(self,floors):
        if self.nowP >0 and self.floorNext != 0:
            self.floorNow = self.floorNext
        elif self.floorNext == 0:
            for i in floors:
                if i.getnumP() != 0:
                    self.floorNext = i.getnumF()
                    break
            self.floorNow = self.floorNext

    def trevelcustom(self,floors,el,fl,c,elt,e,build2):
        if self.nowP >-1 and self.floorNext != -1 and self.floorNext != self.floorNow:
            #while self.floorNext!=self.floorNow:
            #time.sleep(0.25)
            if self.floorNow < self.floorNext:
                self.floorNow +=1
            else:
                self.floorNow -= 1
            c.coords(el,100 + e*40,fl[self.floorNow],130 + e*40,fl[self.floorNow]+20)
            c.coords(elt,115 + e*40,fl[self.floorNow]+10)
            if self.floorNow == self.floorNext:
                self.cheak = 1



        # elif self.floorNext == -1:
        #     for i in floors:
        #         if i.getnumP() != 0:
        #             self.floorNext = i.getnumF()
        #             break
        #     if self.floorNext != 0:
        #         for i in range(0,abs(self.floorNext-self.floorNow)):
        #             time.sleep(0.2)
        #     else:
        #         if self.floorNext +1 > len(floors)-1:
        #             self.floorNext +=1
        #         else:
        #             self.floorNext = 0
        #     c.coords(el, 100 + e * 40, fl[self.floorNext], 130 + e * 40, fl[self.floorNext] + 20)
        #     c.coords(elt, 115 + e * 40, fl[self.floorNext] + 10)
        #     self.floorNow = self.floorNext

    def trevel(self,floors,el,fl,c,elt,build1):
        if self.nowP >0 and self.floorNext != -1:
            while self.floorNext!=self.floorNow:
                time.sleep(0.25)
                if self.floorNow < self.floorNext:
                    self.floorNow +=1
                else:
                    self.floorNow -= 1
                c.coords(el, 100, fl[self.floorNow], 130, fl[self.floorNow] + 20)
                c.coords(elt,115 ,fl[self.floorNow]+10)
                build1.update()
            # for i in range(0,abs(self.floorNext-self.floorNow)):
            #     time.sleep(1)
            # c.coords(el,100 ,fl[self.floorNext],130,fl[self.floorNext]+20)
            # c.coords(elt,115 ,fl[self.floorNext]+10)
            # self.floorNow = self.floorNext
        # elif self.floorNext == -1:
        #     for i in floors:
        #         if i.getnumP() != 0:
        #             self.floorNext = i.getnumF()
        #             break
        #     if self.floorNext != 0:
        #         for i in range(0,abs(self.floorNext-self.floorNow)):
        #             time.sleep(0.2)
        #     else:
        #         if self.floorNext +1 > len(floors)-1:
        #             self.floorNext =0
        #         else:
        #             self.floorNext += 1
        #     c.coords(el, 100 , fl[self.floorNext], 130, fl[self.floorNext] + 20)
        #     c.coords(elt, 115 , fl[self.floorNext] + 10)
        #     self.floorNow = self.floorNext

    def timer(self,i):
     self.allPL.append(i.gettwaitE())
     self.allsummt += i.gettwaitE()
     self.allP +=1
     self.twait = self.allsummt/self.allP
    def getTwait(self):
        return str(self.twait)
    def getAllsumm(self):
        return self.allsummt
    def max(self):
        return str(max(self.allPL))
    def settype(self,type):
        self.type = type
    def gettype(self):
        return str(self.type)
    def __str__(self):
        out = "("
        if len(self.person):
            for i in self.person:
                out += str(i.getFloor()) + ") ("
        return out + ")"
    def delete(self):
        if self.nowP != 0:
            for i in self.person:
                if i.getFloor() == self.floorNow:
                    i.settimeE()
                    self.timer(i)
                    self.person.remove(i)
                    self.nowP-=1
                    self.delete()
    def setfloorNow(self,nowF):
        self.floorNow = nowF
    def getfloornow(self):
        return self.floorNow
    def getfloornext(self):
        return self.floorNext