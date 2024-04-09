correct_password = "my_password"
attempts = 0
while attempts < 5:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print("Access denied. Please try again.")
        if attempts == 5:
            print("System locked.")