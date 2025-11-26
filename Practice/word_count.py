countries = ["India", "Russia", "China", "Japan", "UK", "USA", "Poland", "Germany", "France", "Italy"]
counter = 0
counter1 = 0
counter2 = 0
# Count all the countries Srarting with letter 'I'.
I = []
C = []
J = []
for country in countries:
    if country[0] == 'I':
        counter = counter + 1
        I.append(country)
    
    if country.startswith(('C','U')):
        counter1 = counter1 + 1
        C.append(country)
    if country.startswith('J'):
        counter2 = counter2 + 1
        J.append(country)
    
print(counter)
print(I)
print(counter1)
print(C)
print(counter2)
print(J)