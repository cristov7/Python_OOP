from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity         # total quantity in liters
        self.fuel_consumption = fuel_consumption   # liters per 1 km

    @abstractmethod
    def drive(self, distance: int):   # distance in km
        pass

    @abstractmethod
    def refuel(self, fuel: int):      # amount of fuel
        pass


class Car(Vehicle):
    AIR_CONDITIONER: float = 0.9           # liters per 1 km

    def drive(self, distance: int) -> None:                              # distance in km
        fuel_consumption = self.fuel_consumption + Car.AIR_CONDITIONER   # total liters per 1 km
        total_fuel_consumption = distance * fuel_consumption             # total liters per distance
        if total_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel: int) -> None:   # amount of fuel
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER: float = 1.6   # liters per 1 km
    REFUEL_IN_PERCENTS: int = 95   # refuel 95% from amount

    def drive(self, distance: int) -> None:                                # distance in km
        fuel_consumption = self.fuel_consumption + Truck.AIR_CONDITIONER   # total liters per 1 km
        total_fuel_consumption = distance * fuel_consumption               # total liters per distance
        if total_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel: int) -> None:                     # amount of fuel
        total_fuel = fuel * Truck.REFUEL_IN_PERCENTS / 100   # total amount of fuel
        self.fuel_quantity += total_fuel
