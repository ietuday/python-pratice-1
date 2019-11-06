from tkinter import * # Imports everything fromt the tkinter library
# Tkinter program is mainly made of two things -- Window and Widgets

window = Tk() # Creates an empty window

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text = "Execute", command = km_to_miles) # NOT km_to_miles()

b1.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop() # Everything between the window = tk() line and this goes in the main window
# Also this line allows us to use the 'cross' or 'X' button to close the window
