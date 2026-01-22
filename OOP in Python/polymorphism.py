# Polymorphism :-  It means "many forms". 
# It refers to the ability of the same interface (method, operator, function name) to exhibit differnet behavior depending on: Type of object, Context in which it is used.

# For example :- if we take + sign, it will add two integer but in sting it will work as concatenation.


# Types of Polymorphism:-

# 1. Operator Overloading:- Same operator behaves differently for differnet objects.

print(5 * 2) # 10 , Here * multiplies number
print("Hi" * 3) # HiHiHi , Here * repeats strings


# Python doesn't support Mehod Overloading


# 2. Method Overriding (Run - Time Polymorphism)
# Child class provides its own implementation of a parent method.

class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("Cat meows.")


animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()

# Output:- 
#           Animal makes a sound.
#           Dog barks.
#           Animal makes a sound.
#           Cat meows.
#           Animal makes a sound.



# 3. Function Polymorphism:- Same function with different types of arguments.

print(len("Python")) # 6
print(len(1, 2, 3, 4)) # 4

# same function len()
# works for string, list, tuple, etc.



# 4. Duck Typing:- If it looks like a duck and quacks like a duck, it is a duck.

class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def make_it_fly(obj):
    obj.fly()

make_it_fly(Bird()) 
make_it_fly(Airplane())

# Output:- 
#           Bird flies
#           Airplane flies

# No inheritance
# Only behavior matters.




