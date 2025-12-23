# Lists in Python
# A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.

arr = ["name: John", "age: 30", "city: New York"]
print(type(arr))

print(arr)

for item in arr:
    print(item)

# Accessing list items
print(arr[0])  # First item
print(arr[1])  # Second item
print(arr[-1]) # Last item
print(arr[-2]) # Second last item

# Slicing lists
print(arr[0:2])  # Items from index 0 to 1
print(arr[1:])   # Items from index 1 to end
print(arr[:2])   # Items from start to index 1
print(arr[-2:])  # Last two items

# Modifying list items
arr[1] = "age: 31"
print(arr)

# Adding items to a list
arr.append("country: USA")  # Add to the end
print(arr)

arr.insert(1, "gender: Male")  # Insert at index 1
print(arr)

# Removing items from a list
arr.remove("city: New York")  # Remove by value
print(arr)

popped_item = arr.pop()  # Remove last item
print(popped_item)
print(arr)

del arr[0]  # Delete item at index 0
print(arr)

arr.clear()  # Clear the list
print(arr)

print(len(arr))  # Length of the list

# Copying a list
arr1 = ["name: John", "age: 30", "city: New York"]
arr_copy = arr1.copy()
print(arr_copy)


# Slicing of a list
arr_slice = arr1[1:3]
print(arr_slice)

# Joining two lists
arr2 = ["country: USA", "gender: Male"]
joined_arr = arr1 + arr2
print(joined_arr)

# Using list methods
arr1.append("profession: Developer")
print(arr1) 


arr2 = [10, 20, 5, 15, 30, 25, 0, 40]
arr2.sort()  # Sort the list
print(arr2)

reverse_arr2 = arr2.reverse()  # Reverse the list
print(reverse_arr2)


# Concatenation of lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated_list = list_a + list_b
print(concatenated_list)

# Replication of lists
replicated_list = list_a * 3
print(replicated_list)

# Nested lists
nested_list = [[1, 2, 3], [4, 5,
6], [7, 8, 9]]
print(nested_list)
print(nested_list[0])      # First sub-list
print(nested_list[1][2])   # Third item of second sub-list

# List comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

# Checking membership
print(5 in squared_numbers)  # True
print(15 in squared_numbers) # False

# Iterating through a list with index
for index, value in enumerate(squared_numbers):
    print(f"Index: {index}, Value: {value}")
# Finding index of an item
index_of_25 = squared_numbers.index(25)
print(index_of_25)

# Counting occurrences of an item
count_of_4 = squared_numbers.count(4)
print(count_of_4)

# Extending a list with another list
list_c = [10, 11, 12]
list_a.extend(list_c)
print(list_a)

# Reversing a list
list_a.reverse()
print(list_a)

# Sorting a list
list_a.sort()
print(list_a)

# Copying a list using list() function
list_copy = list(list_a)
print(list_copy)

# Using the list() constructor
new_list = list(("apple", "banana", "cherry"))
print(new_list)

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
























arr = ["name:  John",  "age: 30",  "city: Pune"]
print(type(arr))
print(arr)

for item in arr:
    print(item)

print(arr[0])
print("Indexing 1: ", arr[1])

print("Item from index 1: ", arr[1:])
print("Reverse: ", arr[::-1])


arr.append("Country: India")  # can only add 1 item
print(arr)

arr.insert(1, "gender: Male ") # can only add 1 item at specific index
print(arr)

a = arr * 3
print(a)

arr.extend(["Fruits: Mango","Fruits: Banana"])  # allows multiple items to in list at a single time
print(arr)

arr.remove("Fruits: Mango") # remove the specific item by using it 
print(arr)

arr.pop() # remove the last item if index is not given
print(arr)

arr.reverse() # reverses the string
print(arr)

arr.reverse()
print(arr)

numbers = [1,19,13,0,16,8,2,9]
print(numbers)
numbers.sort() # used to sort the list
print(numbers)

numbers.sort(reverse = True) # used to sort the list in decending order
print(numbers)

input_number_to_count =  0 # used to count the amount of time the element occur
a = numbers.count(input_number_to_count)
print(f"Occurence of {input_number_to_count} in list {numbers} is {a}")


# Membership :- in , not in

print(0 in numbers)
print(4 not in numbers)

# Numerical Operations on list

#min()
print(min(numbers))

#max()
print(max(numbers))

#sum()
print(sum(numbers))

#len()
print(len(numbers))


# Copying a list
new_numbers = numbers.copy()
print(new_numbers)


# Nested Lists
nested_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12,[13,14,15]]]
print(nested_list)
print(nested_list[0])      # First sub-list
print(nested_list[1][2])   # Third item of second sub-list
print(nested_list[4][4][3])  # Third item of fourth sub-list's sub-list :- 15

# List Comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

