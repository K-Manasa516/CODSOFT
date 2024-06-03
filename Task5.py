class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("contacts not found.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deletion is successfully.")
        else:
            print("Invalid contact indexing.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add your Contact")
        print("2. View your Contact List")
        print("3. Search your Contact")
        print("4. Update your Contact")
        print("5. Delete your Contact")
        print("6. Exit")

        choice = input("Enter ur choice: ")

        if choice == '1':
            name = input("Enter their name: ")
            phone_number = input("Enter their phone number: ")
            email = input("Enter their email: ")
            address = input("Enter their address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact addition is successfully.")
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Search Results:")
                for idx, contact in enumerate(found_contacts, start=1):
                    print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter the new name: ")
            phone_number = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.update_contact(index, new_contact)
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6")

if __name__ == "__main__":
    main()
