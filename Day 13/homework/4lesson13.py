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