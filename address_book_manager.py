#Ish Kwatra
import os

# class with all functions for different commands and opening contact file


class AddressBook:

    # loading contacts using constructor
    def __init__(self, file_path):

        self.file_path = file_path
        self.contacts = []
        self.load_contacts()

    # opening file and storing its contents in a 2d list named contacts

    def load_contacts(self):

        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    contact_info = line.strip().split(',')
                    self.contacts.append(contact_info)

        except FileNotFoundError:
            pass  # File doesn't exist yet, it will be created when saving contacts

    # to save the text file after every edit,
    # because whatever add/edit/delete we do, is in our 2d list named contacts,
    # and not the text file, so we need to update this 2d list onto our text file after every update.

    def save_contacts(self):

        with open(self.file_path, 'w') as file:
            for contact_info in self.contacts:
                file.write(','.join(contact_info) + '\n')

    # printing contacts

    def display_contacts(self):

        if not self.contacts:
            print(
                "\n************************************************************************\n")
            print("No contacts in the Address Book.")

        else:
            print(
                "\n************************************************************************\n")
            # (ind,contact_info) is a tuple where ind is serial number and contact_info is individual contact
            # we print line by line the serial number and the individual contact which is a list by joining the fields with comma
            # join function combines elemnts and outputs a string
            for ind, contact_info in enumerate(self.contacts, start=1):
                print(f"{ind}. {', '.join(contact_info)}")

    # searching and printing contacts

    def search_display(self, fname):

        if not self.contacts:
            print(
                "\n************************************************************************\n")
            print("No contacts in the Address Book.")

        elif fname.lower() not in [i[0].lower() for i in self.contacts]:
            print(
                "\n************************************************************************\n")
            print("No contact with the given name exists in the Address Book.")

        else:
            print(
                "\n************************************************************************\n")
            for ind, contact_info in enumerate([i for i in self.contacts if i[0].lower() == fname.lower()], start=1):
                print(f"{ind}. {', '.join(contact_info)}")

    # to add a contact at the end of our list

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone_number, email):

        # appending our 2d list
        contact_info = [first_name, last_name, address,
                        city, state, zip_code, phone_number, email]
        self.contacts.append(contact_info)

        # saving it to the text file
        self.save_contacts()
        print(
            "\n************************************************************************\n")
        print("Contact added successfully.")

    # editing our contact list
    # first we find indeces of all contacts with the given first name and store it in ind_list
    # we then print all contacts with same first name as given and ask user to choose 1
    # we then choose that index from our ind_list

    def edit_contact(self, fname):

        if not self.contacts:
            print(
                "\n************************************************************************\n")
            print("No contacts in the Address Book.")

        elif fname.lower() not in [i[0].lower() for i in self.contacts]:
            print(
                "\n************************************************************************\n")
            print("No contact with the given name exists in the Address Book.")

        else:
            try:
                # finding index of contact with given first name
                ind = 0
                ind_list = []
                for i in self.contacts:
                    if i[0].lower() == fname.lower():
                        ind_list.append(ind)
                        ind += 1
                    else:
                        ind += 1
                for i, contact_info in enumerate([j for j in self.contacts if j[0].lower() == fname.lower()], start=1):
                    print(f"{i}. {', '.join(contact_info)}")
                temp = int(input("Enter index of contact to be edited: "))
                if temp not in range(1, len(ind_list)+1):
                    print(
                        f"Invalid index. Please provide a valid index in range {1}-{len(ind_list)}.")
                    return 0
                ind = ind_list[temp-1]

                # getting the field to be edited
                print("1. First Name")
                print("2. Last Name")
                print("3. Address")
                print("4. City")
                print("5. State")
                print("6. ZIP Code")
                print("7. Phone Number")
                print("8. Email")
                field = int(input("Enter the field to edit: "))
                if field not in range(1, 9):
                    print("Invalid index. Please provide a valid index in range 1-8.")
                    return 0

                # asking new value
                new_value = input("Enter the new value: ")
                self.contacts[ind][field-1] = new_value

                # saving it to our text file
                self.save_contacts()
                print(
                    "\n************************************************************************\n")
                print("Contact edited successfully.")

            except (ValueError):
                print(
                    "\n************************************************************************\n")
                print("Invalid index or field. Please provide integer values.")

    # deleting given contact
    # required index is found same way as done for editing a contact

    def delete_contact(self, fname):

        if not self.contacts:
            print(
                "\n************************************************************************\n")
            print("No contacts in the Address Book.")

        elif fname.lower() not in [i[0].lower() for i in self.contacts]:
            print(
                "\n************************************************************************\n")
            print("No contact with the given name exists in the Address Book.")

        else:
            try:
                # finding the index
                ind = 0
                ind_list = []
                for i in self.contacts:
                    if i[0].lower() == fname.lower():
                        ind_list.append(ind)
                        ind += 1
                    else:
                        ind += 1
                for i, contact_info in enumerate([j for j in self.contacts if j[0].lower() == fname.lower()], start=1):
                    print(f"{i}. {', '.join(contact_info)}")
                temp = int(input("Enter index of contact to be deleted: "))
                if temp not in range(1, len(ind_list)+1):
                    print(
                        f"Invalid index. Please provide a valid index in range {1}-{len(ind_list)}.")
                    return 0
                ind = ind_list[temp-1]

                # deletion by popping
                deleted_contact = self.contacts.pop(ind)

                # saving this 2d list onto our text file
                self.save_contacts()
                print(
                    "\n************************************************************************\n")
                print(
                    f"Contact deleted successfully: {', '.join(deleted_contact)}")

            except (ValueError):
                print(
                    "\n************************************************************************\n")
                print("Invalid index. Please provide integer values.")


if __name__ == "__main__":
    # giving contact text file location
    file_path = r'C:\Users\hp\Documents\Ish\codes\file handling\contacts.txt'
    # creating object in our class
    address_book = AddressBook(file_path)

    while True:
        print("\n************************************************************************")
        print("\nWelcome to Address Book!")
        print("\nAddress Book Menu:")
        print("1. Display All Contacts")
        print("2. Search and display a contact")
        print("3. Add Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            address_book.display_contacts()
        elif choice == '2':
            fname = input("Enter the first name of the contact: ")
            address_book.search_display(fname)
        elif choice == '3':
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
        elif choice == '4':
            fname = input("Enter the first name of the contact: ")
            address_book.edit_contact(fname)
        elif choice == '5':
            fname = input("Enter the first name of the contact: ")
            address_book.delete_contact(fname)
        elif choice == '6':
            break
        else:
            print(
                "\n************************************************************************\n")
            print("Invalid choice. Please enter a number between 1 and 6.")
