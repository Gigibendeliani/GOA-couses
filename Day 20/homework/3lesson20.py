words = input("შემოიტანეთ ხუთი სიტყვა: ").split()
result = ""
for word in words:
    if len(word) > 0:
        result += word[0]
if result:
    print(result)
else:
    print("Empty string")