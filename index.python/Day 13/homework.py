#1
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#2
        def check_number():
          number = input("შეიყვანეთ რიცხვი: ")
    try:
        number = float(number)
        if number > 0:
            print(f"{number} არის დადებითი.")
        elif number < 0:
            print(f"{number} არის უარყოფითი.")
        else:
            print(f"{number} არის ნულოვანი.")
    except ValueError:
        print("შეცდომა: გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")

check_number()


#3

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


#4
        
        # მოცემული ცვლადის შექმნა და ინიციალიზაცია
total = 0
# რიცხვი, რომელიც განსაზღვრავს რამდენი რიცხვის ჯამის დათვლას გვინდა
number = 1

# while ციკლი, რომელიც გამოიყენებს რიცხვების ჯამის დათვლის
while number <= 100:
    total += number
    number += 1

# შედეგის ბეჭდვა
print("1-დან 100-მდე რიცხვების ჯამია:", total)


#5

number = int(input("შემოიტანეთ რიცხვი: "))

if number == 1:
    print("ორშაბათი")
elif number == 2:
    print("სამშაბათი")
elif number == 3:
    print("ოთხშაბათი")
elif number == 4:
    print("ხუთშაბათი")
elif number == 5:
    print("პარასკევი")
elif number == 6:
    print("შაბათი")
elif number == 7:
    print("კვირა")
else:
    print("არასწორი რიცხვი")

#6
    number = int(input("შემოიტანეთ რიცხვი: "))

if number == 0:
    print("რიცხვი ნულია")
elif number % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")

#7
    
