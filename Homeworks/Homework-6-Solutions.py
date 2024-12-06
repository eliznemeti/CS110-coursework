## Name:
## ID:
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# [20 pts] Question 1 - List Manipulation 
def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

user_input = input("Enter a list of integers (comma-separated): ")
numbers = [int(num.strip()) for num in user_input.split(",")]
odd_numbers = filter_odd_numbers(numbers)
print(f"Odd numbers: {odd_numbers}")


# [20 pts] Question 2: Weekday List Challenge 

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"The third day in the list is: {days_of_week[2]}")
# Change a Day
days_of_week[-1] = "FunDay"
print(f"Updated list after changing the last day: {days_of_week}")
# Add New Day
days_of_week.append("Holiday")
print(f"Updated list after adding 'Holiday': {days_of_week}")
# Remove a Day
days_of_week.remove("Wednesday")
print(f"Updated list after removing 'Wednesday': {days_of_week}")


# [20 pts] Question 3: Create a Simple Bank Account Class 

# Initialize the bank account with the account holder's name and an initial balance.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    #  Add the given amount to the balance.
    def deposit(self, amount):
        self.balance += amount

    # Subtract the given amount from the balance if funds are sufficient.
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    # Return the current balance.
    def get_balance(self):
        return self.balance

# Tasks
alice_account = BankAccount("Alice", 1000)
alice_account.deposit(500)
alice_account.withdraw(200)
print(f"Alice's final balance: {alice_account.get_balance()}")


# [20 pts] Question 4: Movie Class 

class Movie:
    """
    A class to represent a movie.
    """

    def __init__(self, title, director, year, rating):
        """
        Initialize the movie with title, director, release year, and rating.
        """
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def get_info(self):
        """
        Return a string with the movie's title, director, year, and rating.
        """
        return f"Title: {self.title}, Director: {self.director}, Year: {self.year}, Rating: {self.rating}"

    def update_rating(self, new_rating):
        """
        Update the rating of the movie if it's between 1 and 10.
        """
        if 1 <= new_rating <= 10:
            self.rating = new_rating
            print(f"Rating updated to {new_rating}.")
        else:
            print("Invalid rating. Please provide a value between 1 and 10.")


# Create a movie object for "Inception"
inception = Movie("Inception", "Christopher Nolan", 2010, 8.8)

# Print movie details using get_info()
print("Initial movie details:")
print(inception.get_info())

# Update the movie's rating to 9.2
inception.update_rating(9.2)

# Print updated movie details
print("\nUpdated movie details:")
print(inception.get_info())


# [20 pts] Question 5: The School Yearbook 

students = [
    ["Alice", 10, "Math"],
    ["Bob", 11, "History"],
    ["Charlie", 10, "Science"],
    ["Daisy", 12, "Math"],
    ["Eve", 11, "Art"]
]

# Task 1: Function to find the grade of a student by name
def find_grade(students, name):
    for student in students:
        if student[0] == name:
            return student[1]
    return None

print(f"Charlie's grade: {find_grade(students, 'Charlie')}")

# Task 2: Function to find students with a specific favorite subject
def find_favorite_subject(students, subject):
    matching_students = [student[0] for student in students if student[2] == subject]
    print(", ".join(matching_students))

print("Students who like 'Art':")
find_favorite_subject(students, "Art")

# Task 3: Calculates and returns the average grade of all students.
def average_grade(students):
    total_grade = sum(student[1] for student in students)
    return total_grade / len(students)

print(f"Average grade: {average_grade(students):.2f}")