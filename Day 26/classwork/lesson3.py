def aritmettic_mean(start, end):
    numbers = list(range(start, end + 1))
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

start = 3
end = 7
print("Range:", start, "-", end)
print("aritmettic mean:", aritmettic_mean(start, end))