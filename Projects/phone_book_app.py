# Phone Book Directory
import json
import os
from re import fullmatch

class ContactDatabase:

    FILE = "contacts.json"

    
    def __init__(self):
        self.contacts = {}
        self.load()
    
    # Load Contact
    def load(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "rt") as fh:
                raw = json.load(fh)
                for name, data in raw.items():
                    self.contacts[name] = Contact(**data)

    # Save Data
    def save_data(self):
        raw = {}

        for name, data in self.Contact_Data.items():
            raw[name] = data.__dict__


        with open("FILE", "wt") as fh:
            json.dump(self.Contact_Data, fh, indent=4)
    
    # Add Contact
    def add_contact(self, name):
        self.Contact_Data[name] = name




class Contact:

    def __init__(self, name, mobile_number):
        self.name = name
        self.phone = mobile_number
    
    def show_contact(self):
        return f"Name: {self.name}, Contact Number: {self.phone}"


    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory!")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())
    

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.show_contact()     
        return f"Contact Not Found for {search_name}"


    @staticmethod
    def validate_phone_number(number):
        number = str(number)
        #if len(number) == 10 and number.isdigit():
        #    return True
        #else:
        #    return False
        return bool(fullmatch(r"\d{10}", number))





"""
c1 = Contact("John", 9876543210)
c2 = Contact("Alice", 9076543218)
c3 = Contact("Carol", 1234567890)
# print(Contact.phone_directory)

# print(c1.show_contact())
# print(c2.show_contact())

Contact.show_all_contact()

# print(c1.__dict__)
# print(c2.__dict__)



# Search Contact
print(Contact.search_contact("John"))
print(Contact.search_contact("john"))
print(Contact.search_contact("Mark"))


print()
print()
print()
print()
"""

def main():
    
    ch = int(input("1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. View All Contact\5. Exit"))
    
    match ch:

        case 1:
            print("Adding Contact")
            n_contacts = int(input("How many contacts do you want to add?: "))

            for i in range(n_contacts):
                name = input("Enter The Name of the Contact: ")
                mobile_number = int(input("Enter the mobile number: "))
                if Contact.validate_phone_number(mobile_number):
                    Contact(name, mobile_number)    
                else:
                    print(f"Invalid Mobile Number for {name}")
            
            print("Contact Added Succesfully.")
        
        case 2:
            name = input("Enter the Name to Search in Contact List: ")
            Contact.search_contact(name)
        
        case 3:
            name = input("Enter the Name to Delete in Contact List: ")
            Contact.






Contact.show_all_contact()