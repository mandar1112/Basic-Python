# Dict in Python
# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict.get("age"))
print("City:", my_dict["city"])
# Adding a new key-value pair
my_dict["job"] = "Engineer"
print("Updated Dictionary:", my_dict)

# Modifying an existing value
my_dict["age"] = 31
print("Modified Age:", my_dict["age"])

# Removing a key-value pair
del my_dict["city"]
print("After Deletion:", my_dict)

# Iterating through the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary.")

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", list(keys))
print("Values:", list(values))

# Getting the number of key-value pairs
length = len(my_dict)
print("Number of key-value pairs:", length)

# Clearing the dictionary
my_dict.clear()
print("Cleared Dictionary:", my_dict)


Std1 = {"Math": 85, "Science": 90, "English": 78, "History": 88, "Art": 92}
Std2 = {"Biology": 80, "Science": 85, "English": 82, "History": 90, "CS": 88}

print(Std1["Science"])
print(Std2.get("Maths")) #Get Method, it will return None if the key is not found

print(Std2.get("Physics", 80))


# Example dictionaries for students' scores
total_score_Std1 = sum(Std1.values())
total_score_Std2 = sum(Std2.values())
print("Total Score of Student 1:", total_score_Std1)
print("Total Score of Student 2:", total_score_Std2)
 
 #POP Method
removed_score = Std1.pop("Art", "Not Found")
print("Removed Score:", removed_score)          

#POPITEM Method
last_item = Std2.popitem()
print("Last Item Removed:", last_item)



# We cannot use lists as dictionary keys because they are mutable and unhashable.
# The following line will raise a TypeError
# d1 = {[1,3,5]:9,[2,4,6]:8}  # This will raise a TypeError because lists are unhashable and cannot be used as dictionary keys
# print(d1)

# However, we can use tuples as dictionary keys because they are immutable and hashable.
# d2 = {(1,3,5):9, (2,4,6):8}  # This is valid
# print(d2)

# Allowed dictionary keys :- tuples, strings, numbers (int, float, bool, etc.)
# Not allowed dictionary keys :- lists, sets, dictionaries, etc.

# Values in a dictionary can be of any data type, including lists, sets, and even other dictionaries.

Student1 = {"id":101, "name":"John", "marks":[85, 90, 78, 81.9], "is_passed":True}

print(Student1)
print(Student1['marks'][1]) # Output":- 85


Student2 = {"id": 102, "name": "Tom", "marks":{"English": 92.5,"Physics":95, "Biology":87,"Maths":95},"is_passed":True}
# If i want to fetch Biology marks of Student2 
print(Student2['marks']['Biology'])


Std_1_2_data = [Student1 | Student2]
print(Std_1_2_data)


"""
Std1 = {"Name": "Tom", "ID": 1, "Marks":{"English":90, "Science":89, "Maths":95}}
Std2 = {"name": "John", "id":2, "marks":{"english": 92, "science": 93, "maths": 98}}

for Key, Value in Std1.items():
    print(f"{Key} : {Value}")
    if Key == "Marks":
        for subject, marks in Value.items():
            print(f"{subject} : {marks}")

for Key, Value in Std2.items():
    print(f"{Key} : {Value}")
    if Key == "Marks":
        for subject, marks in Value.items():
            print(f"{subject} : {marks}")

# Std3  = Std1 | Std2
# print(Std3)

Std3 = {}

for d in (Std1,Std2):
    for key, value in d.items():
        Std3[key] = value
print(Std3)
"""


# Only to get keys of the dict
print(Student1.keys()) # Output:- dict_keys(['id', 'name', 'marks', 'is_passed'])

# Only to get values of the dict
print(Student1.values()) # Output:- dict_values([101, 'John', [85, 90, 78, 81.9], True])

# To get keys and values of the dict
print(Student1.items()) # Output:- dict_items([('id', 101), ('name', 'John'), ('marks', [85, 90, 78, 81.9]), ('is_passed', True)])
