# Tuples
# A tuple is an immutable ordered collection of items.
# Tuples are defined by enclosing items in parentheses ().
# Tuples can contain items of different data types.
# Tuples support indexing and slicing, similar to lists.
# Tuples are often used to group related data together.
# Example of creating a tuple
my_tuple = (1, "Hello", 3.14, True)

# Accessing elements in a tuple
first_element = my_tuple[0]  # Accessing the first element

second_element = my_tuple[1]  # Accessing the second element

# Slicing a tuple
sliced_tuple = my_tuple[1:3]  # Slicing from index 1
# Tuples are immutable, so we cannot change their elements
# However, we can concatenate tuples to create a new one
another_tuple = (42, "World")
combined_tuple = my_tuple + another_tuple  # Concatenating tuples

# Tuple unpacking
a, b, c, d = my_tuple  # Unpacking the tuple into variables

# Printing the results
print("Original Tuple:", my_tuple)
print("First Element:", first_element)
print("Second Element:", second_element)
print("Sliced Tuple:", sliced_tuple)
print("Combined Tuple:", combined_tuple)
print("Unpacked Values:", a, b, c, d)

# Output:
# Original Tuple: (1, 'Hello', 3.14, True)
# First Element: 1
# Second Element: Hello
# Sliced Tuple: ('Hello', 3.14)
# Combined Tuple: (1, 'Hello', 3.14, True, 42
# Unpacked Values: 1 Hello 3.14 True,'World')

# Note: Since tuples are immutable, operations that modify the tuple will result in a new tuple being created.

# Reverse a tuple
reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)

# Output:
# Reversed Tuple: (True, 3.14, 'Hello', 1)



# Opertaions on tuples: concatenation, repetition, membership testing, length calculation, counting elements, finding index of an element, min, max, sum (for numeric tuples), indexing, slicing

