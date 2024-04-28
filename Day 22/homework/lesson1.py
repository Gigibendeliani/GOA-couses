word = input("შეიყვანეთ სიტყვა: ")

if len(word) > 3:
    print(word[:3])
else:
    print(word[0])
