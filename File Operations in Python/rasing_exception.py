# rasie

salary = float(input("Enter Salary: "))

if salary < 0:
    raise Exception("Salary Cannot be Negative.")
else:
    print(f"Your Salary is {salary}")
