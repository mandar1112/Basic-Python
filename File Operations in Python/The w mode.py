# w mode - open the file for writing. Overwriting the file.
# If file doesnt exist, then w mode create file.
# Use x mode for safe, if you use w mode and file already exist then w mode will overwrite the file.

try:
    fh = open("file2.txt", "xt+")
except Exception as e:
    print("Error: ", e)
    exit() # or return in a function

fh.write("This file is overwritten using 'w' mode in Pyhton. \n")
fh.write("Have a nice day!")

fh.close()

