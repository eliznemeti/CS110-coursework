## Name:
## ID:
## Save this file as yourname_cs110_lab10.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""
# [10 pts] Task 1

# [3 pts] Create a list called number_list with numbers from 1 to 20
number_list = list(range(1, 21))
print("Initial list:", number_list)

# [6 pts] Remove every 3rd element in number_list, starting from the first element
# Hint: Use slicing and element removal
del number_list[2::3]
# Another solution:
#number_list = [num for i, num in enumerate(number_list) if (i + 1) % 3 != 0]

# # another solution:
# for n in number_list:
#     if n % 3 == 0:
#         number_list.remove(n)

# [1 pt] Print number_list to display the final result
print("After removing every 3rd element:", number_list)

# [10 pts] Task 2

## [3 pts] Part 1
# [1.5] Create two shopping lists: grocery and electronic
grocery = ["apples", "bananas", "carrots", "dates", "eggplant"]
electronic = ["laptop", "headphones", "camera", "smartphone", "charger"]

# [0 pts] Print lists before sorting
print("\nGrocery list before sorting:", grocery)
print("Electronic list before sorting:", electronic)

# [1.5] Sort each list
grocery.sort()
electronic.sort()

# [0 pts] Print after sorting
print("Grocery list after sorting:", grocery)
print("Electronic list after sorting:", electronic)

## [7 pts] Part 2
# [1 pt] Create a table: shopping_table
shopping_table = [[], []]

# [1.5 pt] Collect the first two items from the grocery list into the table
shopping_table[0].extend(grocery[:2])

# [1.5 pt] Collect the last two items from the electronics list into the table
shopping_table[1].extend([electronic[4], electronic[3]])

# [1 pt] Print the final shopping table
# [2 pts] Items from electronics list must appear in the order: electronic[4] followed by electronic[3]
print("\nShopping table:")
print(shopping_table)

## Another Solution for part 2:
# for i in range(0,2):
#     shopping_table[0].append(grocery[i])
# for j in range(4,2,-1):
#     shopping_table[1].append(electronic[j])
# print(shopping_table) 

# # Solution 3 for part 2:
# for item in electronic[-1::-1][:2]:
#     shopping_table[1].append(item)