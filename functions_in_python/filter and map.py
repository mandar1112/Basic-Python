# Filter and map

# The filter() function in Python is a built-in function used to construct an iterator from elements of an iterable for which a function returns true. It is a powerful tool for selecting specific items from a sequence based on a given condition.
# filter(function, sequence)

seq = [1,2,3,4]
odd = lambda x: True if x % 2 != 0 else False
filterred_output = filter(odd, seq)
# filtered_output = filter(lambda x: True if x % 2 != 0 else False, seq)
print(filterred_output) # We get filter object
print(list(filterred_output))
# Output:- [1,3]


# map()
# map(function, sequence)
# This will give what is output of the function
mapped_output = map(lambda x: True if x % 2 != 0 else False, seq)
print(list(mapped_output))
# Output:- [True,False,True,False]
