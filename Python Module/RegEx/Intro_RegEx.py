# Regular Expression (RegEx)
# A special sequence of character that defines a pattern for doing complex string maching personalities.

message = "The Current Python Version is 3.12. Other previous versions are 3.13, 3.14, 3.15 3.11, 3.10, 3.9"

"""
# If Python is present in message
print("Python" in message)  # True
print("12" in message) # True
print("13" in message) # False

print(message.find('3.12')) # This will give index 
# Output:- 30

print(message.find("Python")) # Output:- 12

"""

# RegEx :- re module 
import re

# re.search(regex_patter, string) => returns match object when there match found, else return None
match_obj = re.search('13', message)
print(match_obj)

print(message[66:68])

if re.search('13', message):
    print("Found")
else:
    print("Not Found")







# RegEx Metacharacters

match_obj1 = re.search("[0-9][0-9]", message) 
print(match_obj1)

match_obj2 = re.search("[0-9][0-9]", "House Number : 251/A")
print(match_obj2) # Output:- 25







# Dot "." is metacharacter
# . means any character except new line character("\n")

match_obj3 = re.search("[0-9].[0-9][0-9]", message)
print(match_obj3) # Output:- 3.12

match_obj4 = re.search("[0-9].[0-9]", "House Number : 251/A")
print(match_obj4) # Output:- 251


message1 = "This year is 2025"
match_obj5 = re.search("[0-9].[0-9][0-9]", message1)
print(match_obj5) # Output:- 2025

match_obj6 = re.search("[0-9][.][0-9][0-9]", message)
print(match_obj6) # Output:- 3.12






# Special Characters in RegEx

s1 = "Python is a Programming Language. Python3.12 is current version."
pat1 = "old\new" # This will print old   ew(on new line)

# So for that we use r, which tell treat every charcter as string.
pat = r"[a-z][a-z]"
# pat = r"[A-Z][a-z][a-z]" => This will give output 'Pyt'
match_obj7 = re.search(pat, s1)
print(match_obj7) # Output:- 'yt'  (Python is case sensetive we told to search lower case chracter)








# \d and  \D
# \d matches 1 digit chracter. It is similar to [0-9]
pat = r"[a-z][a-z][a-z]\d"
match_obj8 = re.search(pat, s1)
print(match_obj8) # Output:- 'hon3'

# \D matches 1 non-digit character.
pat = r"[a-z][a-z][a-z]\D"
match_obj9 = re.search(pat, s1)
print(match_obj9) # Output:- ytho'




# \s and \S
# \s matches any whitespace character. It is tab and new line character as well.
pat = r"[a-z][a-z][a-z]\s"
match_obj10 = re.search(pat, s1)
print(match_obj10) # Output:- 'hon '


s2 = """Hello There
We are Learning Python.
"""
print(s2)

pat = r"[a-z][a-z][a-z]\s"
match_obj10 = re.search(pat, s2)
print(match_obj10) # Output:- 'llo '


# \S => Opposite of \s. It matches any character except, space, \n and \t
pat = r"[a-z][a-z][a-z]\S"
match_obj11 = re.search(pat, s2)
print(match_obj11) # Output:- 'ello'




# \w => matches [a-z], [A-Z], [0-9], _
pat = r"[a-z][a-z][a-z]\w"
match_obj11 = re.search(pat, s2)
print(match_obj11) # Output:- 'ello'


# \W => opposite of \w. Matches a character except [a-z],[A-Z],[0-9],_
pat = r"[a-z][a-z][a-z]\W"
match_obj11 = re.search(pat, s2)
print(match_obj11) # Output:- 'ere\n'







# Quantifiers ==> They are used to tell quantity
# +, *, ?, {n}
s3 = """Hello There, We are Learning Python.
"""

pat = r"[a-z]{4}"
match_obj12 = re.search(pat, s3)
print(match_obj12) # Output:- 'ello'

pat = r"[A-Z][a-z]{5}"
match_obj13 = re.search(pat, s3)
print(match_obj13) # Output:- 'Learni'

pat = r"[A-Z][a-z]{2,5}"
match_obj14 = re.search(pat, s3)
print(match_obj14) # Output:- 'Hel'

# + => matches 1 or more repititions of the previous pattern
pat = r"[A-Z][a-z]+"
match_obj15 = re.search(pat, s3)
print(match_obj15) # Output:- 'Hel'

# ? => 0 or 1 repititions of the previous pattern
pat = r"[A-Z][a-z]?"
match_obj16 = re.search(pat, s3)
print(match_obj16) # Output:- 'He'

# * => 0 or more repititions of the previous pattern
pat = r"[A-Z][a-z]*"
match_obj17 = re.search(pat, s3)
print(match_obj17) # Output:- 'Hello'





s4 = "Python is a programming language."

pat = r"[a-z]{8}"
match_obj18 = re.search(pat, s4)
print(match_obj18) # Output :- 'program'


# ^ - Caret => Checks at the begin of the string that if it start with it or not.
pat = r"^[a-z]{8}"
match_obj19 = re.search(pat, s4)
print(match_obj19) # Output :- None


# $ - dollar => end of the string
pat = r"[a-z]{8}$"
match_obj20 = re.search(pat, s4)
print(match_obj20) # Output :- 'language'


# group - () + or - |
email = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"(com|edu)"
match_obj21 = re.search(pat, email)
print(match_obj21) # Output :- 'com'

pat = r"[com|edu]"
match_obj22 = re.search(pat, email)
print(match_obj22) # Output :- 'c'





# match() => only looks for the pattern at the beginning of the string.

s5 = "We are learning regex in Python."
pat = r"[A-Z][a-z]"
match_obj23 = re.match(pat, s5)
print(match_obj23) # Output:- 'We'

pat = r"[a-z]{3}"
match_obj24 = re.match(pat, s5)
print(match_obj24) # Output:- None



phones = "John-1234567890, Carol-9876543210, Mark-9087654321, Alice-3434560, Dan-31341341341497563, We are Learning Python in 3.12.10 version."
pat = r"[0-9]{10}"
match_obj25 = re.search(pat, phones)
print(match_obj25)



# findall() 
pat = r"[0-9]{10}"
match_obj26 = re.findall(pat, phones)
print(match_obj26) # Output:- ['1234567890', '9876543210', '9087654321']

pat = r"[0-9]+"
match_obj27 = re.findall(pat, phones)
print(match_obj27) # Output:- ['1234567890', '9876543210', '9087654321', '3434560','31341341341497563', '3', '12', '10']



# fetch all phone numbers. The Phone numbers are exactly 7 digits and should not exceed 15 digit.
pat = r"[0-9]{7,15}"
match_obj27 = re.findall(pat, phones)
print(match_obj27) # Output:- ['1234567890', '9876543210', '9087654321', '3434560']

# fetch all phone numbers. The Phone numbers are exactly 7 digits and there is not upper limit.
pat = r"[0-9]{7,}" # 7 or more
match_obj28 = re.findall(pat, phones)
print(match_obj28) # Output:- ['1234567890', '9876543210', '9087654321', '3434560', '31341341341497563']


# \b :- word boundary
# fetch all phone numbers. The Phone numbers are exactly 7 digits and should not exceed 15 digit.
pat = r"[0-9]{7,15}\b"
match_obj29 = re.findall(pat, phones)
print(match_obj29) # Output:- ['1234567890', '9876543210', '9087654321', '3434560', '341341341497563']

# fetch all phone numbers. The Phone numbers are exactly 7 digits and should not exceed 15 digit.
pat = r"\b[0-9]{7,15}\b"
match_obj30 = re.findall(pat, phones)
print(match_obj30) # Output:- ['1234567890', '9876543210', '9087654321', '3434560']


print("Finditer Function.")
# finditer()

pat = r"\b[0-9]{7,15}\b"
match_obj_iter = re.finditer(pat, phones)
print(match_obj_iter) # Output:- <callable_iterator object at 0x00000149226A7160>

for matches in match_obj_iter:
    print(matches)

"""
Output:-
        <re.Match object; span=(5, 15), match='1234567890'>
        <re.Match object; span=(23, 33), match='9876543210'>
        <re.Match object; span=(40, 50), match='9087654321'>
        <re.Match object; span=(58, 65), match='3434560'>
"""


print("Learning sub() Function")

# sub() => It is used to substitute pattern with another string or sub string.
s6 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
pat = "Sunday"
replacement = "Friday"
result = re.sub(pat, replacement, s6)
print(result) # Output:- Friday, Monday, Tuesday, Monday, Friday, Saturday

result = re.sub(pat, replacement, s6, count=1)
print(result) # Output:- Friday, Monday, Tuesday, Monday, Sunday, Saturday


pat =  r"S[a-z]+"
replacement = "Friday"
result = re.sub(pat, replacement, s6)
print(result) # Output:- Friday, Monday, Tuesday, Monday, Friday, Friday


message2 = """We are learning re. Using re we can search for a pattern in a given string. 
Using the sub(), we can replace the pattern with a given string as well."""

patt = r"\bre\b"
replace = "Regular Expression"
result = re.sub(patt, replace, message2)
print(result)
"""
Output:- 
    We are learning Regular Expression. Using Regular Expression we can search for a pattern in a given string.
    Using the sub(), we can replace the pattern with a given string as well.
"""

message3 = """We are learning re. Using RE we can search for a pattern in a given string. 
Using the sub(), we can replace the pattern with a given string as well."""


patt = r"\bre\b"
replace = "Regular Expression"
result = re.sub(patt, replace, message3, flags= re.IGNORECASE) # It will replace both 're' and 'RE'
print(result)
"""
Output:-
We are learning Regular Expression. Using Regular Expression we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well.
"""


phone_numbers = "+91-1234567890, +91-9087654321"
pattern = r"[+-]"
replace = ""
result = re.sub(pattern, replace, phone_numbers, flags= re.IGNORECASE) # It will replace both 're' and 'RE'
print(result) # Output:- 911234567890, 919087654321





# Complie Function
phoness = "Alice-1234567890, Mark-9876543212, Carol-1290875673"
pattern = r"\d{10}"
match_obj31 = re.findall(pattern, phoness)
print(match_obj31) # Output:- ['1234567890', '9876543212', '1290875673']


pattern_compiled = re.compile(pattern) # Why? :- It optimized the efforts, if you want to use pattern again and again then compile it.
print(pattern_compiled, type(pattern_compiled)) # Output:- re.compile('\\d{10}') <class 're.Pattern'>
match_obj32 = re.findall(pattern_compiled, phoness)
print(match_obj32) # Output:- ['1234567890', '9876543212', '1290875673']


with open("Student_details", "rt") as fh:
    data = fh.read()
print(data, type(data))

phone_matches = re.finditer(pattern_compiled, data)
print(phone_matches) # Output:- <callable_iterator object at 0x00000171CA928B80>

for matches in phone_matches:
    print(matches)
"""
Output:-
<re.Match object; span=(24, 34), match='9876543210'>
<re.Match object; span=(62, 72), match='1234567890'>
<re.Match object; span=(95, 105), match='9999999999'>
"""

