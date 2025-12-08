# Opening a File in Python
# we have open(file_name, mode_to_open)
# Modes: r = read, x = create, w = write or overwrite, a = append, t = for text file, b = for binary mode
# rt is default mode
file_handler = open("practices.txt", 'xt+')

file_handler.write("Hello, this is a test file!") # Write to file
file_handler.seek(0)     # move cursor to start
print(file_handler)      # read from file

file_handler.close()
print(file_handler)  # it will print even after close, after closing file you cannot do any operations on the file like read, write, etc.
# You can close the file no of times it will not give an error.



# x mode => Create a file

fh = open("file.txt", 'xt')

# Writing into a file
# write(content)
fh.write("This file is created using the 'x' mode in Python.\n")
fh.write("Next Line.")

# Close the file
fh.close() 


