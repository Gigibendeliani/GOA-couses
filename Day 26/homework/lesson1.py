def sum_of_even_indices(numbers):
    total = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            total += numbers[i]
    return total

# შევამოწმოთ ფუნქციის მუშაობა
numbers = [1, 2, 3, 4, 5,]