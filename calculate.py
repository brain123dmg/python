from tkinter import *

# Create main window
parent = Tk()
parent.title("Calculator")

# Entry widget for displaying input and output
entry = Entry(parent, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# Define button texts and their grid positions
buttons = [
    ('A/C', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('|', 1, 3),
    ('9', 2, 0), ('8', 2, 1), ('7', 2, 2), ('X', 2, 3),
    ('6', 3, 0), ('5', 3, 1), ('4', 3, 2), ('-', 3, 3),
    ('3', 4, 0), ('2', 4, 1), ('1', 4, 2), ('+', 4, 3),
    ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
]

# Create and place buttons
for (text, row, column, *colspan) in buttons:
    Button(parent, text=text, width=5, height=2).grid(row=row, column=column, columnspan=colspan[0] if colspan else 1, padx=5, pady=5)

# Run the application
parent.mainloop()
