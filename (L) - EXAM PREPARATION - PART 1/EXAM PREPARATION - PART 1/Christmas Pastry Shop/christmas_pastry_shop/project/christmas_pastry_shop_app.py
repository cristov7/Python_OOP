from typing import List
from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    VALID_TYPES_DELICACIES_DICT = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_TYPES_BOOTHS_DICT = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []          # contain all booths (objects) that are created
        self.delicacies: List[Delicacy] = []   # all delicacies (objects) that are created
        self.income: float = 0.0               # the total income of the pastry shop.

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> [Exception, str]:
        delicacy_objects_list = [delicacy_object for delicacy_object in self.delicacies
                                 if delicacy_object.name == name]
        if delicacy_objects_list:
            raise Exception(f"{name} already exists!")
        elif type_delicacy not in self.VALID_TYPES_DELICACIES_DICT.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        else:
            class_name = self.VALID_TYPES_DELICACIES_DICT[type_delicacy]
            delicacy_object = class_name(name, price)
            self.delicacies.append(delicacy_object)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> [Exception, str]:
        booth_objects_list = [booth_object for booth_object in self.booths
                              if booth_object.booth_number == booth_number]
        if booth_objects_list:
            raise Exception(f"Booth number {booth_number} already exists!")
        elif type_booth not in self.VALID_TYPES_BOOTHS_DICT.keys():
            raise Exception(f"{type_booth} is not a valid booth!")
        else:
            class_name = self.VALID_TYPES_BOOTHS_DICT[type_booth]
            booth_object = class_name(booth_number, capacity)
            self.booths.append(booth_object)
            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> [str, Exception]:
        booth_objects_list = [booth_object for booth_object in self.booths
                              if not booth_object.is_reserved and booth_object.capacity >= number_of_people]
        if booth_objects_list:
            booth_object = booth_objects_list[0]
            booth_object.reserve(number_of_people)
            booth_number = booth_object.booth_number
            return f"Booth {booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception("No available booth for {number of people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> [str, Exception]:
        booth_objects_list = [booth_object for booth_object in self.booths
                              if booth_object.booth_number == booth_number]
        if booth_objects_list:
            booth_object = booth_objects_list[0]
            delicacy_objects_list = [delicacy_object for delicacy_object in self.delicacies
                                     if delicacy_object.name == delicacy_name]
            if delicacy_objects_list:
                delicacy_object = delicacy_objects_list[0]
                booth_object.delicacy_orders.append(delicacy_object)
                return f"Booth {booth_number} ordered {delicacy_name}."
            else:
                raise Exception(f"No {delicacy_name} in the pastry shop!")
        else:
            raise Exception(f"Could not find booth {booth_number}!")

    def leave_booth(self, booth_number: int) -> str:
        booth_object = next(booth_object for booth_object in self.booths
                            if booth_object.booth_number == booth_number)
        price_per_reservation = booth_object.price_for_reservation
        price_of_all_orders = sum(delicacy.price for delicacy in booth_object.delicacy_orders)
        bill = price_per_reservation + price_of_all_orders
        self.income += bill
        booth_object.delicacy_orders.clear()
        booth_object.is_reserved = False
        booth_object.price_for_reservation = 0
        return f"Booth {booth_number}:" \
               f"\nBill: {bill:.2f}lv."

    def get_income(self) -> str:
        income = self.income
        return f"Income: {income:.2f}lv."
