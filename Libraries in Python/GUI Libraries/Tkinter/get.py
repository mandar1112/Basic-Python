# Get Method --> get()
# Entry has a get method that returns it's text

import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update the label
    # label['text'] = entry_text
    label.configure(text = entry_text)
    entry['state'] = 'disable' # it will make entry widget disabled.
    # print(label.configure())



# window
window = tk.Tk()
window.title('Getting and Setting Widgets')

# widgets

"""
Widgets can be updated with config

for example:-  Label.configure(text = 'some new text')
               Label['text'] = 'some new text'

"""


label = ttk.Label(master = window, text = 'Some Text')
label.pack()
label.focus()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Button', command = button_func)
button.pack()


# Exercise on Enabling entry widget using other button

exercise_button = ttk.Button(master = window, text = 'Exercise Button', command = lambda: (entry.configure(state = 'normal') , print("Entry Button Enabled Again")))
exercise_button.pack()





# Quit Button
quit_button = ttk.Button(master = window, text = 'Quit', command = window.destroy)
quit_button.pack(pady = 5)

# Run
window.mainloop()
