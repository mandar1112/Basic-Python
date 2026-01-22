import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Frame Implementation")
window.geometry("400x300") # Size of the window

# Creating Frames
my_frame = ttk.Frame(window)
my_frame1 = ttk.Frame(window)

# Style Using ttk
style = ttk.Style()
style.theme_use("clam")

style.configure("My.TLabel", foreground = "white", background = "black", font=("Arial", 16, "bold", "italic"), padding = 100)


my_frame.pack(side="left", fill="both", expand=True)
my_frame1.pack(side="right", fill="both", expand=True)



label1 = ttk.Label(my_frame, text="Hello World!", style="My.TLabel")
label1.pack(side="top", fill="both", expand=True)

label2 = tk.Label(window, text="How Are You?", bg="Blue")
label2.pack(side="top", fill="both", expand=True)

label3 = tk.Label(window, text="Have a Nice Day!", bg="Green")
label3.pack(side="top", fill="both", expand=True)




window.mainloop()