"""
We have to delete keys in a dictionary based on certain conditions.
"""

user = {"user_name": "John Doe", "age": 30, "is_active": True, "password": "12345", "address": "123 Main St"}

# Delete the 'password' key for security reasons
sensitive_keys = ["password", "address", "mobile_number"]
"""
for key in user:
    if key in sensitive_keys:
        user.pop(key)
        # user.delete(key)  # Using both pop and del for demonstration

print(user)  # Output should be: {'user_name': 'John Doe', 'age': 30, 'is_active': True}

""" # This will raise a RuntimeError: dictionary changed size during iteration ==> Means we cannot modify a dictionary while iterating over it.
# Difference between pop and del:
# pop() removes the specified key and returns its value, while del removes the key without returning its value.
print(user)

for key in sensitive_keys:
    # to print the value being removed
    # print(f"Removing key: {key}, Value: {user.get(key)}")
    if key in user:
        user.pop(key, None)
    else:
        print(f"Key '{key}' not found in the dictionary.")
print(user)  # Output should be: {'user_name': 'John Doe', 'age': 30, 'is_active': True}

# Dont run the dict directly while iterating over it
# Instead, iterate over a copy of the keys


 