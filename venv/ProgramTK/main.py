from tkinter import *
import random
import msvcrt
import time
import os
from Elevator import*
from Floor import*
from People import*
floors = [200,170,140,110,80,50,20]

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

def proccess(el):
    while True:
        time.sleep(1)
        for i in Fl:
            if elevator.getfloorNow() == i.getnumF():
                elevator.enterP(i)
        elevator.trevel(Fl,el,floors)
        if time.clock()%30 >=0 and time.clock()%30<6:
            addPeople(5)

def butt1():
    build1 = Toplevel(root)
    build1.minsize(width=200,height=300)
    printe()
    Fl[0].build1(build1)
    el = Label(build1,text = "lift" + " [" + str(elevator.getnowP()) + "]")
    el.place(x = 120,y = floors[0])
    proccess(el)




root =Tk()

but1 = Button(root,text = "7 этажей 1 лифт", command = butt1)
but1.pack()

root.mainloop()