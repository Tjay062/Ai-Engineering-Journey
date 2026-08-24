correct_username = "admin"
correct_password = "1234"
username = input("Enter your username: ")
if username == correct_username:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Login successful!")
    else:
        print("Wrong password.")
if username != correct_username:
    print("Wrong username.")

