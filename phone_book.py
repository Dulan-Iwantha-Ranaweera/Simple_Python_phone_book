


contacts = [
    {"name": "Dulan", "phone": "0771234567"},
    {"name": "Prashan", "phone": "0712345678"},
    {"name": "Hasika", "phone": "0761234567"},
    {"name": "Kasun", "phone": "0751234567"}
]



def view_contacts():
    print("\n========== ALL CONTACTS ==========")

    if len(contacts) == 0:
        print("No contacts available.")
    else:
        for contact in contacts:
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("---------------------------------")



def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    new_contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(new_contact)

    print("Contact added successfully!")



def search_contact():
    search_name = input("Enter name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("\nContact Found!")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            found = True
            break

    if not found:
        print("Contact not found!")


def delete_contact():
    delete_name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")



while True:

    print("\n PHONE BOOK ")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank you for using Phone Book!")
        break

    else:
        print("Invalid choice! Please try again.")
