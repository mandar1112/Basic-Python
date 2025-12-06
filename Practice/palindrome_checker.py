pal_s = input("Enter a String you want to check Palindrome: ")
rev = ""
for ch in pal_s:
    rev = ch + rev
    
if pal_s == rev:
    print(pal_s,"is an Palindrome.")
else:
    print(pal_s,"is not an Palindrome.")