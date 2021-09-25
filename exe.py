"""Unit converter"""

from tkinter import *

units = {
    "grams":0,
    "pounds":0,
    "ounce": 0
}

def convert():
    tp.delete('1.0',END)
    tg.delete('1.0',END)
    to.delete('1.0',END)
    try:
        var = float(value.get())
        print(type(var))
    except ValueError:
        # w =Tk()
        # w.title("error")
        # l = Label(w,text="Only Numeric Values are allowed")
        # l.grid(row=0,column=1,rowspan=3)
        # en.delete(0,'end')
        # w.mainloop()
        la = Label(window,text="Only Numeric Values are allowed")
        la.grid(row=3,column=1)
        
    else:
        
        units["grams"] =var *1000
        units["pounds"] = var *2.20462
        units["ounce"] = var * 35.274
        print(units["grams"])
        tg.insert(END,units["grams"])
        tp.insert(END,units["pounds"])
        to.insert(END,units["ounce"])

def clear():
    tp.delete('1.0',END)
    tg.delete('1.0',END)
    to.delete('1.0',END)
    en.delete(0,'end')

window = Tk()
window.title("Unit Convertor")
window.geometry("500x200")





label = Label(window,text=" Kg")
label.grid(row=0,column=0,rowspan=1)

value = StringVar()
en = Entry(window,textvariable=value)
en.grid(row=0,column=2,rowspan=2)

btn =Button(window,text="Convert",command=convert)
btn.grid(row=0,column=5,rowspan=2)
btn =Button(window,text="Clear",command=clear)
btn.grid(row=0,column=6,rowspan=2)

lg = Label(window,text="   Grams: ")
lg.grid(row=4,column=0)
tg = Text(window,height=1,width=20)
tg.grid(row=4, column=1)
l = Label(window)
l.grid(row=3,column=0)

""""for pounds """
lp = Label(window,text="   Pounds: ")
lp.grid(row=5,column=0)
tp = Text(window,height=1,width=20)
tp.grid(row=5, column=1)


"""for ounce"""
lo = Label(window,text="    Ounces: ")
lo.grid(row=6,column=0)
to = Text(window,height=1, width=20)
to.grid(row=6,column=1)



window.mainloop()