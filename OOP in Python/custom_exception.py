# Exception are generally classes.
# Exception is child of BaseException.


class SalaryError(Exception):
    pass

def get_salary(salary):
    if salary < 0:
        raise SalaryError("Salary Cannot be Negative!")
    else:
        return salary + (0.1 * salary)
    
salary = float(input("Enter Your Salary: "))
total_salary = get_salary(salary)
print(total_salary)