
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
# Write code below. Paste the input/output of each condition as a comment below. Make sure it runs without error. #

g = int(input("Please enter your integer grade: "))
if g>=90:
    print("A")
elif g>=80 and g<=89:
    print("B")
elif g>=70 and g<=79:
    print("C")
elif g>=60 and g<=69:
    print("D")
else:
    print("F")