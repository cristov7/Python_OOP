from typing import List
from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, customer_id: int):
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds: List[DVD] = []   # [dvd_objects]

    def __repr__(self) -> str:
        customer_id = self.id
        customer_name = self.name
        customer_age = self.age
        count_rented_dvds = len(self.rented_dvds)
        dvd_names = ", ".join(dvd_object.name
                              for dvd_object in self.rented_dvds)
        return f"{customer_id}: {customer_name} of age {customer_age} has {count_rented_dvds} rented DVD's ({dvd_names})"
