import unittest
from car_manager import Car


class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Mercedes-Benz", "A-Class Model", 10, 10_000)

    def test_make_successfully(self):
        result = self.car.make
        expected_result = "Mercedes-Benz"
        self.assertEqual(result, expected_result)

    def test_make_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.make = ""
        result = str(content.exception)
        expected_result = "Make cannot be null or empty!"
        self.assertEqual(result, expected_result)

    def test_model_successfully(self):
        result = self.car.model
        expected_result = "A-Class Model"
        self.assertEqual(result, expected_result)

    def test_model_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.model = ""
        result = str(content.exception)
        expected_result = "Model cannot be null or empty!"
        self.assertEqual(result, expected_result)

    def test_fuel_consumption_successfully(self):
        result = self.car.fuel_consumption
        expected_result = 10
        self.assertEqual(result, expected_result)

    def test_fuel_consumption_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.fuel_consumption = 0
        result = str(content.exception)
        expected_result = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(result, expected_result)

    def test_fuel_capacity_successfully(self):
        result = self.car.fuel_capacity
        expected_result = 10_000
        self.assertEqual(result, expected_result)

    def test_fuel_capacity_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.fuel_capacity = 0
        result = str(content.exception)
        expected_result = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(result, expected_result)

    def test_fuel_amount_successfully(self):
        result = self.car.fuel_amount
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_fuel_amount_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.fuel_amount = -10
        result = str(content.exception)
        expected_result = "Fuel amount cannot be negative!"
        self.assertEqual(result, expected_result)

    def test_refuel_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.refuel(0)
        result = str(content.exception)
        expected_result = "Fuel amount cannot be zero or negative!"
        self.assertEqual(result, expected_result)

    def test_refuel_successfully(self):
        self.car.refuel(100)
        result = self.car.fuel_amount
        expected_result = 100
        self.assertEqual(result, expected_result)
        self.car.refuel(100_000)
        result = self.car.fuel_amount
        expected_result = 10_000
        self.assertEqual(result, expected_result)

    def test_drive_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.car.drive(100)
        result = str(content.exception)
        expected_result = "You don't have enough fuel to drive!"
        self.assertEqual(result, expected_result)

    def test_drive_successfully(self):
        self.car.refuel(1_000)
        self.car.drive(10_000)
        result = self.car.fuel_amount
        expected_result = 0
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
