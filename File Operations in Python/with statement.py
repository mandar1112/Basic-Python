# with statement 
# with insures that the file automatically close after the block ends.
# if there is error in the with block, with ensures that file is close before ending the program.



fh = open("file2.txt", "rt")
content = fh.read()
fh.close()  # We have to close the file manually.
print(content)

# Using with statement
# with simplifies the setup, more readable.

with open("file2.txt", "rt") as fh:
    content1 = fh.read()
print(content1)


