"""
with open("my_file.txt", 'rt') as fh:
    data = fh.read()
print(data)  # FileNotFoundError
"""

try:
    with open("file2.txt", 'rt') as fh:
        data = fh.read()
except Exception as e:
    print(e)
else: # this will execute only when there is no error.
    print(data)
finally: # This execute if there is error or not
    print("This is finally block.")


