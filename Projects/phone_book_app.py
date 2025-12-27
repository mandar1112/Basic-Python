# Phone Book Directory


class Contact:
    phone_directory = []

    def __init__(self, name, mobile_number):
        self.name = name
        self.phone = mobile_number
        Contact.phone_directory.append(self)
    
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
        print("Contact Not Found!")


    @staticmethod
    def validate_phone_number(number):
        number = str(number)
        if len(number) == 10 and number.isdigit():
            return True
        else:
            return False



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


n_contacts = int(input("How many contacts do you want to add?: "))

for i in range(n_contacts):
    name = input("Enter The Name of the Contact: ")
    mobile_number = int(input("Enter the mobile number: "))
    if Contact.validate_phone_number(mobile_number):
        Contact(name, mobile_number)    
    else:
        print(f"Invalid Mobile Number for {name}")

Contact.show_all_contact()