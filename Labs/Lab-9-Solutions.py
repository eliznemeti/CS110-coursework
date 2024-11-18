## Name:
## ID:
## Save this file as yourname_cs110_lab9.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# [10 pts] Task 1: Calculate Square and Cube using Lambda Functions

# (1 pt) Define the function calculate_square_and_cube that takes an integer n and returns a tuple containing the square and cube of n.
def calculate_square_and_cube(n) -> tuple:
    # (2 pts) Define a lambda function to calculate the square of n
    square = lambda x: x ** 2
    # (2 pts) Define a lambda function to calculate the cube of n
    cube = lambda x: x ** 3
    
    # (2 pts) Return a tuple containing both the square and the cube
    return (square(n), cube(n))

# (1 pt) Ask the user to input a number
user_input = int(input("Enter a number to calculate its square and cube: "))
# (2 pts) Call calculate_square_and_cube with the user input and store the result and print the result
result = calculate_square_and_cube(user_input)
print(f"The square of {user_input} is {result[0]} and the cube is {result[1]}.")


# [10 pts] Task 2: Recursive Sum of All Positive Integers Up to a Given Number

# (2 pts) Define the function sum_up_to that takes an integer n and returns the sum of all positive integers up to n using recursion.
def sum_up_to(n) -> int:
    # (2 pts) Base case: if n is less than or equal to 0, return 0
    if n <= 0:
        return 0
    # (3 pts) Recursive case: add n to the result of sum_up_to(n - 1)
    else:
        return n + sum_up_to(n - 1)

# (1 pt) Ask the user to input a positive integer
user_input_sum = int(input("Enter a positive integer to calculate the sum up to that number: "))
# (2 pts) Call sum_up_to with the user input and store the result and print the result
sum_result = sum_up_to(user_input_sum)
print(f"The sum of all positive integers up to {user_input_sum} is {sum_result}.")
