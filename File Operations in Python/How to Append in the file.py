# 'a' mode ==> Append Mode
# Add Data to end of the file.
# If the file does not exist, 'a' mode creates the file.



fh = open("file2.txt", 'at+')
fh.write("\nThis content has written using 'a' mode. \n")
fh.write("\n'a' mode is used to add new content at the end of the file.\n")
fh.write("\n'a' mode creates the file if file doesn't exist.\n")
fh.write("\nGood Bye!\n")

fh.seek(0)
lines = fh.readlines()
for line in lines:
    print(line.strip())



fh.close() # Close the file.