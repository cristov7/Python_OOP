from project.computer_types.computer import Computer
from typing import Dict


class DesktopComputer(Computer):
    @property   # getter
    def type_of_computer(self) -> str:
        type_computer = "desktop computer"
        return type_computer

    @property   # getter
    def available_processors(self) -> Dict[str, int]:
        processors_with_prices_dict = {"AMD Ryzen 7 5700G": 500,
                                       "Intel Core i5-12600K": 600,
                                       "Apple M1 Max": 1800}
        return processors_with_prices_dict

    @property   # getter
    def max_ram_memory(self) -> int:
        max_ram = 128
        return max_ram
