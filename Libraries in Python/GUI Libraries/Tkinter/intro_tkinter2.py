import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.minsize(300, 300)
# window.geometry("600x400")
window.title("Intro 2")

style = ttk.Style()
style.configure("My.TLabel", font=("Arial", 20, "italic", "bold"), padding=10)

label1 = ttk.Label(master = window, text="Hello!", style="My.TLabel")
label1.pack(pady = 5)

label2 = ttk.Label(master = window, text="Enter Your Name")
label2.pack(pady = 5)

def user_name_input():
    a = user_name.get()
    label2.config(text=f"Your Name is {a}")

user_name = ttk.Entry(master = window, width=30)
user_name.pack(pady = 5)

btn1 = ttk.Button(master = window, text="Submit", command=user_name_input)
btn1.pack(pady = 5)




## Text Widget

label3 = ttk.Label(master = window, text="Enter Description")
label3.pack(pady = 5)


# This is used to write multiple text lines
text1 = tk.Text(master = window, width=30, height=5)
text1.pack(pady = 5)

text1.focus()  # This makes cursor go visible inside the Text box
text1.insert('1.0','Enter Your Comments: ')  # Here '1.0' means 1 == first line, 0 == first character of the line

# How to read the what is written in the text box
# Here we have to give starting index and ending index to read other it will give error.
# text_data = text1.get('1.0', 'end') 

def text_function():
    text_data = text1.get('1.0', 'end') # This will read complete text box
    print(text_data) # But to show data in cmd you need button same as Entry option


text_button = ttk.Button(text = "Get Text", command = text_function)
text_button.pack(pady=2)



## Separator Widget

sep = ttk.Separator(orient='horizontal') # This make a single pixel line in between the two component
sep.pack(fill='x') # This will make the complete horizontal line


# padding give space inside the widget
# padx/pady in pack method it will give space between component



## Checkbutton Widget

# check_option = tk.IntVar()
# check_option = tk.StringVar()
check_option = tk.BooleanVar()

def check_option_task():
    print(check_option.get())

# check_button = ttk.Checkbutton(text = "Agree with the terms & conditions", variable = check_option, command = check_option_task, onvalue = 'Yes', offvalue = 'No')
check_button = ttk.Checkbutton(text = "Agree with the terms & conditions", variable = check_option, command = check_option_task)
check_button.pack()



## Radiobutton Widget

# creating a variable
radio_value = tk.StringVar()

def get_radio_value():
    print(radio_value.get())

radio_button1 = ttk.Radiobutton(text = 'Male', variable = radio_value, value = 'male', command = get_radio_value)
radio_button2 = ttk.Radiobutton(text = 'Female', variable = radio_value, value = 'female', command = get_radio_value)
radio_button1.pack(padx = 10)
radio_button2.pack()



## ComboBox Widget

selected_country = tk.StringVar()

countries = ttk.Combobox(textvariable = selected_country, value = ( "India", "Russia","Australia", "Canada","Sweden", "US", "France", "Germany", "Itlay"))
countries['state'] = 'readonly'
countries.pack()


def display_country(event):
    msg = f"Selected Country is {selected_country.get()}"
    # print(f"Selected Country is {selected_country.get()}")
    country_label = ttk.Label(text = msg )
    country_label.pack()


# This is used to connect combobox and function together
countries.bind("<<ComboboxSelected>>", display_country)




## List Widget

food_items = ("Pizza", "Burger", "Garlic Bread", "Nachos", "Salad") 
fav_food = tk.StringVar(value = food_items)

food_list = tk.Listbox(listvariable=fav_food, height=5, selectmode='multiple')
food_list.pack(pady=10)

def food_item_task(event):
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>", food_item_task)



## Spinbox Widget

counter = tk.IntVar(value = 10)

def get_spin_box_value():
    print(f"Current Value: {spin_box.get()}")

# spin_box = ttk.Spinbox(textvariable=counter, from_=0, to = 20, wrap=True, command=get_spin_box_value)
# spin_box = ttk.Spinbox(values=(10,15,20,25), textvariable=counter, from_=0, to = 20, wrap=True, command=get_spin_box_value)
spin_box = ttk.Spinbox(values=tuple(range(5,105,5)), textvariable=counter, from_=0, to = 20, wrap=True, command=get_spin_box_value)
spin_box.pack(pady = 5)

print(f"Initial Value: {spin_box.get()}")









# Quit Button
btn2 = ttk.Button(master = window, text="Quit", command=window.destroy)
btn2.pack(side="bottom",pady = 5)

window.mainloop()