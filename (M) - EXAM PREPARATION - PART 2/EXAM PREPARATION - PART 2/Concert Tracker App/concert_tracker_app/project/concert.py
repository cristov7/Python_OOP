class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre                 # the genre of the concert
        self.audience = audience           # the number of people that will attend the concert
        self.ticket_price = ticket_price   # the price of ONE ticket
        self.expenses = expenses           # the price for all expenses for the concert
        self.place = place                 # the place where the concert will be performed

    @property   # getter
    def genre(self) -> str:
        return self.__genre

    @genre.setter   # setter
    def genre(self, value: str) -> [ValueError, None]:
        genre_list = ["Metal", "Rock", "Jazz"]
        if value not in genre_list:
            genre = value
            raise ValueError(f"Our group doesn't play {genre}!")
        else:
            self.__genre = value

    @property   # getter
    def audience(self) -> int:
        return self.__audience

    @audience.setter   # setter
    def audience(self, value: int) -> [ValueError, None]:
        if value < 1:
            raise ValueError("At least one person should attend the concert!")
        else:
            self.__audience = value

    @property   # getter
    def ticket_price(self) -> float:
        return self.__ticket_price

    @ticket_price.setter   # setter
    def ticket_price(self, value: float) -> [ValueError, None]:
        if value < 1.0:
            raise ValueError("Ticket price must be at least 1.00$!")
        else:
            self.__ticket_price = value

    @property   # getter
    def expenses(self) -> float:
        return self.__expenses

    @expenses.setter   # setter
    def expenses(self, value: float) -> [ValueError, None]:
        if value < 0.00:
            raise ValueError("Expenses cannot be a negative number!")
        else:
            self.__expenses = value

    @property   # getter
    def place(self) -> str:
        return self.__place

    @place.setter   # setter
    def place(self, value: str) -> [ValueError, None]:
        if len(value) < 2 or value.isspace():
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        else:
            self.__place = value

    def __str__(self) -> str:
        genre = self.genre
        place = self.place
        return f"{genre} concert at {place}."
