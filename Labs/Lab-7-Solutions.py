## Name:
## ID:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

'''
[5 pts] Task 1
Create a multiplication table for a user-input number.

- Ask the user to input a number. (Explicitly ask a question and use a colon ":"). 
- Use a while loop to print the multiplication table for that number from 1-10.
Example Output:
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
'''
# Write code below #

num = int(input("Enter a number: "))
count = 1

while count <= 10:
    print(f"{num} x {count} = {num * count}")
    count += 1

'''
[15 pts] Task 2
Give this a go with your neighbor in class!
Player 1 will input a secret number. Player 2 will guess it.

1. Create a variable to store Player 1's secret number.
2. Prompt Player 1 to enter a number from 1-20 only. (Explicitly ask a question and use a colon ":").
3. Clear the screen for Player 2 by printing 20 new lines using "\n".
4. Have Player 2 guess the secret number.
   - Use a while loop to keep Player 2 guessing until they get the number correct.
   - If Player 2 guesses lower than the number, print "Too low".
   - If Player 2 guesses higher than the number, print "Too high".
   - If Player 2 guesses the correct number, print "Congrats you guessed it!"
   - End the game.
'''
# Write code below #

secret_number = int(input("Player 1, enter a secret number between 1 and 20: "))
print("\n" * 20)

guess = 0
while guess != secret_number:
    guess = int(input("Player 2, guess the number between 1 and 20: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")