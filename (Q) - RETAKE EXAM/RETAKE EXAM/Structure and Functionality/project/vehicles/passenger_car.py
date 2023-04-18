from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    max_mileage: float = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.max_mileage)

    def drive(self, mileage: float) -> None:   # implemented method
        decrease_battery_level = round((mileage / self.max_mileage) * 100)
        self.battery_level -= decrease_battery_level
