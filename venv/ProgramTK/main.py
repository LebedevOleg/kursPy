from tkinter import *
import random
import msvcrt
import time
import os
from Elevator import*
from Floor import*
from People import*
floors = [180,150,130,90,60,30,0]

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

def proccess(el,build1,c,elt):
        time.sleep(1)
        for i in Fl:
            if elevator.getfloorNow() == i.getnumF():
                elevator.enterP(i)
        elevator.trevel(Fl,el,floors,c,elt)
        if time.clock()%30 >=0 and time.clock()%30<6:
            addPeople(5)
def butt1():
    build1 = Toplevel(root)
    build1.minsize(width=200,height=300)
    c = Canvas(build1,width = 200, height = 300, bg = 'white')
    c.pack()
    printe()
    Fl[0].build1(build1,c)
    el = c.create_rectangle(100,floors[0],130,floors[0]+20,outline='BLACK')
    elt = c.create_text(115,floors[0]+10,text = "[" + str(elevator.getnowP()) + "]")
    while True:
        proccess(el,build1,c,elt)



    #el = Button(build1,text = "lift" + " [" + str(elevator.getnowP()) + "]")
    #el.place(x = 120,y = floors[0])
    #while True:
    #    proccess(el,build1)
     #   el.configure(text = "lift" + " [" + str(elevator.getnowP()) + "]")
      #  build1.update()
       # build1.mainloop()




root =Tk()

but1 = Button(root,text = "7 этажей 1 лифт", command = butt1)
but1.pack()

root.mainloop()