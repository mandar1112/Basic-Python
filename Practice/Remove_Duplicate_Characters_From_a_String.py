a = "programming"
a = input("Enter a Word: ")
result = ''
for i in range(len(a)):
    if i == 0 or a[i] != a[i-1]:
        result += a[i]
print(result)
# Output:- programing
