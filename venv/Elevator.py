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
        self.twait = 0
        self.maxP = 10
        self.nowP = 0
        self.floorNow = 0
        self.floorNext = 1
        self.floorQueue = fakeQueue()
        self.person = []
    def enterP(self,Floor,numF):
        while self.nowP != self.maxP and Floor.getnumP() > 0:
            self.person.append(Floor.getpeople())
            self.floorQueue.add(self.person[self.nowP -1].getFloor())
            self.nowP+=1
        if self.nowP != 0:
            for i in self.person:
                if i.getFloor() == self.floorNow:
                    i.settimeE()
                    self.timer(i)
                    self.person.remove(i)
                    self.nowP-=1
      #  try:
            self.floorNext = self.floorQueue.dequeue(numF)
        # except:
        #     self.floorNext = -1
        #     print("Ошибка")

    def getfloorNow(self):
        return self.floorNow
    def getnowP(self):
        return self.nowP
    def strgetnowP(self):
        return str(self.nowP)
    def clean(self):
        self.allsummt = 0  # Техническая переменная для счета среднего времени пребывания пассажира в лифте
        self.allP = 0
        self.twait = 0
        self.maxP = 10
        self.nowP = 0
        self.floorNow = 0
        self.floorNext = 1
        self.floorQueue.clear()
        self.person = []
    def trevelt(self,floors):
        if self.nowP >0 and self.floorNext != 0:
            self.floorNow = self.floorNext
        elif self.floorNext == 0:
            for i in floors:
                if i.getnumP() != 0:
                    self.floorNext = i.getnumF()
                    break
            self.floorNow = self.floorNext

    def trevelcustom(self,floors,el,fl,c,elt,e):
        if self.nowP >0 and self.floorNext != -1:
            while self.floorNext!=self.floorNow:
                time.sleep(0.5)
                if self.floorNow < self.floorNext:
                    self.floorNow +=1
                else:
                    self.floorNow -= 1
                c.coords(el,100 + e*40,fl[self.floorNext],130 + e*40,fl[self.floorNext]+20)
                c.coords(elt,115 + e*40,fl[self.floorNext]+10)
            self.floorNow = self.floorNext
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
                time.sleep(0.5)
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
     self.allsummt += i.gettwaitE()
     self.allP +=1
     self.twait = self.allsummt/self.allP
    def getTwait(self):
        return str(self.twait)
    def getAllsumm(self):
        return self.allsummt