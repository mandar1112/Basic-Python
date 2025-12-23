# Pickle Module
"""
- Pickle store data in Binary Format.
- Pickle is not Human Readable.
- Pickle type only support in Python.
- It is mainly use to store ML model.
pickel supports:
    Almost everything:
        Custom classes
        Objects
        Functions
        Sets
        Tuples
        Dictionaries
"""

students = {'student1':{'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2':{'roll': 102, 'name': 'Alice', 'percent': 68.5},
            'student3':{'roll': 103, 'name': 'Carol', 'percent': 88.5}}

"""
with open("Student_info.txt", 'xt') as fh:
    fh.write(str(students))


with open("Student_info.txt", 'rt') as fh:
    fh.seek(0)
    content = fh.read()
    print(content)
print(type(content))


Another Way: to read the file.
with open("Student_info.txt", "rt") as fh:
    for line in fh:
        print(line, end="")

print(type(line))
"""
# After converting dict into txt file or string it cannot be reversed.

# To use pickle module
import pickle

# Serialization => Puting data into file.
# dump() => is used to dump the data in file and data saved will be in binary format.
with open("Students.bin", 'bw') as fh:
    for student in students:
        pickle.dump(students[student], fh)


# Deserialization => Taking out the data from the file.
# load() => it is used to take out data from the file and the data will be in dict foramt.
with open("Students.bin", "br") as fh:
    while True:
        try: 
            print(pickle.load(fh))
        except EOFError: 
            break



# Exception and Exception Handling in Pickle
# In Read file we already use Exception Handling with try-except metthod.

# To get student name who get above 80 percent
student_list_90 = []
print()
print("Now printing Student name who are have above 80 percent.")

with open("Students.bin", "br") as fh:
    fh.seek(0)
    while True:
        try: 
            data = pickle.load(fh)
            if data['percent'] >= 80:
                student_list_90.append(data['name'])
        except EOFError: 
            print("No Student is above 80 percent.")
            break

print(f"List of Student who secured 80 or more: {student_list_90}")

