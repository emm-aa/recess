credentials = {"John": "john4live", "Arinda": "pass433", "Moses": "cooldays"}

while True:
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username in credentials:
        if credentials[input_username] == input_password:
            print("Login successful")
            break
        else:
            print("Incorrect password")
    else:
        print("Username not found")

    retry = input("Try again? (Y/N): ")
    if retry.lower() == "n":
        print("Goodbye")
        break
