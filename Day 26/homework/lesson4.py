def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# ფუნქციის შემოწმება
number = 13
if is_prime(number):
    print(f"{number}-ი მარტივია.")
else:
    print(f"{number}-ი მარტივი არ არის.")