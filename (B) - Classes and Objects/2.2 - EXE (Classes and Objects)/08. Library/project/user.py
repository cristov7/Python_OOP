from typing import List


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []   # [list of rented books]

    def info(self) -> str:
        rented_books = ", ".join(sorted(self.books))
        return rented_books

    def __str__(self) -> str:
        return f"{self.user_id}, {self.username}, {self.books}"
