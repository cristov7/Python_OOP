from typing import List
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[DesktopComputer or Laptop] = []
        self.profits: int = 0

    def configuration(self, computer_object: [DesktopComputer or Laptop], processor: str, ram: int) -> str:
        configuration = computer_object.configure_computer(processor, ram)
        self.warehouse.append(computer_object)
        return configuration

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> [str, ValueError]:
        if type_computer == "Desktop Computer":
            desktop_computer_object = DesktopComputer(manufacturer, model)
            configuration = self.configuration(desktop_computer_object, processor, ram)
            return configuration
        elif type_computer == "Laptop":
            laptop_object = Laptop(manufacturer, model)
            configuration = self.configuration(laptop_object, processor, ram)
            return configuration
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_memory: int) -> [str, Exception]:
        computer_objects_list = [computer_object for computer_object in self.warehouse
                                 if computer_object.price <= client_budget and
                                 computer_object.processor == wanted_processor and
                                 computer_object.ram >= wanted_memory]
        if computer_objects_list:
            computer_object = computer_objects_list[0]
            computer_price = computer_object.price
            profit = client_budget - computer_price
            self.profits += profit
            self.warehouse.remove(computer_object)
            computer = computer_object.__repr__()
            return f"{computer} sold for {client_budget}$."
        else:
            raise Exception("Sorry, we don't have a computer for you.")
