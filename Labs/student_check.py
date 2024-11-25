
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.original_copies = copies  

    def detail_book(self):
        print(f"Title: {self.title}, Author: {self.author}, Available Copies: {self.copies}")

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"Borrowed: {self.title}. Remaining Copies: {self.copies}")
        else:
            print(f"{self.title} is unavailable.")

    def return_book(self):
        if self.copies < self.original_copies:
            self.copies += 1
            print(f"Returned: {self.title}. Updated Copies: {self.copies}")
            if self.copies == self.original_copies:
                print(f"{self.title} is fully returned.")
        else:
            print(f"All copies of {self.title} are already in the library.")
