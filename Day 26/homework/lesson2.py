def is_even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

# ფუნქციის შემოწმება
number = 7
result = is_even_or_odd(number)
if result:
    print(f"{number}-ი ლუწია.")
else:
    print(f"{number}-ი კენტია.")