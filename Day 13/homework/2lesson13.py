user_num = int(input("Please enter your number: "))
if user_num % 2 == 0 and user_num > 0:
    print("Your number is even")
elif user_num % 2 == 1:
    print("Your number is odd")
else:
    print("your number equlas to zero")