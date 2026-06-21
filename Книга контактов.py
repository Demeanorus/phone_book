

def display_menu():
    cont = "Contact"
    print(f"""{cont} Book Menu: 
1. Add {cont}
2. View {cont}
3. Edit {cont}
4. Delete {cont}
5. List All {cont}
6. Exit""")

def add_contact(contact_book):
    name = input("Введите имя: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        phone = input("Введите номер телефона: ")
        email = input("Введите электронную почту: ")
        address = input("Введите адрес: ")
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")


def view_contact(contact_book):
    name = input("Введите имя для поиска абонента: ")
    if name in contact_book:
        contact = contact_book[name]
        output = (
            f"Name: {name}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}\n")
        print(output)
    else:
        print("Contact not found!")


def edit_contact(contact_book):
    name = input("Введите имя: ")
    if name in contact_book:
        current = contact_book[name]
        phone = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        address = input("Введите адрес: ")

        if phone == "":
            phone = current["phone"]
        if email == "":
            email = current["email"]
        if address == "":
            address = current["address"]

        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact(contact_book):
    name = input("Введите имя: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def list_all_contact(contact_book):
    if contact_book == {}:
        print("No contacts found!")
    else:
        for i in contact_book:
            print(f"Name: {i}")
            print(f"Phone: {contact_book[i]['phone']}\n"
                  f"Email: {contact_book[i]['email']}\n"
                  f"Address: {contact_book[i]['address']}\n")

def main():
    contact_book = {}

    while True:
        display_menu()
        choice = input("Выбор действия: ")
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            edit_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            list_all_contact(contact_book)
        elif choice == "6":
            exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()