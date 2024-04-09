min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
for num in range(min_value, max_value + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
