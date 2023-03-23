# # Dependency Inversion (DIP):


from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class IFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class IPrinter(ABC):
    @abstractmethod
    def get_book(self, book: Book) -> str:
        pass


class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def get_book(self, book: Book) -> str:
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book


# my_book = Book("This is content of the book.")
# my_formatter = Formatter()
# my_printer = Printer(my_formatter)
#
# my_formatted_book = my_printer.get_book(my_book)
# print(my_formatted_book)   # This is content of the book.
