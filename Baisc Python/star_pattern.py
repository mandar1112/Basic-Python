# Star Pattern Generator

for i in range(1, 6):  # Number of rows
    for j in range(1, i+1): # Number of stars in each row
        print('*', end=" ") # Print star with space
    print() # Move to the next line after each row
# This code generates the following star pattern:
# *
# * *
# * * *
# * * * *
# * * * * *

# You can change the range values to generate a different size of the star pattern.

for i in range(5, 0, -1):
    for j in range(i, 0, -1): 
        print('*', end=" ")
    print()

# This code generates the following inverted star pattern:
# * * * * *
# * * * *
# * * *
# * *
# *


for i in range(1, 6):  # Number of rows
    for j in range(6-i): # Number of spaces for alignment
        print(" ", end=" ") # Print space for alignment
    for k in range(i): # Number of stars in each row
        print('*', end=" ") # Print star with space
    print() # Move to the next line after each row
# This code generates the following right-aligned star pattern:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *



for i in range(5, 0, -1):  # Number of rows
    for j in range(5-i): # Number of spaces for alignment
        print(" ", end=" ") # Print space for alignment
    for k in range(i): # Number of stars in each row
        print('*', end=" ") # Print star with space
    print() # Move to the next line after each row
# This code generates the following inverted right-aligned star pattern:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# Pyramid Star Pattern
rows = 5 # Number of rows for the pyramid pattern

for i in range(1, rows + 1):  # Loop through each row
    # Print spaces
    for j in range(rows - i): # Number of spaces for alignment
        print(" ", end=" ") # Print space for alignment
    # Print stars
    for k in range(2 * i - 1): # Number of stars in each row, odd numbers only 
        print("*", end=" ") # Print star with space
    print()
# This code generates the following pyramid star pattern:
#         *
#       * * *
#     * * * * *
#   * * * * * * * 
# * * * * * * * * * 


# Reversed Pyramid Star Pattern
for i in range(rows, 0, -1):  # Loop through each row in reverse
    # Print spaces
    for j in range(rows - i): # Number of spaces for alignment
        print(" ", end=" ") # Print space for alignment
    # Print stars
    for k in range(2 * i - 1): # Number of stars in each row, odd numbers only 
        print("*", end=" ") # Print star with space
    print()
# This code generates the following inverted pyramid star pattern:
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *



# Diamond Star Pattern
for i in range(1, rows + 1):  # Upper half of the diamond
    for j in range(rows - i): # Number of spaces for alignment
        print(" ", end=" ") # Print space for alignment
    for k in range(2 * i - 1): # Number of stars in each row, odd numbers only 
        print("*", end=" ") # Print star with space
    print()

for i in range(rows - 1, 0, -1):  # Lower half of the diamond
    for j in range(rows - i): # Number of spaces for alignment
        print(" ", end=" ") # Print space for alignment
    for k in range(2 * i - 1): # Number of stars in each row, odd numbers only 
        print("*", end=" ") # Print star with space
    print()

# This code generates the following diamond star pattern:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *



