import json
import os

# File to store contacts
CONTACT_FILE = "contacts.json"

# ContactBook class handles contact operations
class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(CONTACT_FILE):
            with open(CONTACT_FILE, "r") as file:
                self.contacts = json.load(file)
        else:
            self.contacts = []

    def save_contacts(self):
        with open(CONTACT_FILE, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("✅ Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\n📒 Contact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self, keyword):
        results = [c for c in self.contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]
        if results:
            print("\n🔎 Search Results:")
            for c in results:
                self.display_contact(c)
        else:
            print("❌ No contact found.")

    def update_contact(self, phone):
        for c in self.contacts:
            if c['phone'] == phone:
                print("\nEnter new details (press Enter to keep existing):")
                name = input(f"New name [{c['name']}]: ") or c['name']
                new_phone = input(f"New phone [{c['phone']}]: ") or c['phone']
                email = input(f"New email [{c['email']}]: ") or c['email']
                address = input(f"New address [{c['address']}]: ") or c['address']

                c.update({
                    "name": name,
                    "phone": new_phone,
                    "email": email,
                    "address": address
                })
                self.save_contacts()
                print("✅ Contact updated.")
                return
        print("❌ Contact not found.")

    def delete_contact(self, phone):
        for c in self.contacts:
            if c['phone'] == phone:
                self.contacts.remove(c)
                self.save_contacts()
                print("🗑️ Contact deleted.")
                return
        print("❌ Contact not found.")

    def display_contact(self, contact):
        print(f"Name   : {contact['name']}")
        print(f"Phone  : {contact['phone']}")
        print(f"Email  : {contact['email']}")
        print(f"Address: {contact['address']}")
        print("-" * 30)


# Menu-driven interface
def main():
    book = ContactBook()
    while True:
        print("\n======= Contact Book Menu =======")
        print("1. Add New Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)

        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone to search: ")
            book.search_contact(keyword)

        elif choice == '4':
            phone = input("Enter phone number of contact to update: ")
            book.update_contact(phone)

        elif choice == '5':
            phone = input("Enter phone number of contact to delete: ")
            book.delete_contact(phone)

        elif choice == '6':
            print("👋 Thank you for using Contact Book.")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
main()
