from tkinter import *

window = Tk()
def convertKg():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

l1=Label(window,text="Kg")
l1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convertKg)
b1.grid(row=0, column=2)

#Grams
t1 = Text(window, height=1, width=20)
t1.grid(row=1,column=0)

#Pounds
t2 = Text(window, height=1, width=20)
t2.grid(row=1,column=1)

#Ounces
t3 = Text(window, height=1, width=20)
t3.grid(row=1,column=2)




window.mainloop()
