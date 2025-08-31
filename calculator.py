from tkinter import *

cal = Tk()
cal.title("Calculator")
cal.geometry("400x450")
cal.resizable(True, True)


def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))   

def clear():
    e.delete(0,END)    


def add():
    n1 = e.get()
    global i
    global math 
    math = "addition"
    i =  int(n1)
    e.delete(0,END)

def minus():
    n1 = e.get()
    global i
    global math 
    math = "subtraction"
    i =  int(n1)
    e.delete(0,END)


def mul():
    n1 = e.get()
    global i
    global math 
    math = "multiplication"
    i =  int(n1)
    e.delete(0,END)


def div():
    n1 = e.get()
    global i
    global math 
    math = "division"
    i =  int(n1)
    e.delete(0,END)

def calculation():
    n2 = e.get()
    e.delete(0,END)
    
    if math=="addition":
        e.insert(0,i+int(n2))
    elif math=="subtraction":
        e.insert(0,i-int(n2))    
    elif math=="multiplication":
        e.insert(0,i*int(n2))
    elif math=="division":
        e.insert(0,i / int(n2))
    else:
        e.insert("Error")

e= Entry(cal, font=("Arial", 20), bd=5, justify="right")
e.place(x=0,y=0)

b= Button (cal,text='1', width=5, height=2,  font=("Arial", 14),padx=5, pady=5,command=lambda:click(1))
b.place(x=10,y=50)

b= Button (cal,text='2', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(2))
b.place(x=80,y=50)

b= Button (cal,text='3', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(3))
b.place(x=150,y=50)

b= Button (cal,text='4', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(4))
b.place(x=220,y=50)

b= Button (cal,text='+', width=5, height=2, font=("Arial", 14),padx=5, pady=5, command=add)
b.place(x=220,y=50)

b= Button (cal,text='5', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(5))
b.place(x=10,y=120)

b= Button (cal,text='6', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(6))
b.place(x=80,y=120)

b= Button (cal,text='7', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(7))
b.place(x=150,y=120)

b= Button (cal,text='-', width=5, height=2, font=("Arial", 14),padx=5, pady=5, command=minus)
b.place(x=220,y=120)

b= Button (cal,text='8', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(8))
b.place(x=10,y=190)

b= Button (cal,text='9', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(9))
b.place(x=80,y=190)

b= Button (cal,text='0', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=lambda:click(0))
b.place(x=150,y=190)

b= Button (cal,text='*', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=mul)
b.place(x=220,y=190)

b= Button (cal,text='clear', width=12, height=2, font=("Arial", 14),padx=5, pady=5, command=clear)
b.place(x=10,y=260)

b= Button (cal,text='=', width=5, height=2, font=("Arial", 14),padx=5, pady=5, command=calculation)
b.place(x=150,y=260)

b= Button (cal,text='/', width=5, height=2, font=("Arial", 14),padx=5, pady=5,command=div)
b.place(x=220,y=260)


cal.mainloop()