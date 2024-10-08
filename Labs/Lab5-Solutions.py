## Name:
## ID:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# [10 pts] Exercise 1: Booleans # 

# [2 pts] Cr


# Compare the variables using comparison operators <, !=, ==, >=.

# [2 pts] Check if x is less than y.
print("x < y:", x < y) 

# [2 pts] Check if x is not equal to y. 
print("x != y:", x != y) 

# [2 pts] Check if z is equal to 0. 
print("z == 0:", z == 0) 

# [2 pts] Check if x is greater than or equal to y. 
print("x >= y:", x >= y) 


# [10 pts] Exercise 2: Decision Programs # 

# [1 pts] Prompt the user to enter an integer.
number = int(input("Enter a number: "))

# [4 pts] Use if/else to check whether the integer is a positive or negative number, and print the result with a message.
if number > 0:
    print("The number is positive")
else:
    print("The number is negative or zero")
    
# [1 pts] Prompt the user to enter a new integer.
number2 = int(input("Enter a number: "))

# [4 pts] Use if/else to now check whether the integer is even or odd, and print the result with a message.
# Hint: use the remainder to verify if a number is odd/even.

if number2 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")