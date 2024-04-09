word = input("შეიყვანეთ სიტყვა: ")
if word == word[::-1]:
    print(f"{word} არის პალინდრომი.")
else:
    print(f"{word} არ არის პალინდრომი.")
    