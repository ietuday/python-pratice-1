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

from backend import Database

db = Database("books.db")


class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("BookStore")
        l1 = Label(window,text="Title")
        l1.grid(row=0,column=0)

        l2 = Label(window,text="Author")
        l2.grid(row=0,column=2)

        l3 = Label(window,text="Year")
        l3.grid(row=1,column=0)

        l4 = Label(window,text="ISBN")
        l4.grid(row=1,column=2)

        #Title
        self.title_value = StringVar()
        self.e1 = Entry(window,textvariable=self.title_value)
        self.e1.grid(row=0,column=1)
        #Author
        self.author_value = StringVar()
        self.e2 = Entry(window,textvariable=self.author_value)
        self.e2.grid(row=0,column=3)
        #Year
        self.year_value = StringVar()
        self.e3 = Entry(window,textvariable=self.year_value)
        self.e3.grid(row=1,column=1)
        #ISBN
        self.isbn_value = StringVar()
        self.e4 = Entry(window,textvariable=self.isbn_value)
        self.e4.grid(row=1,column=3)

        #List
        self.list1 = Listbox(window, height=10,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        #Scrollbar
        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #Buttons
        b1 = Button(window, text="View All",width=12, command=self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window, text="Search Entry",width=12, command=self.search_command)
        b2.grid(row=3,column=3)

        b3 = Button(window, text="Add Entry",width=12, command=self.insert_command)
        b3.grid(row=4,column=3)

        b4 = Button(window, text="Update",width=12, command=self.update_command)
        b4.grid(row=5,column=3)

        b5 = Button(window, text="Delete",width=12, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6 = Button(window, text="Close",width=12, command=window.destroy)
        b6.grid(row=7,column=3)

    def view_command(self):
        self.list1.delete(0,END)
        for row in db.view():
            self.list1.insert(END,row)

    def search_command(self):
        t1 = self.title_value.get()
        a1 = self.author_value.get()
        y1 = self.year_value.get()
        i1 = self.isbn_value.get()
        self.list1.delete(0,END)
        for row in db.search(t1,a1,y1,i1):
            self.list1.insert(END,row)

    def insert_command(self):
        t1 = self.title_value.get()
        a1 = self.author_value.get()
        y1 = self.year_value.get()
        i1 = self.isbn_value.get()
        db.insert(t1,a1,y1,i1)
        self.list1.delete(0,END)
        self.list1.insert(END,(t1,a1,y1,i1))

    def get_selected_row(self,event):
        #This object is a tuple
        global selected_tuple
        if(len(self.list1.curselection())!=0):
            index          = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END, self.selected_tuple[1])

            self.e2.delete(0,END)
            self.e2.insert(END, self.selected_tuple[2])

            self.e3.delete(0,END)
            self.e3.insert(END, self.selected_tuple[3])

            self.e4.delete(0,END)
            self.e4.insert(END, self.selected_tuple[4])

    def delete_command(self):
        db.delete(self.selected_tuple[0])
        self.list1.delete(0,END)
        self.view_command()

    def update_command(self):
        db.update(self.selected_tuple[0],self.title_value.get(),self.author_value.get(),self.year_value.get(), self.isbn_value.get())
        self.list1.delete(0,END)
        self.view_command()





window = Tk()
Window(window)
window.mainloop()
