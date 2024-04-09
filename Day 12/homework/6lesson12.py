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