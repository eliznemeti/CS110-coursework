# Question 7: .format() Method with Multi-Line Strings (Part 2)

# [15 pts] (Code)
# Write a Python program that asks user input for two questions:
# Why they are taking the course?
# What interests them most about Python?
print("Why are you taking the course?")
reason = input()

print("What interests you most about Python?")
interest = input()

# Use a multi-line string with triple quotes to display their answers in the following format:
# My Course Reflection
# I'm taking this course because: <user answer>
# What excites me most about learning Python is: <user answer>
print("""
My Course Reflection
I'm taking this course because: {0}
What excites me most about learning Python is: {1}
""".format(reason, interest))

# [5 pts] (Written)
# What benefits can you observe from using triple quotes instead of adding \n at every line?
# You can visualize how it will print while coding and you only have to add quotes once,
# not add \n each time.
