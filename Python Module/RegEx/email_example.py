import re

with open("Student_details", "rt") as fh: # reading a file
    data = fh.read() 

pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[.][a-zA-Z]+" # Creating a pattern


# . => in regex means ANY character

# \. => means actual dot


matches = list(re.finditer(pattern, data)) 
for match in matches:
    print(match)
"""
Output:-
<re.Match object; span=(6, 32), match='alice-cool_123@example.com'>
<re.Match object; span=(50, 71), match='Carol_123@example.com'>
<re.Match object; span=(88, 115), match='john.dan.12345@mydomain.com'>
<re.Match object; span=(147, 160), match='-@example.com'>
<re.Match object; span=(161, 180), match='_123abc@example.com'>
<re.Match object; span=(181, 200), match='_123abc@example.edu'>
"""

for match in matches:
    print(match.group())
"""
Output:-
alice-cool_123@example.com
Carol_123@example.com
john.dan.12345@mydomain.com
-@example.com
_123abc@example.com
_123abc@example.edu
"""

pattern1 = r"[a-zA-Z]+[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
matches1 = re.finditer(pattern1, data)
for match1 in matches1:
    print(match1.group())
"""
Output:-
alice-cool_123@example.com
Carol_123@example.com
john.dan.12345@mydomain.com
abc@example.com
abc@example.edu
"""


pattern2 = r"\b[a-zA-Z]+[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]+\b"
matches2 = re.finditer(pattern2, data)
for match2 in matches2:
    print(match2.group())
"""
Output:-
alice-cool_123@example.com
Carol_123@example.com
john.dan.12345@mydomain.com
"""



