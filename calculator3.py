from tkinter import *

# Create main window
parent = Tk()
parent.title('Brain-_0 Dmg')

# Create entry widget
e = Entry(parent, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global first_num
    global math
    first_num = int(e.get())
    math = "addition"
    e.delete(0, END)

def button_subtract():
    global first_num
    global math
    first_num = int(e.get())
    math = "subtraction"
    e.delete(0, END)
    
def button_multi():
    global first_num
    global math
    first_num = int(e.get())
    math = "multiplication"
    e.delete(0, END)

def button_div():
    global first_num
    global math
    first_num = int(e.get())
    math = "division"
    e.delete(0, END)

def button_equal():
    second_number = int(e.get())
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, first_num + second_number)
    elif math == "subtraction":
        e.insert(0, first_num - second_number)
    elif math == "multiplication":
        e.insert(0, first_num * second_number)
    elif math == "division":
        e.insert(0, first_num / second_number)
      


# Create buttons
button_1 = Button(parent, text='1', padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(parent, text='2', padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(parent, text='3', padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(parent, text='4', padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(parent, text='5', padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(parent, text='6', padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(parent, text='7', padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(parent, text='8', padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(parent, text='9', padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(parent, text='0', padx=20, pady=10, command=lambda: button_click(0))

button_add = Button(parent, text='+', padx=20, pady=10, command=button_add)
button_subtract = Button(parent, text='-', padx=20, pady=10, command=button_subtract)
button_multi = Button(parent, text='*', padx=20, pady=10, command=button_multi)
button_div = Button(parent, text='-_-', padx=12, pady=10, command=button_div)
button_equal = Button(parent, text='=', padx=20, pady=10, command=button_equal)
button_clear = Button(parent, text='Clear', padx=8, pady=10, command=button_clear)

# Place buttons on grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_multi.grid(row=4,column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

# Run the application
parent.mainloop()
