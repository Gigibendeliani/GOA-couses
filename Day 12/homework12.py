#1
budget = float(input("Enter your budget: "))
item_cost = float(input("Enter the cost of the desired item: "))
if budget >= item_cost:
    print("You can buy the item.")
else:
    print("You cannot buy the item.")

#2
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

#3
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
num_steps = int(input("Enter the number of steps: "))
for i in range(min_value, max_value + 1, num_steps):
    print(i)


#4
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The data is correct.")
else:
    print("The data is incorrect. Please try again.")


#5
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
for num in range(min_value, max_value + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


#6
num1 = float(input("ჩაწერე პირველი რიცხვი: "))
num2 = float(input("ჩაწერე მეორე რიცხვი: "))
operator = input("აირჩიე ოპერატორები (+, -, *, /, ^): ")


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("შეცდომა ნულზე გაყოფა არ შეიძლება.")
        result = None
    else:
        result = num1 / num2
elif operator == "^":
    result = num1 ** num2
else:
    print("შეცდომა.")
    result = None

if result is not None:
    print(f"პასუხი {result}.")

while True:
    user_number = int(input("Enter a number: "))
    
    if user_number % 2 == 0 or user_number % 3 == 0:
        print(f"{user_number} is a multiple of 2 or 3.")
        break
    else:
        print(f"{user_number} is not a multiple of 2 or 3. Try again.")

# 7
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#8
leg1 = float(input("\nEnter the length of the first leg of a right triangle: "))
leg2 = float(input("Enter the length of the second leg of a right triangle: "))

hypotenuse = (leg1 + leg2)**0.5
print(f"The hypotenuse of the right triangle is: {hypotenuse:.2f}")

#9
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to participate in elections.")
else:
    print("You are not eligible to participate in elections yet.")