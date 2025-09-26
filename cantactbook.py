contacts = {}

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter 10-digit phone number: ")
    if not valid_phone(phone):
        print("Invalid phone number. It must be exactly 10 digits.")
        return
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"{name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name} | Phone: {details['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if name.lower() == keyword.lower() or details["phone"] == keyword:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new 10-digit phone number: ")
        if not valid_phone(phone):
            print("Invalid phone number. It must be exactly 10 digits.")
            return
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"{name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

menu()   