from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []   # [customer_objects]
        self.dvds: List[DVD] = []             # [dvd_objects]

    @staticmethod
    def dvd_capacity():
        dvd_capacity: int = 15
        return dvd_capacity

    @staticmethod
    def customer_capacity():
        customer_capacity: int = 10
        return customer_capacity

    def add_customer(self, customer: Customer) -> None:   # customer = customer_object
        max_capacity = self.customer_capacity()   # self.customer_capacity() == MovieWorld.customer_capacity()
        if len(self.customers) < max_capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:   # dvd = dvd_object
        max_capacity = self.dvd_capacity()   # self.dvd_capacity() == MovieWorld.dvd_capacity()
        if len(self.dvds) < max_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer_object = [customer_object for customer_object in self.customers
                           if customer_object.id == customer_id][0]
        dvd_object = [dvd_object for dvd_object in self.dvds
                      if dvd_object.id == dvd_id][0]
        customer_name = customer_object.name
        dvd_name = dvd_object.name
        age_restriction = dvd_object.age_restriction
        if dvd_object in customer_object.rented_dvds:
            return f"{customer_name} has already rented {dvd_name}"
        elif dvd_object.is_rented:
            return "DVD is already rented"
        elif customer_object.age < dvd_object.age_restriction:
            return f"{customer_name} should be at least {age_restriction} to rent this movie"
        else:
            customer_object.rented_dvds.append(dvd_object)
            dvd_object.is_rented = True
            return f"{customer_name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer_object = [customer_object for customer_object in self.customers
                           if customer_object.id == customer_id][0]
        dvd_object = [dvd_object for dvd_object in self.dvds
                      if dvd_object.id == dvd_id][0]
        customer_name = customer_object.name
        dvd_name = dvd_object.name
        if dvd_object in customer_object.rented_dvds:
            customer_object.rented_dvds.remove(dvd_object)
            dvd_object.is_rented = False
            return f"{customer_name} has successfully returned {dvd_name}"
        else:
            return f"{customer_name} does not have that DVD"

    def __repr__(self) -> str:
        customer_info = "\n".join([customer_object.__repr__()   # str(customer_object)
                                   for customer_object in self.customers])
        dvd_info = "\n".join([dvd_object.__repr__()   # str(dvd_object)
                              for dvd_object in self.dvds])
        return f"{customer_info}" \
               f"\n{dvd_info}"
