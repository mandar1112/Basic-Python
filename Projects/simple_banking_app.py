# Create a Simple Banking App 
# Includes: Check Balance, Deposit, Withdraw
from random import randint
Account_Data = {}

def create_account():
    print("\n   Create New Account   ")
    name = input("Enter Account Holder Name: ")
    age = int(input("Enter Account Holder Age: "))
    mobile_number = int(input("Enter Mobile Number of Account Holder: "))

    guardian_name = None
    guardian_age = None
    guardian_mobile_number = None

    if age < 18:
        print("You are Minor. Please Give Guardian Details.")
        guardian_name = input("Enter Guardian Name: ")
        guardian_age = int(input("Enter Guardian Age: "))
        if guardian_age >= 18:
            guardian_mobile_number = int(input("Enter Guardian Mobile Number: "))
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
    
    print("\nAccount Created.")
    print(f"\nAccount Number: {acc_no}, Account Holder Name: {Account_Data[acc_no]['Name']}")

def delete_account():
    print("\n   Delete Account   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        del Account_Data[acc_no]
        print("Account Successfully Deleted.")

def deposit():
    print("\n   Deposit Money   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        add_money = float(input("Enter the Amount: "))
        if add_money > 0:
            Account_Data[acc_no]["Balance"] = add_money + float(Account_Data[acc_no]["Balance"])
            print(f'Total Balance in Your Account {acc_no} is {Account_Data[acc_no]["Balance"]}')
        else:
            print("Invalid Amount.")

def withdraw():
    print("\n   Withdraw Money   ")
    acc_no = input("Enter Your Account Number: ")
    if acc_no not in Account_Data:
        print("Account Doesnt Exist.")
    else:
        money = float(input("Enter the Amount: "))
        if money > 0:
            if money <= Account_Data[acc_no]["Balance"]:
                Account_Data[acc_no]["Balance"] = float(Account_Data[acc_no]["Balance"]) - money
                print(f'Total Balance in Your Account {acc_no} is {Account_Data[acc_no]["Balance"]}')
            else:
                print("Insufficient Balance...")
        else:
            print("Invalid Amount.")

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
            Choice = int(input("\nEnter Your Choice: \n1. Create Account\n2. Delete Account\n3. Deposit Money\n4. Withdraw Money\n5. Check Balance\n6. Exit Loop\n"))
        except ValueError:
            print("Please Enter a Number Between 1-6.")
            continue
        match Choice:
            case 1: 
                create_account()
            case 2:
                delete_account()
            case 3:
                deposit()
            case 4:
                withdraw()
            case 5:
                check_balance()
            case 6:
                print("Exiting.....")
                break
            case _:
                print("Invalid Choice. Please Choose Between 1-6")

if __name__ == "__main__":
    main()
