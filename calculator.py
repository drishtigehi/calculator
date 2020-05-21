#!/usr/bin/env python3
from tkinter import *

root=Tk()
root.title("SCIENTIFIC CALCULATOR")#add sq,sqrt,inv,sin,cos,tan,sininv,scientific basically +one unique feature

def button_click(number): # get numbers
    
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear(): #clear input box
    e.delete(0,END)
    return

def button_add():
    first_no=e.get()
    global f_num
    global math
    math="add"
    f_num=int(first_no)
    e.delete(0,END)

def button_sub():
    first_no=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(first_no)
    e.delete(0,END)

def button_mul():
    first_no=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(first_no)
    e.delete(0,END)

def button_div():
    first_no=e.get()
    global f_num
    global math
    math="div"
    f_num=float(first_no) #imp
    e.delete(0,END)

def button_equal():
    second_no=e.get()
    e.delete(0,END)

    if math=="add":
        e.insert(0,f_num + int(second_no))
    if math=="sub":
        e.insert(0,f_num - int(second_no))
    if math=="mul":
        e.insert(0,f_num * int(second_no))
    if math=="div":
        e.insert(0,f_num / float(second_no))


#Defining the buttons
button_0=Button(root,text="0",padx=30,pady=20,command= lambda: button_click(0)) #can't put button_clck() coz then it will auto execute 

button_1=Button(root,text="1",padx=30,pady=20,command=lambda: button_click(1)) #we want to execute it when it is clicked
button_2=Button(root,text="2",padx=30,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=30,pady=20,command=lambda: button_click(3))

button_4=Button(root,text="4",padx=30,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=30,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=30,pady=20,command=lambda: button_click(6))

button_7=Button(root,text="7",padx=30,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=30,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=30,pady=20,command=lambda: button_click(9))

button_equal1=Button(root,text="=",padx=30,pady=20,command=button_equal)

button_add1=Button(root,text="+",padx=30,pady=20,command=button_add)
button_sub1=Button(root,text="-",padx=30,pady=20,command= button_sub)
button_mul1=Button(root,text="*",padx=30,pady=20,command= button_mul)
button_div1=Button(root,text="/",padx=30,pady=20,command= button_div)

button_clc=Button(root,text="CE",padx=30,pady=20,command=button_clear)#deletes everything,no lambda we dont pass anything to the function
button_quit=Button(root,text="QUIT",padx=30,pady=20,command=root.quit)
button_equal=Button(root,text="=",padx=30,pady=20,command=button_equal)

#Place the buttons
button_0.grid(row=4,column=1)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add1.grid(row=1,column=3)
button_sub1.grid(row=2,column=3)
button_mul1.grid(row=3,column=3)
button_div1.grid(row=4,column=2)

button_clc.grid(row=4,column=0)
button_quit.grid(row=5,column=0)
button_equal1.grid(row=5,column=1)


#Entry Box
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,columnspan=3)
e.insert(0," ")

root.mainloop()