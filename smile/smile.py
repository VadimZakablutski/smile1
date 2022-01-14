from tkinter import *
def golova1():
        global var_golova
        global c
        if var_golova.get()=="1":
            c.create_oval((15,15,450,500),fill="white",outline="white")
            c.create_oval((250,100,300,150))
            c.create_oval((125,100,175,150))
            c.create_arc((175,200,350,350),outline="black")
            c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="black")
        elif var_golova.get()=="0":
            c.create_oval((15,15,450,500),fill="orange",outline="black")
            c.create_oval((250,100,300,150))
            c.create_oval((125,100,175,150))
            c.create_arc((175,200,350,350),outline="black")
            c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="black")
def glaz1():
    global var_glaz1
    global c
    if var_glaz1.get()=="1":
        c.create_oval((250,100,300,150))
    elif var_glaz1.get()=="0":
       c.create_oval((250,100,300,150),outline="orange")
def glaz2():
    global var_glaz2
    global c
    if var_glaz2.get()=="1":
        c.create_oval((125,100,175,150))    
    elif var_glaz2.get()=="0":
        c.create_oval((125,100,175,150),outline="orange")
def nos():
    if var_nos.get()=="1":
        c.create_arc((175,200,350,350),outline="orange")
    elif var_nos.get()=="0":
        c.create_arc((175,200,350,350),outline="black")
def rot():
    if var_rot.get()=="1":
        c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="orange")
    elif var_rot.get()=="0":
        c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="black")
tk = Tk()
fm=Frame(tk)
fm.pack(side=RIGHT)
c = Canvas(tk, width=500, height=500, bg="white") 
c.create_oval((15,15,450,500),fill="orange")#golova
c.create_oval((125,100,175,150))#glaz1
c.create_oval((250,100,300,150))#glaz2
c.create_arc((175,200,350,350))#nos
c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150)#rot
c.pack(side=LEFT)
var_golova=StringVar()
golova=Checkbutton(fm,text="Голова",font="Calibri 26", fg="blue",variable=var_golova,onvalue="1",offvalue="0",command=golova1)
var_glaz1=StringVar()
glaz1=Checkbutton(fm,text="Правый глаз",font="Calibri 26", fg="blue",variable=var_glaz1,onvalue="1",offvalue="0",command=glaz1)
var_glaz2=StringVar()
glaz2=Checkbutton(fm,text="Левый глаз",font="Calibri 26", fg="blue",variable=var_glaz2,onvalue="1",offvalue="0",command=glaz2)
var_rot=StringVar()
rot=Checkbutton(fm,text="Рот",font="Calibri 26", fg="blue",variable=var_rot,onvalue="1",offvalue="0",command=rot)
var_nos=StringVar()
nos=Checkbutton(fm,text="Нос",font="Calibri 26", fg="blue",variable=var_nos,onvalue="1",offvalue="0",command=nos)
golova.pack(side=RIGHT)
rot.pack(side=RIGHT)
nos.pack(side=RIGHT)
glaz1.pack(side=RIGHT)
glaz2.pack(side=RIGHT)
tk.mainloop()