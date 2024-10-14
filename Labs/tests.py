# Question 6: .format() Method with Single-Line Strings (Part 1)
# [7 pts] (Code) 
# Use the .format() method to print the message: 
# "My name is <your name> and I am <your age> years old."

# [3 pts] (Written) Name up to 3 reasons why using .format() method makes the code more readable compared to concatenating strings with +?

your_name="Kevin"
your_age="18"
print("My name is {} and I am {} years old.".format(your_name,your_age))
print("By using the format function, I'm able to put make my long sentences much shorter, avoiding the usage of back slashes like I have previously used\
      It's also better because I don't have to enter the same name or number again and can just put in a variable instead.\
      If I want to change a the name that appears multiple times then I can do that once and all of the names in the string will change, making it much easier than having to change each name. ")


# Question 7: .format() Method with Multi-Line Strings (Part 2)

# [15 pts] (Code) 
# Write a Python program that asks user input for two questions:
# Why they are taking the course?
# What interests them most about Python? 
# Use a multi-line string with triple quotes to display their answers in the following format:

# My Course Reflection
# I'm taking this course because: <user answer>
# What excites me most about learning Python is: <user answer>

# [5 pts] (Written) What benefits can you observe from using triple quotes instead of adding \n at every line?
x=input("Why are you taking this course:")
y=input("What interests you most about python:")
print(f"""My Course reflection
I'm taking this course because {x}
What excites me most about learning Python is {y}""")
print("It's more convenient because having to add commas and \n everytime is tedious and prone to error")
