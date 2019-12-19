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
Elevators = []
ftext = []
def move(build2,elev,c,elevt,numF,type):
    for e in range(0,len(elevator)):
        elevator[e].trevelcustom(Fl, elev[e], floors, c, elevt[e], e, build2)
    build2.update()
    time.sleep(0.25)
    for e in range(0,len(elevator)):
        if elevator[e].cheakt() == 0:
            if type == 4:
                elevator[e].ent(Fl[elevator[e].getfloornow()],Fl)
            move(build2,elev,c,elevt,numF,type)


def printe(numF,numE,type):
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
        el.setfloorNow(random.randint(0,numF-1))
        el.settype(type)
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
def floorwaitmax():
    wait = []
    for i in Fl:
        wait.append(i.max())
    temp = max(wait)
    return str(temp)
def elevatorwait():
    wait = 0
    for i in elevator:
        wait += i.getAllsumm()
    wait = wait/len(elevator)
    return str(wait)

def elevatorwaitmax():
    wait = []
    for i in elevator:
        wait.append(i.max())
    temp = max(wait)
    return str(temp)

def butt2(root,numF,numE,type):
    build2 = Toplevel(root)
    build2.minsize(width=600,height=700)
    c = Canvas(build2,width = 600,height = 700,bg = 'white')
    c.pack()
    if type == 4:
        printe(numF,numE,type-1)
    else:
        printe(numF, numE, type)
    Fl[0].build2(build2,c,numF)
    for i in range(numE):
        el = c.create_rectangle(100+ i*40,floors[elevator[i].getfloornow()],130+ i*40,floors[elevator[i].getfloornow()]+20,outline = 'BLACK')
        elt = c.create_text(115 + i*40,floors[elevator[i].getfloornow()]+10,text = "[" + str(elevator[i].getnowP()) + "]")
        Elevator = c.create_text(500, 500+i*40, text = elevator[i])
        Elevators.append(Elevator)
        elev.append(el)
        elevt.append(elt)
    waitE = c.create_text(430,30,text = "Среднее время \nожидания в лифте: ",anchor = W)
    waitF = c.create_text(430,80,text = "Среднее время \nожидания на этаже: ",anchor = W)
    waitEM = c.create_text(430, 110, text="Максимальное время \nожидания в лифте: ", anchor=W)
    waitFM = c.create_text(430, 150, text="Максимальное время \nожидания на этаже: ", anchor=W)
    for i in range(numF):
        f = c.create_text(80,floors[i]+10 ,text = "(" + str(Fl[i].getnumP()) + ")")
        ftext.append(f)
    build2.update()
    while True:
        #region process
        for i in Fl:
            if len(elevator) >1:
                for e in range(0,len(elevator)):
                    if elevator[e].getfloorNow() == i.getnumF():
                        elevator[e].enterP(i,numF,Fl,elevator)
                        c.itemconfigure(elevt[e], text="[" + elevator[e].strgetnowP() + "]")
                        c.itemconfig(Elevators[e], text=elevator[e])
            elif len(elevator) == 1:
                if elevator[0].getfloorNow() == i.getnumF():
                    elevator[0].enterP(i, numF, Fl)
                    elevator[0].trevel(Fl, elev[0], floors, c, elevt[0])
        move(build2,elev,c,elevt,numF,type)
        for e in range(0, len(elevator)):
            elevator[e].setcheak(0)
        # for e in range(0, len(elevator)):
        #     elevator[e].trevelcustom(Fl,elev[e],floors,c,elevt[e],e,build2)
        #     build2.update()
        if time.clock() % 45 >= 0 and time.clock() % 45 < 4:
            addPeople(5)
        else:
            addPeople()
        #endregion
        c.itemconfigure(waitF,text = "Среднее время \nожидания на этаже: " + floorwait())
        c.itemconfigure(waitE,text ="Среднее время \nожидания в лифте: " + elevatorwait())
        c.itemconfig(waitFM,text = "Максимальное время \nожидания на этаже: "+ floorwaitmax())
        c.itemconfig(waitEM,text = "Максимальное время \nожидания в лифте: "+  elevatorwaitmax())
        for i in range(numF):
            c.itemconfig(ftext[i], text="(" + str(Fl[i].getnumP()) + ")")
        for i in range(numE):
            c.itemconfigure(elevt[i], text = "[" + elevator[i].strgetnowP() + "]")
        build2.update()
        print("end")
      #  build2.update()