sentence = "I am Learning Python."
count = 0
for i in range(len(sentence)):
    if (sentence[i] != " " and (i == 0 or sentence[i-1] == " ")):
        count += 1
print(count)
# Output: 4
# sentence = input("Enter a sentence: ")
