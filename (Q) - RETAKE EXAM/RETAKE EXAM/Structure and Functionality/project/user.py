class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name                           # the user’s first name
        self.last_name = last_name                             # the user’s last name
        self.driving_license_number = driving_license_number   # the user’s driving license number
        self.rating: float = 0                                 # the user’s rating
        self.is_blocked: bool = False                          # the user’s blocked status

    @property   # getter
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter   # setter
    def first_name(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("First name cannot be empty!")
        else:
            self.__first_name = value

    @property   # getter
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter   # setter
    def last_name(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Last name cannot be empty!")
        else:
            self.__last_name = value

    @property   # getter
    def driving_license_number(self) -> str:
        return self.__driving_license_number

    @driving_license_number.setter   # setter
    def driving_license_number(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Driving license number is required!")
        else:
            self.__driving_license_number = value

    @property   # getter
    def rating(self) -> float:
        return self.__rating

    @rating.setter   # setter
    def rating(self, value: float) -> [ValueError, None]:
        if value < 0:
            raise ValueError("Users rating cannot be negative!")
        else:
            self.__rating = value

    def increase_rating(self) -> None:
        current_rating = self.rating
        increase_rating = 0.5
        if current_rating + increase_rating > 10:
            self.rating = 10
        else:
            self.rating += increase_rating

    def decrease_rating(self) -> None:
        current_rating = self.rating
        decrease_rating = 2.0
        if current_rating - decrease_rating < 0:
            self.rating = 0
            self.is_blocked = True
        else:
            self.rating -= decrease_rating

    def __str__(self) -> str:
        first_name = self.first_name
        last_name = self.last_name
        driving_license_number = self.driving_license_number
        rating = self.rating
        return f"{first_name} {last_name} Driving license: {driving_license_number} Rating: {rating}"
