# Sets are collections of unique elements.
# Sets are defined by enclosing items in curly braces {} or by using the set() function.
# Sets are unordered, meaning that the items do not have a defined order.
# Sets do not allow duplicate elements.
# Sets support operations like union, intersection, difference, and symmetric difference.
# Example of creating a set
my_set = {1, 2, 3, 4, 5}
# Alternatively, using the set() function
another_set = set([4, 5, 6, 7, 8])

# Adding elements to a set
my_set.add(6)  # Adding a single element
my_set.update([7, 8, 9])  # Adding multiple elements

# Removing elements from a set
my_set.remove(3)  # Removes element 3, raises KeyError if not found
my_set.discard(10)  # Removes element 10 if present, does nothing if not found
my_set.pop()  # Removes and returns an arbitrary element
# Clearing all elements from a set
# my_set.clear()

# Set operations
union_set = my_set.union(another_set)  # Union of two sets
intersection_set = my_set.intersection(another_set)  # Intersection of two sets
difference_set = my_set.difference(another_set)  # Difference of two sets
symmetric_difference_set = my_set.symmetric_difference(another_set)  # Symmetric difference

# Checking membership
is_member = 5 in my_set  # True if 5 is in my_set
is_not_member = 10 not in my_set  # True if 10 is not in

# Printing the results
print("Original Set:", my_set)
print("Another Set:", another_set)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
print("Is 5 a member of my_set?", is_member)
print("Is 10 not a member of my_set?", is_not_member)
my_set.clear()
print("Cleared Set:", my_set)

# Output:
# Original Set: {1, 2, 4, 5, 6,
# Another Set: {4, 5, 6, 7, 8}
# Union Set: {1, 2, 4, 5, 6,
# Intersection Set: {4, 5, 6}
# Difference Set: {1, 2}
# Symmetric Difference Set: {1, 2, 7, 8}
# Is 5 a member of my_set? True
# Is 10 not a member of my_set? True
# Note: Since sets are unordered, the order of elements in the printed output may vary.

# Set operations: union, intersection, difference, symmetric difference, membership testing, adding elements, removing elements, clearing the set






"""
✔️ Sets are non-sequential, unordered, unique, mutable

Correct.

✔️ Why do we need a Set?

No duplicates allowed

Fast membership testing (in,not in)

Supports mathematical operations (union, intersection, etc.)

✅ Your Code with Explanations
1. Creating a Set
s1 = {10, "Python", 2.5, 2, 10, 20, 59, 28}
print(s1)
print(len(s1))


✔️ Duplicate 10 is removed automatically.
✔️ len(s1) gives number of unique elements.

2. Converting a Tuple to Set
tuple1 = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
week_days = set(tuple1)
print(week_days)


✔️ Set is unordered, so the output order will be random.

3. Membership Operators
nums = {10, 2, 3, 1, 123, 12, 83, -1}

print(0 in nums)      # False
print(0 not in nums)  # True


✔️ Correct.

4. Adding Elements
nums.add(5)
nums.add(6)
print(nums)


✔️ add() inserts new element; duplicates are ignored.

5. Removing Elements (remove vs discard)
nums.remove(5)       # Works
print(nums)


⚠️ If 5 was not present → error

nums.discard(6)      # No error even if not present
nums.discard(5)


✔️ discard() is safer.

🧮 Mathematical Set Operations
Sample Sets
std1 = {"English", "Maths", "Marathi", "CS", "Physics"}
std2 = {"English", "Biology", "Chemistry", "Physics"}
std3 = {"Sanskrit", "Maths", "ML"}

1. Intersection (Common items)
common_subject = std1.intersection(std2)  # or std1 & std2
print(common_subject)


✔️ Shows common subjects: English, Physics

2. Union (All unique items)
all_subjects = std1.union(std2, std3)  # or std1 | std2 | std3
print(all_subjects)


✔️ Contains all unique subjects of all students.

3. Difference (Items in A but not in B)
difference_of_sets = std1 - std2
print(difference_of_sets)


✔️ Shows subjects student 1 has, but student 2 does not.

🧊 Frozen Set (Immutable Set)
fs1 = frozenset({10,30,20,60,40,50})
print(fs1, type(fs1))


✔️ frozenset is:

Immutable

Cannot add/remove elements

Supports union, intersection, difference

Use case:
✔️ When you want sets inside a dictionary or another set (must be immutable).

Summary Table
Feature	set	frozenset
Mutable	✔️ Yes	❌ No
Allows duplicate	❌ No	❌ No
Ordered	❌ No	❌ No
Can add/remove	✔️ Yes	❌ No
Supports math operations	✔️ Yes	✔️ Yes

"""