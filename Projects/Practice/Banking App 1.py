import os
from curses.ascii import isdigit
from random import randint
from re import fullmatch
import json

# Banking App Try 1

class Validate:

    @staticmethod
    def validate_name(name):
        if str(name).isdigit() or len(str(name)) <= 1 or len(str(name)) > 20 or name == "" or name == None:
            return False
        name = name.strip()
        if not name:
            return False
        return bool(fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", name))

    @staticmethod
    def validate_age(age):
        try:
            if age <= 0 or not age:
                print("Please enter a valid age")
                return False
            else:
                return True
        except ValueError:
            print("Invalid age")
            return False

    @staticmethod
    def validate_age_holder(age):
        if not Validate.validate_age(age):
            return False
        else:
            if age <= 18:
                print("Account Holder is UnderAge Required Guardian")
                return BankAccount.guardian()
            else:
                return True
                

    @staticmethod
    def validate_age_holder_guardian(age):
        if not Validate.validate_age(age):
            return False
        else:
            if age <= 18:
                print(f"{BankAccount.self.guardian_name} is UnderAge Required Guardian Above 18.")
                return False
            else:
                guardian_name = guardian_age = guardian_mobile_number = None
                return True

    @staticmethod
    def validate_mobile_number(mobile_number):
        if mobile_number.startswith("+91"):
            mobile_number = mobile_number[3:]
        return bool(fullmatch(r"[6-9]\d{9}", mobile_number))

    @staticmethod
    def validate_KYC(KYC):
        if not KYC:
            print("Invalid KYC")
        return bool(fullmatch(r"[0-9]\d{11}", KYC))

class BankAccount:

    def __init__(self, name, age, mobile_number, guardian_name, guardian_age, guardian_mobile_number, acc_no, pin, pin_attempt, Locked = False, balance = 0.0, KYC = False):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.guardian_name = guardian_name
        self.guardian_age = guardian_age
        self.guardian_mobile_number = guardian_mobile_number
        self.acc_no = acc_no
        self.pin = pin
        self.pin_attempt = pin_attempt
        self.Locked = Locked
        self.balance = balance
        self.KYC = KYC

    def verify_pin(self, pin):
        if self.pin == pin:
            return True
        return False

    def verify_acc_no(self, acc_no):
        if self.acc_no == acc_no:
            return True
        return False

    def verify_pin_attempt(self, pin_attempt):
        if self.pin_attempt == pin_attempt:
            return True
        return False

    def KYC(self, KYC):
        if self.KYC == KYC:
            return True
        return False

    def verify_pin(self, pin):
        if self.pin == pin:
            return True
        return False

    def deposit(self, amount):
        if self.Locked == False:
            print("\n    Deposit Money    ")
            acc_no = self.acc_no
            if not BankAccount.verify_acc_no(acc_no):
                print("\n    Invalid Account Number")
                return False
            else:
                if amount <= 0:
                    print("Invalid Amount")
                    return False
                else:
                    self.balance += amount
                    return True
        return False

    def withdraw(self, amount):
        if self.Locked == False:
            print("\n    Withdraw Money    ")
            acc_no = self.acc_no
            if not BankAccount.verify_acc_no(acc_no):
                print("\n    Invalid Account Number")
                return False
            else:
                if amount <= 0:
                    print("Invalid Amount")
                    return False
                else:
                    self.balance -= amount
                    return True
        return False

    def guardian(self):
        
        guardian_name = input("Enter Guardian Name: ")
        if not Validate.validate_name(guardian_name):
            print("Invalid Name")
            return False
        self.guardian_name = guardian_name

        age = int(input("Enter Guardian Age: "))
        if not Validate.validate_age_holder_guardian(self.guardian_age):
            print("Invalid Age")
            return False
        self.guardian_age = age

        guardian_mobile_number = int(input("Enter Guardian Mobile Number: "))
        if not Validate.validate_mobile_number(guardian_mobile_number):
            print("Invalid Mobile Number")
            return False
        self.guardian_mobile_number = guardian_mobile_number
    


class BankDatabase:

    FILE = "accounts.json"

    def __init__(self):
        if os.path.exists(self.FILE:
            with open(BankDatabase.FILE, "r") as fh:
                raw = json.load(fh)
        else:
            raw = {}

        self.accounts = {}

        for acc_no, data in raw.items():
            self.accounts[acc_no] = BankAccount(**data)

    def save(self):
        raw = {}
        for acc_no, account in self.accounts.items():
            raw[acc_no] = account.__dict__

        with open(self.FILE, "w") as fh:
            json.dump(raw, fh, indent=4)

    def load(self):
        for acc_no, account in self.accounts.items():
            with open(self.FILE, "r") as fh:
                raw = json.load(fh)

    def add_account(self, account):
        self.accounts[account.acc_no] = account
        self.save()

    def get_account(self, acc_no):
        return self.accounts[acc_no]

    def delete_account(self, acc_no):
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            self.save()
            return True
        return False


class BankSystem:

    def __init__(self):
        self.db = BankDatabase()

    def create_account(self):
        name = input("\nEnter your name: ")
        if not Validate.validate_name(name):
            print("\n    Invalid Name")
            return False

        age = input("\nEnter your age: ")
        if not Validate.validate_age_holder(age):
            return False
        else:
            self.age = age

        mobile_number = input("\nEnter your mobile number: ")
        if not Validate.validate_mobile_number(mobile_number):
            print("\n    Invalid Mobile Number")
            return False
        else:
            self.mobile_number = mobile_number
        
        KYC = input("Enter KYC Number(Aadhaar Number): ")
        if not Validate.validate_KYC(KYC):
            return False
        self.KYC = KYC

        pin = input("\nEnter your pin: ")
        self.pin = pin

        acc_no = str(randint(100000000000,999999999999))
        acc = BankAccount(name, age, mobile_number, )

        





