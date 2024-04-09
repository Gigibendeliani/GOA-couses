user_number = int(input("Enter a number: "))

while user_number != 1:
    if user_number % 2 == 0:
        user_number = user_number // 2
    else:
        user_number = (user_number * 3) + 1

    print(user_number)
