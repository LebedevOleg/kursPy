from tkinter import *
import random
import msvcrt
import time
import os
from Elevator import*
from Floor import*
from People import*

floors = []
elevator = []
Fl = []
elev = []
elevt = []
ftext = []

def printe(numF,numE):
    temp = 10
    for i in range(numF):
        floor = Floor(i)
        p = People(numF-1)
        floor.setnumP(p)
        floors.append(10 + i*30)
        Fl.append(floor)
    floors.reverse()
    for i in range(numE):
        el = Elevator()
        elevator.append(el)
    print(floors[0])

def addPeople(x = 3):
    for j in range(1,random.randint(1,x)):
        for i in range(0,random.randint(1,len(Fl))):
            p = People(len(Fl)-1)
            Fl[i].setnumP(p)

def floorwait():
    wait = 0
    for i in Fl:
        wait += i.getAllsumm()
    wait = wait/len(Fl)
    return str(wait)

def elevatorwait():
    wait = 0
    for i in elevator:
        wait += i.getAllsumm()
    wait = wait/len(elevator)
    return str(wait)

def butt2(root,numF,numE):
    build2 = Toplevel(root)
    build2.minsize(width=600,height=700)
    c = Canvas(build2,width = 600,height = 700,bg = 'white')
    c.pack()
    printe(numF,numE)
    Fl[0].build2(build2,c,numF)
    for i in range(numE):
        el = c.create_rectangle(100+ i*40,floors[0],130+ i*40,floors[0]+20,outline = 'BLACK')
        elt = c.create_text(115 + i*40,floors[0]+10,text = "[" + str(elevator[i].getnowP()) + "]")
        elev.append(el)
        elevt.append(elt)
    waitE = c.create_text(460,30,text = "Среднее время \nожидания в лифте: ",anchor = W)
    waitF = c.create_text(460,80,text = "Среднее время \nожидания на этаже: ",anchor = W)
    for i in range(numF):
        f = c.create_text(80,floors[i]+10 ,text = "(" + str(Fl[i].getnumP()) + ")")
        ftext.append(f)
    build2.update()
    while True:
        #region process
        for i in Fl:
            for e in range(len(elevator) -1):
                if elevator[e].getfloorNow() == i.getnumF():
                    elevator[e].enterP(i)
                elevator[e].travel(Fl,elev[e],floors,c,elevt[e])
        if time.clock() % 30 >= 0 and time.clock() % 30 < 4:
            addPeople(5)
        #endregion
        c.itemconfigure(waitF,text = "Среднее время \nожидания на этаже: " + floorwait())
        c.itemconfigure(waitE,text ="Среднее время \nожидания на этаже: " + elevatorwait())
        for i in range(numF):
            c.itemconfig(ftext[i], text="(" + str(Fl[i].getnumP()) + ")")