class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption
        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")
        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


import unittest


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
