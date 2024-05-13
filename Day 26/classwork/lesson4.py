def print_char_by_index(name, index):
    if index < 0 or index >= len(name):
        print("Index out of range.")
    else:
        print("Character at index", index, "in", name, ":", name[index])

# ფუნქციის გამოძახება
name = "John"
index = 2
print_char_by_index(name, index)