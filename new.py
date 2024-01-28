import os


class AddressBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    contact_info = line.strip().split(',')
                    self.contacts.append(contact_info)
        except FileNotFoundError:
            pass  # File doesn't exist yet, it will be created when saving contacts

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            for contact_info in self.contacts:
                file.write(','.join(contact_info) + '\n')

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the Address Book.")
        else:
            for index, contact_info in enumerate(self.contacts, start=1):
                print(f"{index}. {', '.join(contact_info)}")

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        contact_info = [first_name, last_name, address,
                        city, state, zip_code, phone_number, email]
        self.contacts.append(contact_info)
        self.save_contacts()
        print("Contact added successfully.")

    def edit_contact(self, index, field, new_value):
        try:
            index = int(index) - 1
            field = int(field) - 1  # Convert the field to an integer
            self.contacts[index][field] = new_value
            self.save_contacts()
            print("Contact edited successfully.")
        except (ValueError, IndexError):
            print("Invalid index or field. Please provide valid values.")

    def delete_contact(self, index):
        try:
            index = int(index) - 1
            deleted_contact = self.contacts.pop(index)
            self.save_contacts()
            print(
                f"Contact deleted successfully: {', '.join(deleted_contact)}")
        except (ValueError, IndexError):
            print("Invalid index. Please provide a valid index.")


if __name__ == "__main__":
    file_path = r'C:\Users\hp\Documents\Ish\codes\file handling\contacts.txt'
    address_book = AddressBook(file_path)

    while True:
        print("\nAddress Book Menu:")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            address_book.display_contacts()
        elif choice == '2':
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            zip_code = input("Enter ZIP Code: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address_book.add_contact(
                first_name, last_name, address, city, state, zip_code, phone_number, email)
        elif choice == '3':
            address_book.display_contacts()
            index = input("Enter the index of the contact to edit: ")
            field = input("Enter the field to edit: ")
            new_value = input("Enter the new value: ")
            address_book.edit_contact(index, field, new_value)
        elif choice == '4':
            address_book.display_contacts()
            index = input("Enter the index of the contact to delete: ")
            address_book.delete_contact(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
