from tkinter import *
def golova():
        global var_golova
        global c
        if var_golova.get()=="1":
            c.create_oval((15,15,450,500),fill="white")
        elif var_golova.get()=="0":
            c.create_oval((15,15,450,500),outline="black")
tk = Tk()
fm=Frame(tk)
fm.pack(side=RIGHT)
c = Canvas(tk, width=1000, height=500, bg="white") 
c.create_oval((15,15,450,500))
c.create_oval((125,100,175,150))
c.create_oval((250,100,300,150))
c.create_arc((175,200,350,350))
c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150)
c.pack(side=LEFT)
var_golova=StringVar()
golova=Checkbutton(fm,text="Голова",font="Calibri 26", fg="green",variable=var_golova,onvalue="1",offvalue="0",command=golova)
var_rot=StringVar()
rot=Checkbutton(fm,text="Рот",font="Calibri 26", fg="green",variable=var_rot,onvalue="1",offvalue="0")
var_nos=StringVar()
nos=Checkbutton(fm,text="Нос",font="Calibri 26", fg="green",variable=var_nos,onvalue="1",offvalue="0")
var_glaz=StringVar()
glaz=Checkbutton(fm,text="Глаз левый",font="Calibri 26", fg="green",variable=var_glaz,onvalue="1",offvalue="0")
var_glaz2=StringVar()
glaz2=Checkbutton(fm,text="Глаз правый",font="Calibri 26", fg="green",variable=var_glaz2,onvalue="1",offvalue="0")
golova.pack(side=RIGHT)
rot.pack(side=RIGHT)
nos.pack(side=RIGHT)
glaz.pack(side=RIGHT)
glaz2.pack(side=RIGHT)
tk.mainloop()