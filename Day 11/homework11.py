#1
for i in range(1, 51):
        if i % 5 == 0:
            print(i)
        
#2
for i in range(2, 21, 2):
    print(i)

#3
    product = 1
for num in range(5, 11):
    product *= num
print("Product:", product)

#4
user_number = int(input("Enter a number: "))
factorial = 1

for i in range(1, user_number + 1):
    factorial *= i

print(f"The factorial of {user_number} is: {factorial}")

#5

user_number = int(input("Enter a number: "))

while user_number != 1:
    if user_number % 2 == 0:
        user_number = user_number // 2
    else:
        user_number = (user_number * 3) + 1

    print(user_number)
