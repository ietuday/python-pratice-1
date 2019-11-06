"""
FRONT-END
A Program that stores this book information:
Title,Author,Year ,ISBN

Functional Requirements:
View all records
Search an entry
Add an entry
Update an entry
Delete
Close the program
"""
from tkinter import *

import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    t1 = title_value.get()
    a1 = author_value.get()
    y1 = year_value.get()
    i1 = isbn_value.get()
    list1.delete(0,END)
    for row in backend.search(t1,a1,y1,i1):
        list1.insert(END,row)

def insert_command():
    t1 = title_value.get()
    a1 = author_value.get()
    y1 = year_value.get()
    i1 = isbn_value.get()
    backend.insert(t1,a1,y1,i1)
    list1.delete(0,END)
    list1.insert(END,(t1,a1,y1,i1))

def get_selected_row(event):
    #This object is a tuple
    global selected_tuple
    if(len(list1.curselection())!=0):
        index          = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])

        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])

        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0,END)
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(), isbn_value.get())
    list1.delete(0,END)
    view_command()





window = Tk()

window.wm_title("BookStore")



l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

#Title
title_value = StringVar()
e1 = Entry(window,textvariable=title_value)
e1.grid(row=0,column=1)
#Author
author_value = StringVar()
e2 = Entry(window,textvariable=author_value)
e2.grid(row=0,column=3)
#Year
year_value = StringVar()
e3 = Entry(window,textvariable=year_value)
e3.grid(row=1,column=1)
#ISBN
isbn_value = StringVar()
e4 = Entry(window,textvariable=isbn_value)
e4.grid(row=1,column=3)

#List
list1 = Listbox(window, height=10,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#Buttons
b1 = Button(window, text="View All",width=12, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search Entry",width=12, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add Entry",width=12, command=insert_command)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update",width=12, command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text="Delete",width=12, command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text="Close",width=12, command=window.destroy)
b6.grid(row=7,column=3)

view_command()

window.mainloop()
