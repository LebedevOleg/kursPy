import random
from Elevator import*
from Floor import*
from People import*
class People:
    def __init__(self, floorMax):
        self.needF = random.randint(0,floorMax)
        self.time_waitF = 0
        self.time_waitE = 0
    def __str__(self):
        return " ("+ str(self.needF)+ ") "
    def getFloor(self):
        return self.needF
    def settimeF(self,start,end):
        self.time_waitF = start - end
    def settimeE(self, start, end):
        self.time_waitE = start - end

def peopleprint(l):
    out = ""
    for i in l:
         out += str(i)
    return out