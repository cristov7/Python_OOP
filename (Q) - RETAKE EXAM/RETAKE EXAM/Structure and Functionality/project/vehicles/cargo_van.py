from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    max_mileage: float = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.max_mileage)

    def drive(self, mileage: float) -> None:   # implemented method
        decrease_battery_level = round((mileage / self.max_mileage) * 100)
        additional_decrease_battery_level = 5
        self.battery_level -= (decrease_battery_level + additional_decrease_battery_level)
