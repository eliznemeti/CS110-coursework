# %% [markdown]
# Question 1: Division and Remainders
# 
# [10 pts] (Code) Write a program that asks the user to enter three integers. Calculate the sum of the first two numbers. Divide the sum by the third number using integer division (//), floating-point division (/), and find the remainder (%). Print the results.
# 
# [5 pts] (Written) Explain the difference between the //, / and % operators in Python. How would the program behave if the third number were zero?

# %%
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_3 = int(input('Enter the third number: '))

integer_division = (number_1 + number_2) // number_3
floating_point_division = (number_1 + number_2) / number_3
remainder = (number_1 + number_2) % number_3

print("Integer division:", integer_division)
print("Floating-point division (/):", floating_point_division)
print("Remainder:", remainder)

# %% [markdown]
# - Integer Division (//) returns the quotient, rounding down to the nearest integer.
# - Floating-Point Division (/) returns the quotient with decimal precision.
# - Remainder (%) returns the remainder of the division.
# - If the third number is zero, the program would raise a ZeroDivisionError because division by zero is mathematically undefined, and therefore Python cannot perform division for //, / or %. 

# %% [markdown]
# Question 2: Order of Operations
# 
# Consider the following expression: 
# result = 2 + 3 * 4 - 6 / 2
# 
# [8 pts] (Code + Written) Without running the code, determine the value of the result. Then explain the order of operations that Python follows to evaluate this expression. 
# 
# [7 pts] (Code + Written) How would adding parentheses change the result? 
# Show the output for the following: result = (2 + 3) * (4 - 6) / 2

# %%
result = 2 + 3 * 4 - 6 / 2
print(result)

result2 = (2 + 3) * (4 - 6) / 2
print(result2)


# %% [markdown]
# In the original expression Python will follow PEMDAS for operational precedence i.e. 3 * 4 first, 6 / 2 second, and then + and - resulting in 11.
# All exponents should be simplified first, followed by multiplication and division from left to right and, finally, addition and subtraction from left to right.
# 
# In the second expression the operations inside the parentheses will be evaluated first.

# %% [markdown]
# Question 3: Variable Tracking
# 
# Given the following variables:
# x = 5
# y = 10
# z = x + y
# x = z + 1
# y = x * z
# 
# [5 pts] (Code) What are the values of x, y, and z after the code runs? Print them. 
# 
# [5 pts] (Written) How does variable storage work and and how can losing track of variables cause bugs in more complex programs? 

# %%
x = 5
y = 10
z = x + y
x = z + 1
y = x * z
print(x, y, z)

# %% [markdown]
# Variables can only store one value at a time, so when assigning a new/updated value to a variable, the previous value is lost as it is overwritten. This means that the order in which assignments happen is critical to the final result.
# 
# Losing track of what each variable represents at different points in the program can lead to logical errors. If you lose track of which variable is being used where, it will be challenging to debug the code.

# %% [markdown]
# Question 4: Unary Operators
# 
# Given the following Python code:
# print(-x + y - z)
# 
# Modify the values of x, y, and z as follows:
# Set x = 10, y = -5, z = -8
# Set x = -10, y = -5, z = 0
# Set x = 0, y = 0, z = -8
# 
# [10 pts] (Code) For each combination, try predicting the output before running the code. Then compare your results after running. 
# 
# [5 pts] (Written) Explain the role of the unary operator and how it impacts the values of x, y, and z in these calculations. 

# %%
x = 10
y = -5
z = -8
print(-x + y - z)

x = -10
y = -5
z = 0
print(-x + y - z)

x = 0
y = 0
z = -8
print(-x + y - z)

# %% [markdown]
# The unary operator is used to negate the value of a variable and changes the sign of the number. When x is positive, -x will make it negative. When x is negative, -x will make it positive. When x is 0, the unary operator has no effect.

# %% [markdown]
# Question 5: Arithmetic Operations
# 
# [15 pts] (Code) First, prompt the user to input one integer and one floating-point number. 
# Then, perform the following operations:
# 
# Add the two numbers.
# Subtract the floating-point number from the integer.
# Multiply the integer by the floating-point number.
# Divide the floating-point number by the integer.
# Print the type and result for each operation as an f-string. 

# %%
int_num = int(input('Enter an integer: '))
float_num = float(input('Enter a floating-point number: '))

addition = int_num + float_num
subtraction = int_num - float_num
multiplication = int_num * float_num
division = float_num / int_num

print(f"Addition: {addition} Type: {type(addition)}") 
print(f"Subtraction: {subtraction} Type: {type(subtraction)}")
print(f"Multiplication: {multiplication} Type: {type(multiplication)}") 
print(f"Division: {division} Type: {type(division)}") 

# %% [markdown]
# Question 6: .format() Method with Single-Line Strings (Part 1)
# 
# [7 pts] (Code) Use the .format() method to print the message: "My name is <your name> and I am <your age> years old."
# 
# [3 pts] (Written) Name 3 reasons why using .format() method makes the code more readable compared to concatenating strings with +?
# 

# %%
name = "Elizabeth"
age = 25

answer = "My name is {} and I am {} years old.".format(name, age)
print(answer)

# %% [markdown]
# 3 reasons are the .format() method:
# - Automatically converts data types. Don't need to use str() for non-string types like numbers. 
# - Maintains structure of statement, reducing errors with spaces and type mismatches.
# - Handles multiple variables easily to avoid chains of + operators. 

# %% [markdown]
# Question 7: .format() Method with Multi-Line Strings (Part 2)
# 
# [15 pts] (Code) Write a Python program that asks the user two questions about why they are taking the course and what interests them most about Python. Use a multi-line string with triple quotes to display their answers in the following format:
# 
# My Course Reflection
# 
# I'm taking this course because: <user answer>
# 
# What excites me most about learning Python is: <user answer>
# 
# [5 pts] (Written) What benefits can you observe from using triple quotes instead of adding \n at every line?

# %% [markdown]
# 

# %%
why_input = input("Why are you taking this course? ")
interest_input = input("What interests you most about learning Python? ")

reflection = '''My Course Reflection

I'm taking this course because: {}

What excites me most about learning Python is: {}

'''.format(why_input, interest_input)

print(reflection)

# %% [markdown]
# - Triple quotes improve readability by keeping string layout exactly as it appears in the code.
# - Repeatedly adding \n can clutter the code and lead to formatting errors. 


