def sum_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

start = 3
end = 7
print("Range:", start, "-", end)
print("Sum:", sum_range(start, end))