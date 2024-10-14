# ## Name:Kevin
# ## ID:kzha296
# """
# This code was my own work, it was written without consulting any sources
# outside of those approved by the instructor. 
# Initial: KZ
# """

# [5 pts] Task 1 # 

# [5 pts] Fix the Python program. It should use a while loop to count numbers from 1 to 10 and print them correctly. 

count = 0
while count < 10:
    count += 1
    print(count)
    
# [5 pts] Task 2 # 

# Modify the program to count from 1 to 50 but print only the numbers that are divisible by 5 below.

count = 0
while count <50:
    count += 1
    if count%5==0:
        print(count)


# [10 pts] Task 3 # 
# Write a Python program that repeatedly asks the user to input an integer until the user enters a negative integer. 
# The program should calculate the sum of (only) the positive numbers entered by the user.

# [1 pts] Create a variable to store the final sum below.

# [1 pts] Create a variable to store the user's input below

# [6 pts] Initiate the while loop to ask for user input and accumulate the sum below.

# [2 pts] Print the total sum, excluding the negative number that stops the loop below.
final = 0
done = False
while not done:
    entry = int(input("Please input an integer: "))
    if entry < 0:
        done= True
        print("This code is done")
    else:
        final=final+entry
        print("The total sum is:", final)

       