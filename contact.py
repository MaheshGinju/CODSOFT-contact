import os

# Define a contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Function to display the menu
def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
1

# Function to add a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print(contact)

# Function to search a contact by name
def search_contact(contacts):
    name = input("Enter the name of the contact you want to search: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == name.lower():
            print(contact)
            found = True
            break
    if not found:
        print("Contact not found.")

# Function to delete a contact by name
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted successfully.")
            found = True
            break
    if not found:
        print("Contact not found.")

# Function to save contacts to a file
def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(f"{contact.name},{contact.phone},{contact.email}\n")
    print("Contacts saved to file.")

# Function to load contacts from a file
def load_contacts(filename="contacts.txt"):
    contacts = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append(Contact(name, phone, email))
    return contacts

# Main function to run the contact book
def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
