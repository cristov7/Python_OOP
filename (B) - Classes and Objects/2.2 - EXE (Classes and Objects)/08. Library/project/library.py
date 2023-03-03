from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []   # [user_objects]
        self.books_available: Dict[str, List[str]] = {}   # {author: [available_books]}
        self.rented_books: Dict[str, Dict[str, int]] = {}   # {username: {book_name: days_to_return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:   # user == user_object
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            if user.username in self.rented_books.keys():
                self.rented_books[user.username][book_name] = days_to_return
            else:   # elif user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {book_name: days_to_return}
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:   # elif book_name not in self.books_available[author]:
            for username, books_dict in self.rented_books.items():
                if book_name in books_dict.keys():
                    days_to_return = books_dict[book_name]
                    break
                else:   # elif book_name not in books_dict.keys():
                    continue
            return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:   # user == user_object
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:   # elif book_name not in user.books:
            username = user.username
            return f"{username} doesn't have this book in his/her records!"
