from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand                                 # the brand of the vehicle
        self.model = model                                 # the model of the vehicle
        self.license_plate_number = license_plate_number   # the license plate number of the vehicle
        self.max_mileage = max_mileage                     # the maximum mileage of the vehicle
        self.battery_level: int = 100                      # the battery level of the vehicle (100 = 100%)
        self.is_damaged: bool = False                      # the damage status of the vehicle

    @property   # getter
    def brand(self) -> str:
        return self.__brand

    @brand.setter   # setter
    def brand(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Brand cannot be empty!")
        else:
            self.__brand = value

    @property   # getter
    def model(self) -> str:
        return self.__model

    @model.setter   # setter
    def model(self, value: str):
        if value == "" or value.isspace():
            raise ValueError("Model cannot be empty!")
        else:
            self.__model = value

    @property   # getter
    def license_plate_number(self) -> str:
        return self.__license_plate_number

    @license_plate_number.setter   # setter
    def license_plate_number(self, value: str):
        if value == "" or value.isspace():
            raise ValueError("License plate number is required!")
        else:
            self.__license_plate_number = value

    @abstractmethod                    # abstractmethod
    def drive(self, mileage: float):   # must be implemented
        pass

    def recharge(self) -> None:
        self.battery_level = 100

    def change_status(self) -> None:
        if self.is_damaged:
            self.is_damaged = False
        else:
            self.is_damaged = True

    def __str__(self) -> str:
        brand = self.brand
        model = self.model
        license_plate_number = self.license_plate_number
        battery_level = self.battery_level
        status = "Damaged" if self.is_damaged else "OK"
        return f"{brand} {model} License plate: {license_plate_number} Battery: {battery_level}% Status: {status}"
