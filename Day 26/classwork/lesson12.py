def add_even_indices(name):
    new_name = ""
    for index, letter in enumerate(name):
        if index % 2 == 0:
            new_name += letter
    print("ფუნქციის გარეთ:", new_name)
    return new_name

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
name = "შემაჯამეთ"
result = add_even_indices(name)
print("დაბეჭდებული შედეგი:", result)