## Name:
## ID:
## Save this file as yourname_cs110_lab8.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# Task 1 - Multiplication Table (5 pts)

# (1 pt) Defining the function named multiplication_table with a parameter number
def multiplication_table(number):
    # (2 pts) Using a for loop to print the multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# (1 pt) Asking the user for input
user_number = int(input("Enter a number: "))
# (1 pt) Calling the function with the user’s input
multiplication_table(user_number)

# Task 2 - Even or Odd Game (15 pts)

# (3 pts) Defining the function is_even to take a parameter number
def is_even(number):
    # (2 pts) Returning True if number is even, False if odd
    return number % 2 == 0

# (3 pts) Defining the function play_even_odd_game
def play_even_odd_game():
    # (3 pts) Asking the user to enter a number between 1 and 50
    user_number = int(input("Enter a number between 1 and 50: "))
    # (2 pts) Using is_even to check if the number is even or odd and print the result
    if is_even(user_number):
        print("The number is even!")
    else:
        print("The number is odd!")

# (2 pts) Calling play_even_odd_game to start the game
play_even_odd_game()