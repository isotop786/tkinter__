import tkinter
from tkinter import *

mile =0;


def convert():
    val = float(e1_value.get())*1.6
    print(val)
    t1.insert(END,val)
    t1.insert(END,none)


window =Tk("hey")
window.title("Kilometer to Mile Convertor.")

b1 = Button(window,text="Convert",command=convert)
b1.grid(row=0,column=3,rowspan=2)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=0,rowspan=3)

t1 = Text(window,height=1,width=20)

t1.grid(row=0,column=5,rowspan=3)




window.mainloop()