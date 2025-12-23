# Read Operation
# read() ==> reads the content of the file.
# If you open the file in text mode then it will read as string.

fh = open("file2.txt", 'rt')

content = fh.read()

print(content)
print(type(content))



# if you want to read first 10 character
fh.seek(0)  # To get pointer at starting of the file.
content1 = fh.read(10) # number in read function is to tell how much character to read. By default it will read complete file.

print(content1)

# if you want to read line
# readline()
fh.seek(0) 
line1 = fh.readline()
line2 = fh.readline()
line3 = fh.readline()
print("First Line: ",line1)
print("Second Line: ",line2)
print("Third Line: ",line3) # This will print Empty String. As nothing is there in that line.
# Empty String => The File has reached End of the File (EOF).


# readlines()
# All the lines will be stored in the list.
# \n means the pointer will go to new line.
# readlines will fetch all the lines after the pointer.
fh.seek(0)
lines = fh.readlines()
print(lines)
for line in lines:
    print(line.strip('\n'))
fh.close()




students = {'student1':{'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2':{'roll': 102, 'name': 'Alice', 'percent': 68.5},
            'student3':{'roll': 103, 'name': 'Carol', 'percent': 88.5}}

"""
with open("Student_info.txt", 'xt') as fh:
    fh.write(str(students))
"""

with open("Student_info.txt", 'rt') as fh:
    fh.seek(0)
    content = fh.read()
    print(content)
print(type(content))

"""
Another Way: to read the file.
with open("Student_info.txt", "rt") as fh:
    for line in fh:
        print(line, end="")

print(type(line))
"""