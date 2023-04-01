from abc import ABC, abstractmethod
from typing import List
from project.delicacies.delicacy import Delicacy


class Booth(ABC):   # AbstractBaseClass
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number            # the booth's number
        self.capacity = capacity                    # the booth's capacity
        self.delicacy_orders: List[Delicacy] = []   # contain delicacies (objects) that are ordered
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property   # getter
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter   # setter
    def capacity(self, value) -> [ValueError, None]:
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        else:
            self.__capacity = value

    @property   # getter
    @abstractmethod
    def get_price_per_person(self) -> float:
        pass

    def reserve(self, number_of_people: int) -> None:
        price_per_person = self.get_price_per_person
        total_price_for_reservation = price_per_person * number_of_people
        self.price_for_reservation = total_price_for_reservation
        self.is_reserved = True
