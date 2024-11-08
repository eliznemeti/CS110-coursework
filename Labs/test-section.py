# Function to generate a string with alternating uppercase and lowercase letters
def string_generator(N):
    # Define a fixed pattern of letters to repeat
    pattern = "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    # Repeat the pattern enough times to get at least N characters and then truncate it
    return (pattern * ((N // len(pattern)) + 1))[:N]

# Main function to find and print the first M vowels
def find_and_print_vowels(N, M):
    generated_string = string_generator(N)
    print("Generated String:", generated_string)
    
    vowels = "AEIOUaeiou"
    found_vowels = []
    
    # Loop through characters in generated_string
    for char in generated_string:
        if char in vowels:
            found_vowels.append(char)
            # Stop if we've found M vowels
            if len(found_vowels) == M:
                print("First", M, "vowels:", ' '.join(found_vowels))
                return
    
    # If we didn't find M vowels, print the number of vowels found
    print("Total vowels found:", len(found_vowels))

# Example usage
find_and_print_vowels(10, 3)
