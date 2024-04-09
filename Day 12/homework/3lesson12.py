min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
num_steps = int(input("Enter the number of steps: "))
for i in range(min_value, max_value + 1, num_steps):
    print(i)