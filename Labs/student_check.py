# Task 2
print("Task 2")
print("Original")
grocery = ["oranges","apples","mangos","blueberries","dragonfruit"]
electronic = ["iphones", "monitors", "computers","headphones","iPads"]
print(grocery)
print(electronic)

print("After sorted")
grocery.sort()
print(grocery)
electronic.sort()
print(electronic)

print("Original shopping table")
shopping_table = [grocery[:2],electronic[-1::-1][:2]]
print (shopping_table)