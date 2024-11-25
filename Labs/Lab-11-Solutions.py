## Name:
## ID:
## Save this file as yourname_cs110_lab11.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

# Task 1 [15 pts]:
# Define a class Book to represent a book in a library with the following attributes and methods.

class Book:
    def __init__(self, title, author, copies):
        # Attributes: title (e.g., "Harry Potter"), author (e.g., "J.K. Rowling"), copies (e.g., 5).
        self.title = title
        self.author = author
        self.copies = copies
        self.initial_copies = copies  # To track original number of copies

    # Method: detail_book()
    # Prints the title, author, and the available number of copies.
    def detail_book(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")

    # Method: borrow_book()
    # Decrease the number of copies by 1 if copies are available.
    # Then, print the title of the book and the remaining number of copies.
    # If there are no remaining, print that the book is unavailable.
    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"{self.title}: Successfully Check-out: Remaining copies: {self.copies}")
        else:
            print(f"{self.title}: Cannot Check-out")

    # Method: return_book()
    # Increase the number of copies by 1.
    # Print the title of the book and the updated number of copies.
    # If the number of available copies meets the original number of copies, print that the book is fully returned.
    def return_book(self):
        if self.copies < self.initial_copies:
            self.copies += 1
            print(f"{self.title}: Successfully returned: Remaining copies: {self.copies}")
            if self.copies == self.initial_copies:
                print(f"{self.title}: Fully returned")
        else:
            print(f"{self.title}: No return needed, all copies are already available")

# Create two book objects:
# book1: Title "1984", Author "George Orwell", Copies 3.
book1 = Book("1984", "George Orwell", 3)

# book2: Title "The Hobbit", Author "J.R.R. Tolkien", Copies 2.
book2 = Book("The Hobbit", "J.R.R. Tolkien", 2)

# Perform the following operations:
# 1. Borrow a copy of book1.
book1.borrow_book()

# 2. Borrow a copy of book2.
book2.borrow_book()

# 3. Borrow a copy of book2 again.
book2.borrow_book()

# 4. Return a copy of book1 and borrow book2.
book1.return_book()
book2.borrow_book()

# 5. Return one copy of book2.
book2.return_book()

# 6. Find the current information about book1 and book2.
print("\nDetails of Books:")
book1.detail_book()
book2.detail_book()