# Create a Simple Banking App 
# Includes: Create Account, Delete Account, Deposit, Withdraw, Check Balance
from random import randint
import json
import os
import re

File_Name = "Account Details.json" # File Name

# Loading Existing Data
if os.path.exists(File_Name):
    with open(File_Name, "rt") as fh:
        Account_Data = json.load(fh)
else:
    Account_Data = {}
    with open(File_Name, "wt") as fh:
        json.dump(Account_Data, fh)

# Save Function
def save_data():
    with open(File_Name, "wt") as fh:
        json.dump(Account_Data, fh, indent=4)

# To Check Name is Valid or not
def validate_name(name):
    name = name.strip()
    if not name:
        return False
    return bool(re.fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", name))

# To Check mobile number is valid or not
def validate_mobile_number(mobile_number):
    if mobile_number.startswith("+91"):
        mobile_number = mobile_number[3:]
    return bool(re.fullmatch(r"[6-9]\d{9}", mobile_number))

# Create Account
def create_account():
    print("\n   Create New Account   ")
    
    name = input("Enter Account Holder Name: ") 
    if not validate_name(name):
        print("Invalid Name.")
        return
    
    try:    
        age = int(input("Enter Account Holder Age: "))
        if age <= 0:
            print("Please Enter Real Age.")
            return
    except ValueError:
        print("Invalid Age.")
        return
    mobile_number = input("Enter Mobile Number of Account Holder: ")
    if not validate_mobile_number(mobile_number):
        print("Invalid Mobile Number. Enter 10-digit numeric number.")
        return
    
    guardian_name = guardian_age = guardian_mobile_number = None

    if age < 18:
        print("You are Minor. Please Give Guardian Details.")
        guardian_name = input("Enter Guardian Name: ")
        if not validate_name(guardian_name):
            print("Invalid Name.")
            return
        
        try:    
            guardian_age = int(input("Enter Guardian Age: "))
            if guardian_age <= 0:
                print("Please Enter Real Age.")
                return
        except ValueError:
            print("Invalid Age.")
            return
        if guardian_age >= 18:
            guardian_mobile_number = input("Enter Guardian Mobile Number: ")
            if not validate_mobile_number(guardian_mobile_number):
                print("Invalid Gaurdian Mobile Number.")
                return
        else:
            print(f'{guardian_name} is not eligible.')
            return
        
    while True:
            acc_no = str(randint(10000000000,99999999999))
            if acc_no not in Account_Data:
                break
        
    if age >= 18:
        
        Account_Data[acc_no] = {
            "Name" : name,
            "Age" : age,
            "Mobile Number" : mobile_number,
            "Guardian Name" : None,
            "Guardian Age" : None,
            "Guardian Mobile Number" : None,
            "Balance" : 0.0
        }

    else:
        acc_no = acc_no + "M"
        
        Account_Data[acc_no] = {
            "Name" : name,
            "Age" : age,
            "Mobile Number" : mobile_number,
            "Guardian Name" : guardian_name,
            "Guardian Age" : guardian_age,
            "Guardian Mobile Number" : guardian_mobile_number,
            "Balance" : 0.0
        }
    
    save_data()
    print("\nAccount Created.")
    print(f"\nAccount Number: {acc_no}, Account Holder Name: {Account_Data[acc_no]['Name']}")

# Delete Account
def delete_account():
    print("\n   Delete Account   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        del Account_Data[acc_no]
        save_data()
        print("Account Successfully Deleted.")

# Deposit Money
def deposit():
    print("\n   Deposit Money   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        try:
            add_money = float(input("Enter the Amount: "))
        except ValueError:
            print("Invalid Amount.")
            return
        if add_money > 0:
            Account_Data[acc_no]["Balance"] += add_money
            save_data()
            print(f'Total Balance in Your Account {acc_no} is {Account_Data[acc_no]["Balance"]}')
        else:
            print("Invalid Amount.")

# Withdraw Money
def withdraw():
    print("\n   Withdraw Money   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        try:
            money = float(input("Enter the Amount: "))
        except ValueError:
            print("Invalid Amount.")
            return
        if money > 0:
            if money <= Account_Data[acc_no]["Balance"]:
                Account_Data[acc_no]["Balance"] -= money
                save_data()
                print(f'Total Balance in Your Account {acc_no} is {Account_Data[acc_no]["Balance"]}')
            else:
                print("Insufficient Balance...")
        else:
            print("Invalid Amount.")

# Check Balance
def check_balance():
    print("\n   Check Balance   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        print(f'Total Balance in Your Account {acc_no} is {Account_Data[acc_no]["Balance"]}')

def main():
    while True:
        try:
            choice = int(input("""
1. Create Account
2. Delete Account
3. Deposit
4. Withdraw
5. Check Balance
6. Exit
Enter Choice: """))
        except ValueError:
            print("Please Enter a Number Between 1-6.")
            continue
        match choice:
            case 1: create_account()
            case 2: delete_account()
            case 3: deposit()
            case 4: withdraw()
            case 5: check_balance()
            case 6:
                print("Exiting.....")
                break
            case _:
                print("Invalid Choice. Please Choose Between 1-6")

if __name__ == "__main__":
    main()
