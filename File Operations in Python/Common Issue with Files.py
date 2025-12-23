fh = open("filess3.txt", "rt") # This file doesnt exist then we will get FileNotFound Error.
content = fh.read()
fh.close()

print(content)

# You Open the file in read mode  and try to write then we will get UnsupportedOperation: not writable


# If you open the file in like only append, write or create and try to read it it will give and Error   io.UnsupportedOperation: not readable

# Always close the file after use.
