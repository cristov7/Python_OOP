from abc import ABC, abstractmethod
from typing import Dict
from math import log2, ceil, floor


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: [str or None] = None
        self.ram: [int or None] = None
        self.price: int = 0

    @property   # getter
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter   # setter
    def manufacturer(self, value) -> [ValueError, None]:
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self.__manufacturer = value

    @property   # getter
    def model(self) -> str:
        return self.__model

    @model.setter   # setter
    def model(self, value) -> [ValueError, None]:
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        else:
            self.__model = value

    @property   # getter
    @abstractmethod
    def type_of_computer(self) -> str:
        pass

    @property   # getter
    @abstractmethod
    def available_processors(self) -> Dict[str, int]:
        pass

    @property   # getter
    @abstractmethod
    def max_ram_memory(self) -> int:
        pass

    @staticmethod
    def ram_validator(ram: int) -> bool:
        number = log2(ram)
        return ceil(number) == floor(number)

    def set_parts(self, processor: str, ram: int) -> None:
        self.processor = processor
        self.ram = ram
        self.price = self.available_processors[processor]
        extras_price = int(log2(ram)) * 100
        self.price += extras_price

    def configure_computer(self, processor: str, ram: int) -> [ValueError, str]:
        type_of_technique = self.type_of_computer
        manufacturer_name = self.manufacturer
        model_name = self.model
        validator_of_ram = self.ram_validator(ram)
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {type_of_technique} {manufacturer_name} {model_name}!")
        elif not validator_of_ram or ram > self.max_ram_memory:
            raise ValueError(f"{ram}GB RAM is not compatible with {type_of_technique} {manufacturer_name} {model_name}!")
        else:
            self.set_parts(processor, ram)
            price = self.price
            return f"Created {manufacturer_name} {model_name} with {processor} and {ram}GB RAM for {price}$."

    def __repr__(self) -> str:
        manufacturer = self.manufacturer
        model = self.model
        processor = self.processor
        ram = self.ram
        return f"{manufacturer} {model} with {processor} and {ram}GB RAM"
