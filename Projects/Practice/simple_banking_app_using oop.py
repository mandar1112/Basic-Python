import json
import os
from random import randint



class BankAccount:

    def __init__(self, holder_name, holder_age, holder_mobile_number,
                 holder_guardian_name, holder_guardian_age,
                 holder_guardian_mobile_number, acc_no, pin, balance=0):

        self.holder_name = holder_name
        self.holder_age = holder_age
        self.holder_mobile_number = holder_mobile_number
        self.holder_guardian_name = holder_guardian_name
        self.holder_guardian_age = holder_guardian_age
        self.holder_guardian_mobile_number = holder_guardian_mobile_number
        self.acc_no = acc_no
        self.pin = pin      
        self.balance = balance

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False




class BankDatabase:

    FILE = "account.json"

    def __init__(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as fh:
                raw = json.load(fh)
        else:
            raw = {}

        self.accounts = {}

        for acc_no, data in raw.items():
            self.accounts[acc_no] = BankAccount(**data) # **data means Unpack dictionary and send as arguments to constructor.

    def save(self):
        raw = {}
        for acc_no, acc in self.accounts.items():
            raw[acc_no] = acc.__dict__

        with open(self.FILE, "w") as fh:
            json.dump(raw, fh, indent=4)

    def add_account(self, account):
        self.accounts[account.acc_no] = account
        self.save()

    def get(self, acc_no):
        return self.accounts.get(acc_no)

    def delete(self, acc_no):
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            self.save()
            return True
        return False




class BankSystem:

    def __init__(self):
        self.db = BankDatabase()

    def create_account(self):
        name = input("Name: ")
        age = int(input("Age: "))
        mobile = input("Mobile: ")
        pin = int(input("Create PIN: "))

        guardian_name = guardian_age = guardian_mobile = None

        if age < 18:
            guardian_name = input("Guardian Name: ")
            guardian_age = int(input("Guardian Age: "))
            guardian_mobile = input("Guardian Mobile: ")

        acc_no = str(randint(1000000000, 9999999999))

        acc = BankAccount(name, age, mobile,
                          guardian_name, guardian_age,
                          guardian_mobile, acc_no, pin)

        self.db.add_account(acc)
        print("Account Created:", acc_no)

    def login(self):
        acc_no = input("Account No: ")
        pin = int(input("PIN: "))

        acc = self.db.get(acc_no)
        if acc and acc.check_pin(pin):
            self.dashboard(acc)
        else:
            print("Invalid Login")

    def dashboard(self, acc):
        while True:
            print("\n1.Deposit\n2.Withdraw\n3.Balance\n4.Logout")
            ch = input("Choice: ")

            if ch == "1":
                amt = float(input("Amount: "))
                acc.deposit(amt)
                self.db.save()

            elif ch == "2":
                amt = float(input("Amount: "))
                acc.withdraw(amt)
                self.db.save()

            elif ch == "3":
                print("Balance:", acc.balance)

            else:
                break




def main():
    app = BankSystem()
    while True:
        print("\n1.Create\n2.Login\n3.Exit")
        ch = input("Choice: ")

        if ch == "1":
            app.create_account()
        elif ch == "2":
            app.login()
        else:
            break

main()



