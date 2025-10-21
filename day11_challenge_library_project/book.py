class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You Borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"Sorry, '{self.title}' is out of stock.")

    def return_book(self):
        self.copies += 1
        print(f"Returned '{self.title}'. Copies available: {self.copies}")