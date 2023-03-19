from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity         # total quantity
        self.fuel_consumption = fuel_consumption   # consumption liters per 1 km

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AIR_CONDITION: float = 0.9   # consumption liters per 1 km

    # def __init__(self, fuel_quantity: int, fuel_consumption: int):
    #     super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int) -> None:   # km
        fuel_consumption = self.fuel_consumption + Car.AIR_CONDITION   # consumption liters per 1 km
        total_consumption = fuel_consumption * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITION: float = 1.6   # consumption liters per 1 km
    REFUEL_PERCENT: int = 95     # refuel percent (95% from 100%)

    # def __init__(self, fuel_quantity: int, fuel_consumption: int):
    #     super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int) -> None:   # km
        fuel_consumption = self.fuel_consumption + Truck.AIR_CONDITION   # consumption liters per 1 km
        total_consumption = fuel_consumption * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel: int) -> None:
        total_fuel = fuel * Truck.REFUEL_PERCENT / 100
        self.fuel_quantity += total_fuel
