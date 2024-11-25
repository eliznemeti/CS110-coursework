from Ahmed_cs110_lab11_Book import Book

book1 = Book("1984", "George Orwell", 3)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 2)


book1.borrow_book()

book2.borrow_book()

book2.borrow_book()

book1.return_book()
book2.borrow_book()


book2.return_book()


book1.detail_book()
book2.detail_book()
