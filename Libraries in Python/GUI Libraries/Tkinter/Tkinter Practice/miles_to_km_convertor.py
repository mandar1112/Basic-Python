import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(f"{km_output} km")

# window
window = ttk.Window(themename = 'journal')
window.title('Miles to Kilometer')
window.geometry('400x260')

# title
title_label = ttk.Label(master=window, text = 'Miles to Kilometers', font = 'Calibri 26 bold')
title_label.pack(pady = 10)

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24 bold', textvariable = output_string)
output_label.pack(pady = 5)

# close
quit_button = ttk.Button(master = window, text = 'Quit', command = window.destroy)
quit_button.pack(side = 'bottom',pady=5)

# run
window.mainloop()