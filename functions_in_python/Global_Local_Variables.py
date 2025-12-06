# Global and Local Variables in Python
# A global variable is defined outside of any function and can be accessed from any function within the same module.
# A local variable is defined within a function and can only be accessed within that function.
# The Precedence Rule states that if a local variable and a global variable have the same name, the local variable takes precedence within the function.
# Example of a global variable
global_var = "I am a global variable"
def my_function():
    # Example of a local variable
    local_var = "I am a local variable"
    print(local_var)  # This will work
    print(global_var)  # This will also work
my_function()
print(global_var)  # This will work
# print(local_var)  # This will raise an error because local_var is not defined outside the function


# Demonstrating the Precedence Rule
var = "I am a global variable"
def another_function():
    var = "I am a local variable"
    print(var)  # This will print the local variable
another_function()
print(var)  # This will print the global variable