from project.computer_types.computer import Computer
from typing import Dict


class Laptop(Computer):
    @property   # getter
    def type_of_computer(self) -> str:
        type_computer = "laptop"
        return type_computer

    @property   # getter
    def available_processors(self) -> Dict[str, int]:
        processors_with_prices_dict = {"AMD Ryzen 9 5950X": 900,
                                       "Intel Core i9-11900H": 1050,
                                       "Apple M1 Pro": 1200}
        return processors_with_prices_dict

    @property   # getter
    def max_ram_memory(self) -> int:
        max_ram = 64
        return max_ram
