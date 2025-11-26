# Nested Loops
# You can use nested loops to iterate over multi-dimensional data structures, such as lists of lists.

for i in range(3): # Outer loop
    for j in range(2): # Inner loop
        print(f"Outer loop iteration {i}, Inner loop iteration {j}")
# This will print the current iteration of both the outer and inner loops.

# Ascending Order
ls = [100, 20, 30, 23, 25, 64, 62, 53]

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[j] < ls[i]:
            ls[i], ls[j] = ls[j], ls[i]  # temp = ls[i]; ls[i] = ls[j]; ls[j] = temp
print(ls)

# Decending Order
ls1 = [123, 52, 32, 31, 8, 95, 90, 12, 43, 56]

for i in range(len(ls1)):
    for j in range(i+1, len(ls1)):
        if ls1[j] < ls1[i]:
            ls1[i], ls1[j] = ls1[j], ls1[i]
print(ls1)


ls2 = [123, 52, 32, 31, 8, 95, 90, 12, 43, 56]
ls2.sort()
print(ls2) 
print(sorted(ls2, reverse=True))
