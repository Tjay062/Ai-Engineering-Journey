correct_username = "admin"
correct_password = "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
elif username == correct_username and password != correct_password:
    print("Incorrect password.")
elif username != correct_username and password == correct_password:
    print("Incorrect username.")
else:
    print("Invalid username or password.")
