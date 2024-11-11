import random
import string

# Prompt for user input
N = int(input('Please enter a positive number: '))

# Function to generate a random string of length N
def string_generator(N):
    chars = string.ascii_uppercase + string.ascii_lowercase
    x = ''.join(random.choice(chars) for _ in range(N))
    return x

# Function to count vowels in a given string
def count_vowels(x):
    vowels = "AEIOUaeiou"
    return sum(1 for char in x if char in vowels)

# Function to calculate the probability of vowels
def calc_probab_of_vowel(N, M, interval):
    total_vowels = 0
    total_characters = N * M  # Total characters generated across all strings

    # Generate strings M times and count total vowels
    for _ in range(M):
        generated_string = string_generator(N)
        total_vowels += count_vowels(generated_string)

    # Calculate the probability
    prob = total_vowels / total_characters
    print(f"Probability of vowel occurrences: {prob:.4f}")
    return prob

# Example usage
calc_probab_of_vowel(N=50, M=1000, interval=50)
