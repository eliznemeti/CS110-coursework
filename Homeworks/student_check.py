## Name: Senay Hailu
## ID: 2667131
## Initial below the statement:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: SH
"""

"""
Homework 3 Instructions

Make sure to test each condition once to ensure it works. 
For example, if a condition involves being divisible by 3 and 5, test numbers that satisfy one, both, and neither condition.
For each condition, paste one example of the input/output as a comment below.
Example comments for Question 1: 
    Input: 1 Output: No discount available. 
    Input: 3 Output: You get a 10% discount!
    Etc.

Tip: To rerun a question multiple times, comment out the rest of the code using cmd+/ (Mac) or ctrl+/ (Windows/Linux).
When done, uncomment to test the program again.

Your code must run successfully without syntax errors to receive full points.
Submit only your .py file. 
"""

"""
[20 pts] Question 1

A grocery store is offering discounts based on the number of items a customer purchases:
15% discount if the number of items is divisible by both 3 and 5.
10% discount if divisible by 3 only.
5% discount if divisible by 5 only.
No discount if not divisible by 3 or 5.
Write a program that asks the user to input the number of items purchased and prints which discount they get.
"""
print("Question 1")
items = int(input("Enter the number of items purchased: "))

# Input/Output Examples:
# Input: 1 Output: No discount available.
# Input: 3 Output: You get a 10% discount!
# Input: 5 Output: You get a 5% discount!
# Input: 15 Output: You get a 15% discount!

if items % 3 == 0 and items % 5 == 0:
    print("You get a 15% discount!")
elif items % 3 == 0:
    print("You get a 10% discount!")
elif items % 5 == 0:
    print("You get a 5% discount!")
else:
    print("No discount available.")

"""
[20 pts] Question 2

A movie theater is offering discounts based on customer age. A customer qualifies for the discount if:
- Their age is between 10 and 50 (inclusive).
- Or, their age is a multiple of 7 (7, 14, 21, etc.).
Write a program that asks the user to input their age and checks if they are eligible for the discount. 
If the customer qualifies, print "Discount eligibility: Yes". If they do not qualify, print "Discount eligibility: No".
"""
print("Question 2")
age = int(input("Enter your age: "))

# Input/Output Examples:
# Input: 25 Output: Discount eligibility: Yes
# Input: 14 Output: Discount eligibility: Yes
# Input: 55 Output: Discount eligibility: No

if 10 <= age <= 50 or age % 7 == 0:
    print("Discount eligibility: Yes")
else:
    print("Discount eligibility: No")

"""
[20 pts] Question 3

Write a program that asks the user for a year and then checks if it's a leap year.
The program should print "Leap year" if the year is divisible by 4 but not divisible by 100, unless it's also divisible by 400.
Otherwise, print "Not a leap year".
"""
print("Question 3")
year = int(input("Enter a year: "))

# Input/Output Examples:
# Input: 2024 Output: Leap year
# Input: 2000 Output: Leap year
# Input: 1900 Output: Not a leap year

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

"""
[20 pts] Question 4

Write a program that simulates a simple bank transaction approval system. 
The program should ask the user to input the amount they want to withdraw and respond according to the following conditions:
- If the amount is greater than $1000, print "Large transaction, approval required."
- If the amount is between $500 (inclusive) and $1000, print "Transaction in review."
- If the amount is less than $500:
    - If the amount is less than $10, do nothing for small transactions by using the pass statement.
    - Otherwise, print "Transaction approved."
"""
print("Question 4")
withdrawal = float(input("Enter the amount you want to withdraw: "))

# Input/Output Examples:
# Input: 1500 Output: Large transaction, approval required.
# Input: 700 Output: Transaction in review
# Input: 25 Output: Transaction approved
# Input: 5 Output: (Nothing happens due to the pass statement)

if withdrawal > 1000:
    print("Large transaction, approval required.")
elif 500 <= withdrawal <= 1000:
    print("Transaction in review")
elif withdrawal < 10:
    pass
else:
    print("Transaction approved")

"""
[20 pts] Question 5

Write a program that takes a user's grade as input and categorizes it as follows:
- If the grade is 90 or higher, print "A".
- If the grade is between 80 and 89, print "B".
- If the grade is between 70 and 79, print "C".
- If the grade is between 60 and 69, print "D".
- If the grade is below 60, print "F".
Hint: make sure to use each at least once: if, elif, and else.
Hint: make sure the number entered is within a valid range.
"""
print("Question 5")
grade = int(input("Enter your grade: "))

# Input/Output Examples:
# Input: 95 Output: A
# Input: 85 Output: B
# Input: 75 Output: C
# Input: 65 Output: D
# Input: 55 Output: F

if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")