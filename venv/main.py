import random
import msvcrt
import time
import os
from Elevator import*
from Floor import*
from People import*

elevator = Elevator()
Fl = []
people = []
def printe():
    for i in range(7):
        floor = Floor(i)
        p = People(6)
        floor.setnumP(p)
        Fl.append(floor)
def addPeople(x = 3):
    for j in range(1,random.randint(1,x)):
        for i in range(0,random.randint(1,len(Fl))):
            p = People(len(Fl)-1)
            Fl[i].setnumP(p)
def printB():
    for i in Fl:
        if elevator[0].getfloorNow() == i.getnumF() and elevator[1].getfloorNow() == i.getnumF():
            print(i, end=' ')
            print("  [" + str(elevator[0].getnowP()) + "]" +"  [" + str(elevator[1].getnowP()) + "]")
            elevator[0].enterP(i)
            elevator[1].enterP(i)
        elif elevator[1].getfloorNow() == i.getnumF() and elevator[0].getfloorNow() != i.getnumF():
            print(i, end=' ')
            print("  [" + str(elevator[1].getnowP()) + "]")
            elevator[1].enterP(i)
        elif elevator[0].getfloorNow() == i.getnumF() and elevator[1].getfloorNow() != i.getnumF():
            print(i, end=' ')
            print("  [" + str(elevator[0].getnowP()) + "]")
            elevator[1].enterP(i)
        else:
            print(i)
def printG():
    for i in Fl:
        if elevator.getfloorNow() == i.getnumF() :
            print(i, end=' ')
            print("  [" + str(elevator.getnowP()) + "]")
            elevator.enterP(i)
        else:
            print(i)
def proccess():
    while True:
        time.sleep(1)
        printG()
        elevator.trevel(Fl)
        if time.clock()%30 >=0 and time.clock()%30<6:
            addPeople(5)
        print("\n\n")


printe()
proccess()
