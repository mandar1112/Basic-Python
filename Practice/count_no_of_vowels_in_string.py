# message = input("Enter a Sentence: ")
# message = "I am Learning Python."
message = "aaa"
ls = ['a','e','i','o','u']
count = 0
for vowels in message.lower():
    if vowels in ls:
        count += 1
print("Number of Vowels: ",count)