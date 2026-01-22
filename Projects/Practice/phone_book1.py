# Contact Book

import json, os
from re import fullmatch


class Contact:

    def __init__(self, name, mobile_number):
        self.name = name
        self.mobile_number = mobile_number
    
    def show(self):
        return f"{self.name} : {self.mobile_number}"

    @staticmethod
    def validate_mobile_number(mobile_number):
        return bool(fullmatch(r"\d{10}", mobile_number))


class ContactDatabase:

    FILE = "contact.json"

    def __init__(self):
        self.contacts = {}
        self.load()

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        self.save()
    
    def search(self, name):
        return self.contacts.get(name)
    
    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save()
    
    def view_all(self):
        return self.contacts.values()
    
    def save(self):
        contact_data = {}
        for name, data in self.contacts.items():
            contact_data[name] = {"Name" : data.name, "Mobile Number" : data.mobile_number}

        with open(self.FILE, "wt") as fh:
            json.dump(contact_data, fh, indent=4)

    def load(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "rt") as fh:
                raw = json.load(fh)
                for name, data in raw.items():
                    self.contacts[name] = Contact(**data)
         
def main():

    db = ContactDatabase()

    while True:
        choice = int(input("\n1. Add Contact\n2. Search Contact\n3. View ALL\n4. Exit\n Enter Choice: "))
        
        match choice:
            case 1:

                ch = int(input("\n1. Adding Single Contact\n2. Adding Multiple Contact\n Enter Choice: "))
                
                if ch == 1:
                    name = input("Name: ")
                    mobile_number = input("Mobile Number: ")

                    if Contact.validate_mobile_number(mobile_number):
                        db.add_contact(Contact(name, mobile_number))
                        print("Contact Added")
                    else:
                        print("Invalid Mobile Number")
                elif ch == 2:        
                    print("Adding Contact")
                    n_contacts = int(input("How many contacts do you want to add?: "))

                    for i in range(n_contacts):
                        name = input("Enter The Name of the Contact: ")
                        mobile_number = int(input("Enter the mobile number: "))
                        if Contact.validate_mobile_number(mobile_number):
                            db.add_contact(Contact(name, mobile_number)) 
                            print("Contact Added")   
                        else:
                            print(f"Invalid Mobile Number for {name}")
            
                    print("Contacts Added Succesfully.")
                else:
                    "Invalid Choice..."
                    exit()
            case 2:
                name = input("Search Name: ")
                contact = db.search(name)
                print(contact.show() if contact else "Not Found")
            case 3:
                for contact in db.view_all():
                    print(contact.show())
            case 4:
                print("Exiting.....")
            case _:
                print("Invalid Choice!")

main()
