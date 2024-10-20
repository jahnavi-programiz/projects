class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact.name} - {contact.phone}")
    else:
        print("No contacts available.")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    else:
        print("No contacts found.")

def update_contact():
    search_term = input("Enter name or phone number to update: ")
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone:
            contact.name = input("Enter new name: ")
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone:
            contacts.remove(contact)
            print("Contact deleted successfully.")                    
            return
    print("Contact not found.")

def main():
    while True:
        print('''Options:
        1. Add Contact
        2. View Contacts  
        3. Search Contact
        4. Update Contact  
        5. Delete Contact  
        6. Exit''')
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
