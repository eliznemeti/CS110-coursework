## Name:
## ID:
## Save this file as yourname_cs110_lab3.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# Optional: Try giving f-strings a go when making print statements for neater code. 

### Step 1 ###

# Prompt the user for 3 inputs and convert them to floats. Print the inputs. 

number_1 = float(input("Please enter a number: "))
print(f"You entered: {number_1}")

number_2 = float(input("Please enter a second number: "))
print(f"You entered: {number_2}")

number_3 = float(input("Please enter a third number: "))
print(f"You entered: {number_3}")

### Step 2 ###

# Increment each of the numbers by 10%. Print the incremented values.

incremented_num1 = number_1 * 1.10
incremented_num2 = number_2 * 1.10
incremented_num3 = number_3 * 1.10

print(f"{number_1} incremented by 10% is {incremented_num1}")
print(f"{number_2} incremented by 10% is {incremented_num2}")
print(f"{number_3} incremented by 10% is {incremented_num3}")

### Step 3 ###

# Calculate the average of the incremented numbers. 

average = (incremented_num1 + incremented_num2 + incremented_num3)/3
print(f"The average of {incremented_num1}, {incremented_num2}, and {incremented_num3} is {average}")
