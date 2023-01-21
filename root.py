from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = Tk()
root.config(bg="#002b36")
root.geometry("500x500")
root.resizable(False, False)
root.title("Tic, Tac, Toe!")
root.iconbitmap("ikonica.ico")





class Counter:
    counter=0
    positions = [12, -1, -15, -6, 8, 90, 30, 4, 5]
    results = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    pobeda = 0


def x_win():
    x = Toplevel()
    x.config(bg="#002b36")
    x.geometry("200x200")
    x.resizable(False, False)
    x.iconbitmap("ikonica.ico")
    x.title("Tic, Tac, Toe!")
    Counter.pobeda = 1
    Label(x, text="X WON!", fg="white", bg="#002b36", font=("Arial", 25)).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(x, text="RESET", fg="white", bg="#002b36", bd=0,font=("Arial", 10), command=lambda:(reset(), x.destroy())).place(relx=0.5, rely=0.7, anchor=CENTER)

def o_win():
    o = Toplevel()
    o.config(bg="#002b36")
    o.geometry("200x200")
    o.resizable(False, False)
    o.iconbitmap("ikonica.ico")
    o.title("Tic, Tac, Toe!")
    Counter.pobeda = 1
    Label(o, text="O WON!", fg="white", bg="#002b36", font=("Arial", 25)).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(o, text="RESET", fg="white", bg="#002b36", bd=0, font=("Arial", 10),  command=lambda:(reset(), o.destroy())).place(relx=0.5, rely=0.7, anchor=CENTER)

def nereseno():
    o = Toplevel()
    o.config(bg="#002b36")
    o.geometry("200x200")
    o.resizable(False, False)
    o.iconbitmap("ikonica.ico")
    o.title("Tic, Tac, Toe!")
    Counter.pobeda = 1
    Label(o, text="DRAW!", fg="white", bg="#002b36", font=("Arial", 25)).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(o, text="RESET", fg="white", bg="#002b36", bd=0, font=("Arial", 10),  command=lambda:(reset(), o.destroy())).place(relx=0.5, rely=0.7, anchor=CENTER)

def reset():
    Buttons.center.config(text="", fg="white")
    Buttons.left.config(text="", fg="white")
    Buttons.right.config(text="", fg="white")
    Buttons.top_left.config(text="", fg="white")
    Buttons.top.config(text="", fg="white")
    Buttons.top_right.config(text="", fg="white")
    Buttons.bottom_left.config(text="", fg="white")
    Buttons.bottom.config(text="", fg="white")
    Buttons.bottom_right.config(text="", fg="white")
    Counter.positions = [12, -1, -15, -6, 8, 90, 30, 4, 5]
    Counter.results = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    Counter.counter=0
    Counter.pobeda = 0

def tl():
    Counter.results[0] = 1
    if Counter.counter==0:
        Buttons.top_left.config(text="X")
        Counter.counter+=1
        Counter.positions[0] = 1
                                    
    else:
        Buttons.top_left.config(text="O")
        Counter.counter-=1
        Counter.positions[0] = 0   
    process()
def t():
    Counter.results[1] = 1
    if Counter.counter==0:
        Buttons.top.config(text="X")
        Counter.counter+=1 
        Counter.positions[1] = 1                              
    else:
        Buttons.top.config(text="O")
        Counter.counter-=1
        Counter.positions[1] = 0     
    process()
def tr():
    Counter.results[2] = 1
    if Counter.counter==0:
        Buttons.top_right.config(text="X")
        Counter.counter+=1   
        Counter.positions[2] = 1                            
    else:
        Buttons.top_right.config(text="O")
        Counter.counter-=1 
        Counter.positions[2] = 0   
    process()
def l():
    Counter.results[3] = 1
    if Counter.counter==0:
        Buttons.left.config(text="X")
        Counter.counter+=1
        Counter.positions[3] = 1                               
    else:
        Buttons.left.config(text="O")
        Counter.counter-=1 
        Counter.positions[3] = 0   
    process()
def c():
    Counter.results[4] = 1
    if Counter.counter==0:
        Buttons.center.config(text="X")
        Counter.counter+=1
        Counter.positions[4] = 1                               
    else:
        Buttons.center.config(text="O")
        Counter.counter-=1 
        Counter.positions[4] = 0  
    process()
def r():
    Counter.results[5] = 1
    if Counter.counter==0:
        Buttons.right.config(text="X")
        Counter.counter+=1 
        Counter.positions[5] = 1                              
    else:
        Buttons.right.config(text="O")
        Counter.counter-=1 
        Counter.positions[5] = 0  
    process()
def bl():
    Counter.results[6] = 1
    if Counter.counter==0:
        Buttons.bottom_left.config(text="X")
        Counter.counter+=1 
        Counter.positions[6] = 1                              
    else:
        Buttons.bottom_left.config(text="O")
        Counter.counter-=1 
        Counter.positions[6] = 0  
    process()
def b():
    Counter.results[7] = 1
    if Counter.counter==0:
        Buttons.bottom.config(text="X")
        Counter.counter+=1 
        Counter.positions[7] = 1                              
    else:
        Buttons.bottom.config(text="O")
        Counter.counter-=1 
        Counter.positions[7] = 0  
    process()
def br():
    Counter.results[8] = 1
    if Counter.counter==0:
        Buttons.bottom_right.config(text="X")
        Counter.counter+=1 
        Counter.positions[8] = 1                              
    else:
        Buttons.bottom_right.config(text="O")
        Counter.counter-=1 
        Counter.positions[8] = 0   
    process()
class Buttons:
    top_left = Button(root, command=tl, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    top = Button(root, command=t, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    top_right = Button(root, command=tr, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    left = Button(root, command=l, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    center = Button(root, command=c, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    right = Button(root, command=r, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    bottom_left = Button(root, command=bl, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    bottom = Button(root, command=b, font=("Arial", 40), bg="#002b36", fg="white", bd=0)
    bottom_right = Button(root, command=br, font=("Arial", 40), bg="#002b36", fg="white", bd=0)


naslov = Label(root, text="TIC, TAC, TOE!", bg="#002b36", fg="white", font=("Helvetica", 30))
naslov.pack(pady=20)

uspravna1 = Label(root, text="I",  bg="#002b36", fg="white", font=("Helvetica", 40))
uspravna2 = Label(root, text="I",  bg="#002b36", fg="white", font=("Helvetica", 40))
uspravna3 = Label(root, text="I",  bg="#002b36", fg="white", font=("Helvetica", 40))
uspravna4 = Label(root, text="I",  bg="#002b36", fg="white", font=("Helvetica", 40))
uspravna5 = Label(root, text="I",  bg="#002b36", fg="white", font=("Helvetica", 40))
uspravna6 = Label(root, text="I",  bg="#002b36", fg="white", font=("Helvetica", 40))

horizontalna1 = Label(root, text="---",  bg="#002b36", fg="white", font=("Helvetica", 30))
horizontalna2 = Label(root, text="---",  bg="#002b36", fg="white", font=("Helvetica", 30))
horizontalna3 = Label(root, text="---",  bg="#002b36", fg="white", font=("Helvetica", 30))
horizontalna4 = Label(root, text="---",  bg="#002b36", fg="white", font=("Helvetica", 30))
horizontalna5 = Label(root, text="---",  bg="#002b36", fg="white", font=("Helvetica", 30))
horizontalna6 = Label(root, text="---",  bg="#002b36", fg="white", font=("Helvetica", 30))

Buttons.center.place(relx=0.5, rely=0.5, anchor=CENTER)
Buttons.left.place(relx=0.3, rely=0.5, anchor=CENTER)
Buttons.right.place(relx=0.7, rely=0.5, anchor=CENTER)
Buttons.top_left.place(relx=0.3, rely=0.3, anchor=CENTER)
Buttons.top.place(relx=0.5, rely=0.3, anchor=CENTER)
Buttons.top_right.place(relx=0.7, rely=0.3, anchor=CENTER)
Buttons.bottom_left.place(relx=0.3, rely=0.7, anchor=CENTER)
Buttons.bottom.place(relx=0.5, rely=0.7, anchor=CENTER)
Buttons.bottom_right.place(relx=0.7, rely=0.7, anchor=CENTER)

uspravna1.place(relx=0.4, rely=0.3, anchor=CENTER)
uspravna2.place(relx=0.6, rely=0.3, anchor=CENTER)
uspravna3.place(relx=0.4, rely=0.5, anchor=CENTER)
uspravna4.place(relx=0.6, rely=0.5, anchor=CENTER)
uspravna5.place(relx=0.4, rely=0.7, anchor=CENTER)
uspravna6.place(relx=0.6, rely=0.7, anchor=CENTER)

horizontalna1.place(relx=0.3, rely=0.4, anchor=CENTER)
horizontalna2.place(relx=0.3, rely=0.6, anchor=CENTER)
horizontalna3.place(relx=0.5, rely=0.4, anchor=CENTER)
horizontalna4.place(relx=0.5, rely=0.6, anchor=CENTER)
horizontalna5.place(relx=0.7, rely=0.4, anchor=CENTER)
horizontalna6.place(relx=0.7, rely=0.6, anchor=CENTER)



komentar = Label(root, text="X goes first!",bg="#002b36", fg="white", font=("Helvetica", 15))
komentar.place(relx=0.5, rely=0.9, anchor=CENTER)


Button(root, text="RESET", fg="white", bg="#002b36", bd=0, font=("Helvetica", 10),  command=reset).place(relx=0.9, rely=0.93, anchor=CENTER)

def process():
    if(Counter.positions[0] == Counter.positions[1] == Counter.positions[2] and Counter.pobeda == 0):
        Buttons.top_left.config(fg="green")
        Buttons.top.config(fg="green")
        Buttons.top_right.config(fg="green")
        if Counter.positions[0] == 1:
            x_win()
            
        elif Counter.positions[0] ==0:
            o_win()

    if(Counter.positions[0] == Counter.positions[3] == Counter.positions[6] and Counter.pobeda == 0):
        Buttons.top_left.config(fg="green")
        Buttons.left.config(fg="green")
        Buttons.bottom_left.config(fg="green")
        if Counter.positions[0] == 1:
            x_win()
        elif Counter.positions[0] ==0:
            o_win()

    if(Counter.positions[0] == Counter.positions[4] == Counter.positions[8] and Counter.pobeda == 0):
        Buttons.top_left.config(fg="green")
        Buttons.center.config(fg="green")
        Buttons.bottom_right.config(fg="green")
        if Counter.positions[0] == 1:
            x_win()
        elif Counter.positions[0] ==0:
            o_win()

    if(Counter.positions[4] == Counter.positions[1] == Counter.positions[7] and Counter.pobeda == 0):
        Buttons.top.config(fg="green")
        Buttons.center.config(fg="green")
        Buttons.bottom.config(fg="green")
        if Counter.positions[1] == 1:
            x_win()
        elif Counter.positions[1] ==0:
            o_win()

    if(Counter.positions[8] == Counter.positions[5] == Counter.positions[2] and Counter.pobeda == 0):
        Buttons.top_right.config(fg="green")
        Buttons.right.config(fg="green")
        Buttons.bottom_right.config(fg="green")
        if Counter.positions[8] == 1:
            x_win()
        elif Counter.positions[8] ==0:
            o_win()

    if(Counter.positions[6] == Counter.positions[4] == Counter.positions[2] and Counter.pobeda == 0):
        Buttons.top_right.config(fg="green")
        Buttons.center.config(fg="green")
        Buttons.bottom_left.config(fg="green")
        if Counter.positions[2] == 1:
            x_win()
        elif Counter.positions[2] ==0:
            o_win()

    if(Counter.positions[3] == Counter.positions[4] == Counter.positions[5] and Counter.pobeda == 0):
        Buttons.left.config(fg="green")
        Buttons.center.config(fg="green")
        Buttons.right.config(fg="green")
        if Counter.positions[3] == 1:
            x_win()
        elif Counter.positions[3] ==0:
            o_win()

    if(Counter.positions[6] == Counter.positions[7] == Counter.positions[8] and Counter.pobeda == 0):
        Buttons.bottom_left.config(fg="green")
        Buttons.bottom.config(fg="green")
        Buttons.bottom_right.config(fg="green")
        if Counter.positions[6] == 1:
            x_win()
        elif Counter.positions[6] ==0:
            o_win()

    if (Counter.pobeda == 0 and Counter.results == [1,1,1,1,1,1,1,1,1]):
        nereseno()

root.mainloop()