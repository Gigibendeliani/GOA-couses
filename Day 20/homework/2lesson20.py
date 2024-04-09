input_list = [1, 1, 2, 2, 3]


unique_elements = []
for item in input_list:
    if input_list.count(item) == 2 and item not in unique_elements:
        unique_elements.append(item)
if not unique_elements:
    print("List is empty")
else:
    print(unique_elements)