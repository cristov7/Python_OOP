from project.user import User
from typing import List, Dict


class Library:
    def __init__(self):
        self.user_records: List[User] = []   # [users objects]
        self.books_available: Dict[str: List[str]] = {}   # {authors: [available books]}
        self.rented_books: Dict[str: Dict[str: int]] = {}   # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for username, books_dict in self.rented_books.items():
                if book_name in books_dict.keys():
                    days_to_return = books_dict[book_name]
                    return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self, author: str, book_name: str, user: User) -> [None, str]:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"
