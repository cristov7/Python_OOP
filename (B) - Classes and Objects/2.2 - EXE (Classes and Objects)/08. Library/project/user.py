from typing import List


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []   # [list of rented books]

    def info(self) -> str:
        sorted_rented_books = ", ".join(sorted(self.books))
        return sorted_rented_books

    def __str__(self) -> str:
        user_id = self.user_id
        username = self.username
        list_of_rented_books = self.books
        return f"{user_id}, {username}, {list_of_rented_books}"
