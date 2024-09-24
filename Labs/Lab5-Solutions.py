## Name:
## ID:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# Create a function named 'reorder' that:
# 1) takes a string (input) in the format "lastname, firstname"
# 2) reorders a name from "lastname, firstname" format to "firstname lastname"
# 3) returns the string in the format "firstname lastname" with exactly one space

# Prompt the user for input for the name in the format "lastname, firstname"
name = input("Enter a name in the format 'lastname, firstname': ")

# Define the function
def reorder(name):
    lastname, firstname = name.split(", ") # Split the string at the comma and strip any extra spaces
    return f"{firstname} {lastname}" # Return the reordered name


# Call the function and print the output
print(reorder(name))
