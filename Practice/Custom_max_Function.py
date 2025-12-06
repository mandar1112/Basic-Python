# Write your own function that returns the maximum of a list.
ls = [5,1,6,4,2,3,9,8,7] 
max_value = ls[0]

for i in range(len(ls)):
    if ls[i] > max_value:
        max_value = ls[i]
print(max_value)
# Output:- 9