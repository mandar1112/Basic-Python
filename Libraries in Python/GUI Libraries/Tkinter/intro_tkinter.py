# Tkinter is built-in GUI library in python.

# Importing the tkinter library
import tkinter as tk
from tkinter import messagebox, Entry, ttk

import tkinter.font as tfont

# Creating a window
window = tk.Tk()

# To change the title of the window
window.title("My Application")

# This is used to set minmum size of the window so the pack method will not resize the window according to the label.
window.minsize(width=600, height=300) 

window.maxsize(width=1920, height=1080) # Max size of the window.


custom_font = tfont.Font(family="Times New Roman", size = 15, slant = "italic", weight="bold") # To use this we need to import tkinter.font


#This is used to add component to the window, but without pack method it will not display on the window.

label1 = ttk.Label(text="Hello!, I am Learning Tkinter Module in Python.", font=custom_font)
# label = tk.Label(text="Hello World!", font=("Times New Roman", 20, "bold"))
label = tk.Label(text="Hello World!")

label1.pack(side="bottom") # here we can use expand so it will be in middle.
label.pack() # This method bring component on the window. And window is get resized to the size of the label.
label.config(font=("Courier New", 25, "underline"))
# If you are using config then you dont need to write font in the Label.






# Change Label Text

label["text"] = "Have a nice day!" # One way to change the text of the vaiabele label

label.config(text="My New App") # Other way to change the text of the Label







# Buttons
counter = 0
def clicked():
    global counter
    counter += 1
    btn_clicked = tk.Label(text=f"Button Clicked {counter} times.")
    btn_clicked.pack()
    messagebox.showinfo("Popup Title", "Button Clicked!")

button = tk.Button(text="Submit", command=clicked)
button.pack(expand=True)







# Entry Component

# user_input = Entry(width=30, show="*")  # When you will input something in the box, it will show you the start, this can be used for password.
label2 = tk.Label(text="Hi! Enter Your Name: ")
label2.pack()
def input_user_text():
    input_text = user_input.get()
    label2.config(text=f"Your Name: {input_text}.")



user_input = Entry(width=30)
user_input.pack()

btn1 = tk.Button(text="Click On This After Entering the Name.", command=input_user_text)
btn1.pack()

# ttk module is better, advanced version of tk.








# Checkbutton Widget


check_option = tk.IntVar()
check_option1 = tk.StringVar()

def check_option_task():
    print(check_option.get())
    if check_option.get() != 0:
        messagebox.showinfo("Popup Title", "You Agree to Terms & Condition")

def check_option_task1():
    print(check_option1.get())
    if check_option1.get() != "No":
        messagebox.showinfo("Popup Title", "You Agree to Terms & Conditionsssss")

check_button1 = ttk.Checkbutton(text="Agree with the terms & conditionsssss", variable=check_option1, command=check_option_task1, onvalue="Yes", offvalue="No")
check_button1.pack(side="bottom")

check_button = ttk.Checkbutton(text="Agree with the terms & condition", variable=check_option, command=check_option_task)
check_button.pack(side="bottom")




    










# Destry Method
quit_button = ttk.Button(text="Quit", command=window.destroy)
quit_button.pack()



window.mainloop() # This method is used to see the window until the program runs properly.




