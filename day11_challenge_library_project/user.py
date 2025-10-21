from book import Book

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow()
        if book.copies >= 0:
            self.borrowed_books.append(book.title)

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            print(f"{self.name} returned the book '{book.title}' successfuly!")
        else:
            print(f"{self.name} didn't borrow '{book.title}'")

    def user_info(self):
        print(f"User: {self.name}")
        if self.borrowed_books:
            print("Borrowed books:")
            for title in self.borrowed_books:
                print(f" - {title}")
        else:
            print("No books borrowed yet.")