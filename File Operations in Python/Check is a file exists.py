# To check the file exist or not.

# os.path.exists() ==> it is the part of os module used to check the file or directory exist or not.

"""import os
file_name = "D:/Coding/Python/Basic/File Operations in Python/practice.txt"

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exists.")
"""

# pathlib.path.exists() ==> pathlib module

from pathlib import Path
file_name1 = Path("D:/Coding/Python/Basic/File Operations in Python/practice1.txt")

def check_file_exist():
    if file_name1.exists():
        print("File exists. Cannot Create.")
    else:
        print("File does not exists, Creating it.")
        with open(file_name1, "xt") as fh:
            fh.write("Some Content.")
        print("File created Successfully.")

check_file_exist()



