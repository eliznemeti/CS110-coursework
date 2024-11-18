## Name:
## ID:
## Save this file as yourname_cs110_lab4.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

## Temperature Conversions ##

## Exercise 1 - Fahrenheit to Celsius ##

# Ask the user to enter today's temperature in degrees Fahrenheit (make sure it's an integer).
temperature_F = int(input("What is the temperature today in Fahrenheit? "))

# Convert Fahrenheit input to Celsius using the formula C = (5/9) * (F - 32)
temperature_C = (5/9) * (temperature_F - 32)

# Display the conversion result using an f-string.
print(f"{temperature_F} in degrees F = {temperature_C} in degrees C")

## Exercise 2 - Highs & Lows ##

# Ask the user to enter the highest and lowest temperature in Fahrenheit for Thursday 9/25. (Make sure it's an integer.)
highest_F = int(input("Enter the highest temperature in Fahrenheit on 9/25: "))
lowest_F = int(input("Enter the lowest temperature in Fahrenheit on 9/25: "))

# Convert the inputs into Celsius
highest_C = (5/9) * (highest_F - 32)
lowest_C = (5/9) * (lowest_F - 32)

# Display the results in Celsius using an f-string. 
print(f"The highest temperature in Celsius is {highest_C} degrees.")
print(f"The lowest temperature in Celsius is {lowest_C} degrees.")

## Exercise 3 - Checking the temperature conversion ##

# Ask the user to re-enter the high and low Celsius values they obtained from Exercise 2 (make sure it's a float).
highest_C_re = float(input("Enter the highest temperature in Celsius: "))
lowest_C_re = float(input("Enter the lowest temperature in Celsius: "))

# Convert the Celsius temperatures back to Fahrenheit using the formula F = (9/5) * C + 32
highest_F_re = (9/5) * highest_C_re + 32
lowest_F_re = (9/5) * lowest_C_re + 32

# Calculate the differences between the original F. temperatures (Exercise 2 inputs) and the converted F. temperatures.
high_temp_difference = highest_F - highest_F_re
low_temp_difference = lowest_F - lowest_F_re

# Round the differences to two decimal places
high_temp_difference = round(high_temp_difference, 2)
low_temp_difference = round(low_temp_difference, 2)

# Display the differences using f-strings - they should be 0.0. 
print(f"The difference in the highest temperature is {high_temp_difference} degrees F.")
print(f"The difference in the lowest temperature is {low_temp_difference} degrees F.")