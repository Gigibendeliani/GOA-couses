budget = int(input("Enter your budget: "))
item_cost = int(input("Enter the cost of the desired item: "))
if budget >= item_cost:
    print("You can buy the item.")
else:
    print("You cannot buy the item.")