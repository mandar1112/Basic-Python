# Importing Libraries
import tkinter as tk
from tkinter import ttk


# Window Creation
window = tk.Tk()
window.title("Calculator")
window.geometry("350x260")
window.resizable(False,False)
window.configure(bg="#272626")

# Style Theme
style = ttk.Style()
style.theme_use('clam')

# Style
style.configure("Orange.TButton", background="#8C3E1F", foreground="white", font=("Calibre", 8))
style.configure("LGrey.TButton", background="#5A5858", foreground="white", font=("Calibre", 8))


# Entry Input
entry_input = tk.StringVar()
first_num = 0
operator = ""

# Add value to entry
def add_value(value):
    current = entry_input.get()
    if value == "." and "." in current:
        return
    entry_input.set(current + str(value))

# Clear entry
def clear():
    global operator, first_num
    entry_input.set("")
    operator = ""
    first_num = 0

# Set Operator
def set_operator(op):
    global first_num, operator
    try:
        if entry_input.get() == "":
            return
        first_num = float(entry_input.get())
        operator = op
        entry_input.set("")
    except:
        result = "Invalid Input"
        entry_input.set(result)

# Calculate result
def calculate():
    global operator
    try:
        second_num = float(entry_input.get())

        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result = first_num * second_num
        elif operator == "/":
            if second_num == 0:
                result = "Cannot divide by zero."
            else:
                result = first_num / second_num
        else:
            result = "Invalid Input"

        entry_input.set(result)
        operator = ""

    except:
        entry_input.set("Invalid Input")


# Entry Box
entry = ttk.Entry(master = window, width=16, font = ("Calibri", 28, "bold"), textvariable=entry_input, justify="right")
entry.pack(pady=5)

# Buttons
ttk.Button(master=window, text=1, width=8, style="LGrey.TButton", command= lambda: add_value(1)).place(x=20,y=70)
ttk.Button(master=window, text=2, width=8, style="LGrey.TButton", command= lambda: add_value(2)).place(x=100,y=70)
ttk.Button(master=window, text=3, width=8, style="LGrey.TButton", command= lambda: add_value(3)).place(x=180,y=70)
ttk.Button(master=window, text=4, width=8, style="LGrey.TButton", command= lambda: add_value(4)).place(x=20,y=120)
ttk.Button(master=window, text=5, width=8, style="LGrey.TButton", command= lambda: add_value(5)).place(x=100,y=120)
ttk.Button(master=window, text=6, width=8, style="LGrey.TButton", command= lambda: add_value(6)).place(x=180,y=120)
ttk.Button(master=window, text=7, width=8, style="LGrey.TButton", command= lambda: add_value(7)).place(x=20,y=170)
ttk.Button(master=window, text=8, width=8, style="LGrey.TButton", command= lambda: add_value(8)).place(x=100,y=170)
ttk.Button(master=window, text=9, width=8, style="LGrey.TButton", command= lambda: add_value(9)).place(x=180,y=170)
ttk.Button(master=window, text=0, width=8, style="LGrey.TButton", command= lambda: add_value(0)).place(x=100,y=220)

ttk.Button(master=window, text=".", width=8, style="LGrey.TButton", command= lambda: add_value(".")).place(x=20,y=220)
ttk.Button(master=window, text="C", width=8, style="LGrey.TButton", command=clear).place(x=180,y=220)

ttk.Button(master=window, text="+", width=9, style="LGrey.TButton", command= lambda: set_operator("+")).place(x=260,y=70)
ttk.Button(master=window, text="-", width=9, style="LGrey.TButton", command= lambda: set_operator("-")).place(x=260,y=120)
ttk.Button(master=window, text="*", width=3, style="LGrey.TButton", command= lambda: set_operator("*")).place(x=260,y=170)
ttk.Button(master=window, text="/", width=3, style="LGrey.TButton", command= lambda: set_operator("/")).place(x=297,y=170)

ttk.Button(master=window, text="=", width=9, style="Orange.TButton", command=calculate).place(x=260, y=220)


# Mainloop
window.mainloop()
