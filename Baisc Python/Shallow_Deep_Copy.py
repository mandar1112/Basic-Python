# Shallow Copy ==> A shallow copy creates a new object, but inserts references into it to the objects found in the original.

# Deep Copy ==> A deep copy creates a new object and recursively adds copies of nested objects found in the original.

import copy

l1 = [1,2.5,[10,20,30],"Python"]

l2 = copy.copy(l1)
print(l1)
print(id(l1))
print(id(l2)) 

# l1 and l2 will have different memory addresses

l1[0] = 100
l1[2][0] = 100
print(l1)
print(l2)  
# if we change the direct element it will not effect in l2 but if we change in l1[2], the changes will be reflected in the l2

# The l1 and l2 have different memory address but the inner element refer same memory address. ==> This is called shallow copy.

l3 = copy.deepcopy(l1)
print(l1)
print(id(l1))
print(l3)
print(id(l3))
# l1 and l3 will have different memory addresses
l1[2][1] = 200
print(l1)
print(l3)
# Here the changes made in l1 will not be reflected in l3 as all the elements are copied to l3 newly. ==> This is called deep copy.
# The l1 and l3 have different memory address and the inner element also refer different memory address.

