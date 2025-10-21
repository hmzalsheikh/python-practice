from book import Book
from user import User

book1 = Book("1984", "George Orwell", 3)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 2)

user1 = User("Hamzeh")
user2 = User("Lina")

user1.borrow_book(book1)
user1.borrow_book(book2)
user1.user_info()

user2.borrow_book(book1)
user2.user_info()

user1.return_book(book1)
user1.user_info()
