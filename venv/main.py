from tkinter import *
import random
import msvcrt
import time
import traceback
from tkinter import messagebox
import os
from Elevator import*
from Floor import*
from People import*
from Customizer import butt2

floors = [190,160,130,100,70,40,10]
elevator = Elevator()
Fl = []
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

# def proccess(el,build1,c,elt):
#         for i in Fl:
#             if elevator.getfloorNow() == i.getnumF():
#                 elevator.enterP(i)
#         elevator.trevel(Fl,el,floors,c,elt)
#         if time.clock()%30 >=0 and time.clock()%30<6:
#             addPeople(5)

def floorwait():
    wait = 0
    for i in Fl:
        wait += i.getAllsumm()
    wait = wait/len(Fl)
    return str(wait)
def butt1():
    build1 = Toplevel(root)
    build1.minsize(width=300,height=300)
    c = Canvas(build1,width = 300, height = 300, bg = 'white')
    c.pack()
    printe()
    Fl[0].build1(build1,c)
    el = c.create_rectangle(100,floors[0],130,floors[0]+20,outline='BLACK')
    elt = c.create_text(115,floors[0]+10,text = "[" + str(elevator.getnowP()) + "]")
    waitE = c.create_text(150,30,text = "Среднее время \nожидания в лифте: "+ elevator.getTwait(),anchor = W)
    waitF = c.create_text(150,80,text = "Среднее время \nожидания на этаже: ",anchor = W)
    f1 = c.create_text(80,200,text = "(" + str(Fl[0].getnumP()) + ")")
    f2 = c.create_text(80, 170, text="(" + str(Fl[1].getnumP()) + ")")
    f3 = c.create_text(80, 140, text="(" + str(Fl[2].getnumP()) + ")")
    f4 = c.create_text(80, 110, text="(" + str(Fl[3].getnumP()) + ")")
    f5 = c.create_text(80, 80, text="(" + str(Fl[4].getnumP()) + ")")
    f6 = c.create_text(80, 50, text="(" + str(Fl[5].getnumP()) + ")")
    f7 = c.create_text(80, 20, text="(" + str(Fl[6].getnumP()) + ")")
    build1.update()
    while True:
#startreg process
        for i in Fl:
            if elevator.getfloorNow() == i.getnumF():
                elevator.enterP(i)
        elevator.trevel(Fl, el, floors, c, elt)
        if time.clock() % 30 >= 0 and time.clock() % 30 < 4:
            addPeople(5)
        else:
            addPeople()
#endreg
        c.itemconfig(waitE,text = "Среднее время \nожидания в лифте: "+  elevator.getTwait())
        c.itemconfig(waitF,text = "Среднее время \nожидания на этаже: "+ floorwait() )
        c.itemconfig(elt, text="[" + str(elevator.getnowP()) + "]")
        c.itemconfig(f1,text = "(" + str(Fl[0].getnumP()) + ")")
        c.itemconfig(f2,text = "(" + str(Fl[1].getnumP()) + ")")
        c.itemconfig(f3,text = "(" + str(Fl[2].getnumP()) + ")")
        c.itemconfig(f4, text="(" + str(Fl[3].getnumP()) + ")")
        c.itemconfig(f5, text="(" + str(Fl[4].getnumP()) + ")")
        c.itemconfig(f6, text="(" + str(Fl[5].getnumP()) + ")")
        c.itemconfig(f7, text="(" + str(Fl[6].getnumP()) + ")")
        build1.update()
def butt22():
    trash = Toplevel(root)
    label1 = Label(trash,text = "Введите колличество этажей")
    textA =Entry(trash)
    label2 = Label(trash,text = "Введите колличество лифтов")
    textB = Entry(trash)
    but = Button(trash,text = "Запуск",command = lambda: com1(textA,textB))
    label1.grid(column=0, row=0)
    textA.grid(column=0, row=1)
    label2.grid(column=1, row=0)
    textB.grid(column=1, row=1)
    but.grid(column=1, row=2)
def com1(textA,textB):
    numF = textA.get()
    numE = textB.get()
    try:
      if int(numF) <0 or int(numE) < 0:
            messagebox.showinfo("Error","Вы ввели неправильные данные")
      else:
            butt2(root,int(numF),int(numE))
    except:
        messagebox.showinfo("Error", traceback.format_exc() )


root =Tk()

but1 = Button(root,text = "7 этажей 1 лифт", command = butt1)
but1.pack()
but2 = Button(root,text = "Кастомный дом", command = butt22)
but2.pack()

root.mainloop()