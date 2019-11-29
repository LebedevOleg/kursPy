import random
import datetime
import time
from Elevator import*
from Floor import*
from People import*
class People:
    def __init__(self, floorMax):
        self.needF = random.randint(0,floorMax)
        self.time_waitF = 0
        self.time_waitE = 0
        self.start = time.clock()
    def __str__(self):
        return " ("+ str(self.needF)+ ") "
    def getFloor(self):
        return self.needF
    def settimeF(self):
        end = time.clock()
        self.time_waitF = end -self.start
        self.start = time.clock()
    def settimeE(self):
        end = time.clock()
        self.time_waitE = end -self.start
    def gettwaitF(self):
        return self.time_waitF
    def gettwaitE(self):
        return self.time_waitE

def peopleprint(l):
    out = ""
    for i in l:
         out += str(i)
    return out