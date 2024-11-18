# user_input = input("Enter a list of integers (comma-separated): ")
# numbers = list(map(int, user_input.split(','))) # Convert the comma-separated string to a list of integers using map
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Use filter and a lambda function to create a new list containing only even numbers

# print("Original list:", numbers)
# print("Even numbers:", even_numbers)

# #v2

# user_input = input("Enter a list of integers (comma-separated): ")
# numbers = list(map(int, user_input.split(',')))  

# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:  
#         even_numbers.append(num)  

# print("Original list:", numbers)  
# print("Even numbers:", even_numbers)  


print("Question 4")
# Write code below. Paste the input/output as a comment below. Make sure it runs without error. #

def count_character(string, char): # Base case: if the string is empty, return 0 (no characters to count)
    if not string:
        return 0
    count = 1 if string[0] == char else 0 # Check if the first character in the string matches the target character
    return count + count_character(string[1:], char) # Add the count (1 or 0) to the result of calling count_character on the rest of the string

string = input("Enter a string: ")
char = input("Enter a character to count: ")
print("Occurrences of character:", count_character(string, char))

# Input: string = "hello", char = "l"
# Output: Occurrences of character: 2