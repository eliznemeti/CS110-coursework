## Name: Linda Azcarate Estrada
## ID: 2671386
## Initial below the statement:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# [10 pts] Question 1.  

# Write a program to print 10, 10.0, “10.0”.  
(a, b, c) = (10, 10.0, "10.0")
print(a, b, c)
# Find the type of each and explain the differences between 10, 10.0, and “10.0”. (code + written)
print(type(10))
print(type(10.0))
print(type("10.0"))
# Explanation: Int is for integers, float is for decimals and string is for letters

# [15 pts] Question 2. 

# Print the expression that adds two integers, 5 and 10. 
(c, d) = (5, 10)
print(c+d)
# Concatenate two strings, '5' and '10', and print the result. 
e = str(5)
f = str(10)
x = e+f
print(x)
# What is the difference between adding integers and concatenating strings? (written)
# Explanation: When we add integers it is the sum of the numbers but when we concatenate strings is to write them together

# [20 pts] Question 3.  

# Verify if Python will accept the code below. Explain why or why not.  
                # ‘100’ + 50 
# Make changes if needed and print the result. 
# Explanation: Phyton does not accept the code because one is a string and the other is an integer, they should be in the same type
g = int(str(100))
h = 50
y = g+h
print(y)
# Let x be ‘2’ and y be 100. 
(x, y) = (2, 100)
# Find the product of x and y and let the product have a variable name z. 
z = x*y
print(z)
# Concatenate it with ' is the same as 2x100.'. 
# Make changes if needed and print the result. 
i = ' is the same as 2x100.'
j = str(int(z))
k = j+i
print(k)
# Explain what happens if you try to convert the string 'hello' to an integer? (code + written)
#l = 'hello'
#m = int(str(l))
#print(m)
# Explanation: We get an error because integers are for numbers and 'hello' is not a number.

# [10 pts] Question 4. 

# Assign the value 25 to a variable called age. 
# Print the value of age. 
age = 25
print(age)

# Reassign age to a new value of 'twenty-five' (a string). 
age = 'twenty-five'

# Print the new value and check its type. 
print(age)
print(type(age))

# How does Python handle changes in variable types? (written)
#Explanation: Phyton recognizes three types of variables: integer (numbers), float (decimals) and string (letters).


# [15 pts] Question 5.

# Assign values to three variables a, b, and c in a single line using tuple assignment. 
(a, b, c) = (1, 2, 3)

# Print them in a single line, separated by commas. 
print(a,",", b,",", c)

# Print them with custom formatting using the format() method, where a is left-aligned in 10 spaces and b and c are right-aligned in 10 spaces.
print("{:<10} {:>10} {:>10}".format(a, b, c))

# How does tuple assignment work? (written)
#Explanation: It equalizes values on the left with those on the right, respecting the order in which these values are found.


# [15 pts] Question 6.

# Prompt the user to enter their name. Use \n to print a greeting on two lines. 
d = input("Please, put your name: ")
print ("Hello, [d]!\nWelcome to this program!")

# Additionally, use \t to print their name indented with a tab. 
print("Hello,  my name is:\n", "\t", d)
# How do control codes like \n and \t change the output formatting? (written)
#Explanation: \n puts the text on another line but \t creates a new tab for other text


# [15 pts] Question 7.

# Write a program that asks the user to input two floating-point numbers.  
float1 = float(input("Insert the number for float1: "))
float2 = float(input("Insert the number for float2: "))
# Apply addition, subtraction, multiplication, and division between two numbers.  
addition = float1 + float2
subtraction = float1 - float2
multiplication = float1 * float2
if float2 != 0:
   division = float1 / float2
else:
   division = "This can not be divided by 0"

# Print the result of each operation after rounding it up to the thousandth place.  
addition = round(float1 + float2, 3)
subtraction = round(float1 - float2, 3)
multiplication = round(float1 * float2, 3)
if float2 != 0:
    division = round(float1 / float2, 3)
else:
    division = "This cannot be divided by 0"
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# What happens if the user enters integers instead of decimal numbers? (code + written)
#Phyton will run it anyways but as a float with .0
