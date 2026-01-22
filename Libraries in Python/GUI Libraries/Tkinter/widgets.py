# Widgets are the building blocks of tkinter.
# Widgets:- text, buttons, checkboxes, menus, frames, etc.

import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print("A button was pressed.")

def button_hello():
    print("Hello")


# Create a window
window = ttk.Window(themename = 'darkly')
window.title('Window and Widgets')
window.geometry('800x720')


# Create Widgets

# ttk label
label = ttk.Label(master = window, text = 'This is a Test')
label.pack(pady = 5)

# ttk.text
text = ttk.Text(master = window, height = 20)
text.pack(pady= 5)

# ttk.entry
entry = ttk.Entry(master = window)
entry.pack(pady = 5)

# my label
my_label = ttk.Label(master = window, text = "My Label")
my_label.pack(pady = 5)

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack(pady = 5)

# hello button
exercise_button = ttk.Button(master = window, text = 'Exercise Button', command = button_hello)
exercise_button1 = ttk.Button(master = window, text = 'Exercise 1 Button', command = lambda: print('hello'))
exercise_button.pack(pady = 5)
exercise_button1.pack(pady = 5)


# Quit button
quit_button = ttk.Button(master = window, text = "Quit", command = window.destroy)
quit_button.pack(pady = 5)

# Run
window.mainloop()
