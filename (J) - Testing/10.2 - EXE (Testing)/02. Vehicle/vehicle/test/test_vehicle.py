import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(125.00, 250.00)

    def test_class_attribute_default_fuel_consumption_successfully(self):
        default_fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        expected_default_fuel_consumption = 1.25
        self.assertEqual(default_fuel_consumption, expected_default_fuel_consumption)

    def test___init___successfully(self):
        fuel = self.vehicle.fuel
        expected_fuel = 125.00
        self.assertEqual(fuel, expected_fuel)
        capacity = self.vehicle.capacity
        expected_capacity = 125.00
        self.assertEqual(capacity, expected_capacity)
        horse_power = self.vehicle.horse_power
        expected_horse_power = 250.00
        self.assertEqual(horse_power, expected_horse_power)
        fuel_consumption = self.vehicle.fuel_consumption
        expected_fuel_consumption = 1.25
        self.assertEqual(fuel_consumption, expected_fuel_consumption)

    def test_drive_successfully(self):
        self.vehicle.drive(100)
        fuel = self.vehicle.fuel
        expected_fuel = 0.00
        self.assertEqual(fuel, expected_fuel)

    def test_drive_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.vehicle.drive(101)
        result = str(content.exception)
        expected_result = "Not enough fuel"
        self.assertEqual(result, expected_result)

    def test_refuel_successfully(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(25)
        fuel = self.vehicle.fuel
        expected_fuel = 125.00
        self.assertEqual(fuel, expected_fuel)

    def test_refuel_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.vehicle.refuel(1)
        result = str(content.exception)
        expected_result = "Too much fuel"
        self.assertEqual(result, expected_result)

    def test___str___successfully(self):
        result = self.vehicle.__str__()
        expected_result = "The vehicle has 250.0 horse power with 125.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
