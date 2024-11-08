class Contact:  #assigning subnames
    def __init__(self, Name, Phone, Email, Address):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email
        self.Address = Address
#manager for contact
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, Name, Phone, Email, Address): #adding contact
        contact = Contact(Name, Phone, Email, Address)
        self.contacts.append(contact)

    def view_contacts(self):        #for viewing contact
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.Name}, Phone: {contact.Phone}")

    def search_contact(self, query):        #for searching any contact
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.Name.lower() or query in contact.Phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(f"Name: {contact.Name}, Phone: {contact.Phone}")

    def update_contact(self, Name, New_name=None, new_phone=None, new_email=None, new_address=None): #updating contact
        for contact in self.contacts:
            if contact.Name == Name:
                if New_name:
                    contact.Name = New_name
                if new_phone:
                    contact.Phone = new_phone
                if new_email:
                    contact.Email = new_email
                if new_address:
                    contact.Address = new_address
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, Name): #for deleting contact
        for contact in self.contacts:
            if contact.Name == Name:
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()      #contact manager
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            Name = input("Enter Name: ")
            Phone = input("Enter Phone number: ")
            Email = input("Enter Email: ")
            Address = input("Enter Address: ")
            manager.add_contact(Name, Phone, Email, Address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter Name or Phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            Name = input("Enter the Name of the contact to update: ")
            New_name = input("Enter new Name (leave blank to keep the same): ")
            new_phone = input("Enter new Phone (leave blank to keep the same): ")
            new_email = input("Enter new Email (leave blank to keep the same): ")
            new_address = input("Enter new Address (leave blank to keep the same): ")
            manager.update_contact(Name, New_name or None, new_phone or None, new_email or None, new_address or None)
        elif choice == '5':
            Name = input("Enter the Name of the contact to delete: ")
            manager.delete_contact(Name)
        elif choice == '6':
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
