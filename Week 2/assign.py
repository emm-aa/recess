def main():
    print("""=== Contact Manager Menu ===
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. Search Contacts
6. List All Contacts
7. Exit""")
    option = 0
    while option > 7 or option < 1:
        try:
            option = int(input("Choose an option (1-7): "))
            if option > 7 or option < 1:
                print("Please enter a correct number.")
        except ValueError:
            print("Please enter a whole number.")

    store = []

    def add_contact():
        print("Enter contact to add: ")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        new_contact = {"name": name, "phone": phone, "email": email}
        store.append(new_contact)
        return name + "" + phone

    match option:
        case 1:
            print()
            add_contact()
        case 2:
            print("Action 2")
        case 3:
            print("Action 3")
        case 4:
            print("Action 4")
        case 5:
            print("Action 5")
        case 6:
            print("Action 6")
        case 7:
            print("Action 7")


main()
