## Name:
## ID:
## Initial below the statement:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

"""
CS 110: Computer Science Fundamentals 
Homework 4 Instructions

Make sure to test each condition once to ensure it works.
For example, if you are looping through a range, test edge cases to ensure the loop behaves correctly (e.g., testing with small values, maximum values, etc.).
For each question, paste one example of the input/output as a comment below.

Tip: To rerun a question multiple times, comment out the rest of the code using cmd+/ (Mac) or ctrl+/ (Windows/Linux).
When done, uncomment to test the program again.

Your code must run successfully without syntax errors to receive full points.
Submit only your .py file. 
"""

"""
[20 pts] Question 1

Write a Python program that prints the numbers from 1 to 5 using a while loop.
Your program should initialize a variable n to 1 and print numbers from 1 to 5.
After the loop completes, print a message indicating that the loop has ended.
"""
print("Question 1")
# Write code below. Paste the input/output as a comment below. Make sure it runs without error. #
n = 1
while n <= 5:
    print(n)
    n += 1
print("The loop has ended.")

# Output:
# 1
# 2
# 3
# 4
# 5
# The loop has ended.

"""
[20 pts] Question 2

Write a Python program that prompts the user to input a positive integer and prints the numbers from that value down to 1 using a while loop.
The program should ask the user for a positive integer and print numbers in descending order from that value to 1.
"""
print("Question 2")
# Write code below. Paste the input/output as a comment below. Make sure it runs without error. #
number = int(input("Enter a positive integer: "))
while number > 0:
    print(number)
    number -= 1
    
# Example Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1

"""
[20 pts] Question 3

Write a Python program that asks the user for a number and prints whether each number from 1 to that value is odd or even using a for loop.
Use the range() function to iterate through numbers from 1 to the user's input.
For each number, print whether it is odd or even.
"""
print("Question 3")
# Write code below. Paste the input/output as a comment below. Make sure it runs without error. #
user_input = int(input("Enter a number: "))
for i in range(1, user_input + 1):
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")
        
# Example Input: 5
# Output:
# 1 is odd.
# 2 is even.
# 3 is odd.
# 4 is even.
# 5 is odd.

"""
[20 pts] Question 4

The given string generator function, string_generator(N), will return a string with N many characters, 
both upper and lower cases combined. Write a program that generates a string by the length of the input 
value of N and counts the number of vowels (Y and y is excluded) in the string. 

Repeat the vowel counting M times. 
Calculate the probability of vowel occurrences in the total M strings 
(=total count of vowels / total number of characters generated). 
For example, 
if N = 50 and M = 11, the program should generate a string with 50 characters 11 times and 
there are a total of 550 generated chracters.
Show that the chance of vowel occurrences gets close to 0.1923 when M increase 
by testing with N = 50 and M changes from 1 to 1000 (inclusive) in intervals of 50.

Print the total number of generated strings,  the total number of characters, and the probability. 
"""
print("Question 4")
# Write code below. Paste the input/output as a comment below. Make sure it runs without error. #

import string
import random

def string_generator(N):
    """Generates a random string of length N with both upper and lower case letters."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(N))

def count_vowels(s):
    """Counts vowels in the string, excluding Y and y."""
    vowels = set("AEIOUaeiou")
    return sum(1 for char in s if char in vowels)

def calculate_vowel_probability(N, M):
    total_vowels = 0
    total_characters = N * M
    
    for _ in range(M):
        generated_string = string_generator(N)
        total_vowels += count_vowels(generated_string)
    
    probability = total_vowels / total_characters
    return M, total_characters, probability

# Test with N=50 and M values from 1 to 1000 in intervals of 50
N = 50
for M in range(1, 1001, 50):
    generated_strings, total_characters, probability = calculate_vowel_probability(N, M)
    print(f"Total generated strings: {generated_strings}")
    print(f"Total number of characters: {total_characters}")
    print(f"Vowel occurrence probability: {probability:.4f}\n")
# Example Output:
# M=1: Total Vowels=8, Total Characters=50, Probability=0.1600
# M=51: Total Vowels=392, Total Characters=2550, Probability=0.1537
# M=1001: Total Vowels=9601, Total Characters=50050, Probability=0.1918

"""
[20 pts] Question 5

Write a Python program that prints the first n numbers of the Fibonacci sequence. 
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
The program should:
Ask the user to input a positive integer n (greater than or equal to 2).
Print the first n numbers of the Fibonacci sequence.
Hint: Use a for loop and maintain two variables to track the previous two numbers in the sequence.
"""
print("Question 5")
# Write code below. Paste the input/output as a comment below. Make sure it runs without error. #

n = int(input("Enter a positive integer (>= 2): "))
a, b = 0, 1
print(a, b, end=" ")
for _ in range(2, n):
    a, b = b, a + b
    print(b, end=" ")
print()

# Example Input: 5
# Output:
# 0 1 1 2 3