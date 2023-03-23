# # Single Responsibility (SRP):


from typing import List


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self) -> str:
        title = self.title
        author = self.author
        pages = self.pages
        return f"Title: \"{title}\". Author: \"{author}\". Pages: {pages}."


class Library:
    def __init__(self):
        self.books: List[Book] = []   # [book_objects]

    def add_book(self, book: Book) -> str:   # book_object
        self.books.append(book)
        return "The book was added to the library."

    def find_book(self, title: str) -> str:
        book_objects_list = [book_object for book_object in self.books
                             if book_object.title == title]
        if book_objects_list:
            book_object = book_objects_list[0]
            book_info = book_object.__repr__()
            return f"Book found: {book_info}"
        else:
            return f"We don't have book with title: \"{title}\"."

    def __repr__(self) -> str:
        count_books = len(self.books)
        return f"The library has {count_books} count books."


# my_book = Book("Под игото", "Иван Вазов", 431)   # create an instance
# print(my_book)   # Title: "Под игото". Author: "Иван Вазов". Pages: 431.
#
# my_library = Library()   # create an instance
# print(my_library.add_book(my_book))   # The book was added to the library.
#
# print(my_library.find_book("Под игото"))   # Book found: Title: "Под игото". Author: "Иван Вазов". Pages: 431.
# print(my_library.find_book("Мечо Пух"))   # We don't have book with title: "Мечо Пух".
#
# print(my_library)   # The library has 1 count books.
