from project.truck_driver import TruckDriver
import unittest


class TruckDriverTests(unittest.TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Alex", 1.25)

    def test___init___successfully(self):
        assert self.truck_driver.name == "Alex"
        assert isinstance(self.truck_driver.name, str)
        assert self.truck_driver.money_per_mile == 1.25
        assert isinstance(self.truck_driver.money_per_mile, float)
        assert self.truck_driver.available_cargos == {}
        assert isinstance(self.truck_driver.available_cargos, dict)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        assert self.truck_driver.miles == 0
        assert isinstance(self.truck_driver.miles, int)

    def test_earned_money_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.earned_money = 100
        assert self.truck_driver.earned_money == 100
        assert isinstance(self.truck_driver.earned_money, int)

    def test_earned_money_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.truck_driver.earned_money = -100
        assert str(content.exception) == "Alex went bankrupt."

    def test_add_cargo_offer_successfully(self):
        assert self.truck_driver.available_cargos == {}
        assert isinstance(self.truck_driver.available_cargos, dict)
        assert self.truck_driver.add_cargo_offer("Madrid", 100) == "Cargo for 100 to Madrid was added as an offer."
        assert self.truck_driver.available_cargos == {"Madrid": 100}
        assert isinstance(self.truck_driver.available_cargos, dict)
        assert isinstance(self.truck_driver.add_cargo_offer("Barcelona", 500), str)
        assert self.truck_driver.available_cargos == {"Madrid": 100, "Barcelona": 500}
        assert isinstance(self.truck_driver.available_cargos, dict)

    def test_add_cargo_offer_and_raise_exception(self):
        self.truck_driver.available_cargos["Madrid"] = 100
        assert self.truck_driver.available_cargos == {"Madrid": 100}
        with self.assertRaises(Exception) as content:
            self.truck_driver.add_cargo_offer("Madrid", 100)
        assert str(content.exception) == "Cargo offer is already added."
        assert self.truck_driver.available_cargos == {"Madrid": 100}
        assert isinstance(self.truck_driver.available_cargos, dict)

    def test_drive_best_cargo_offer_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        assert self.truck_driver.miles == 0
        assert isinstance(self.truck_driver.miles, int)
        self.truck_driver.available_cargos["Madrid"] = 100
        assert self.truck_driver.available_cargos == {"Madrid": 100}
        assert isinstance(self.truck_driver.available_cargos, dict)
        self.truck_driver.available_cargos["Barcelona"] = 500
        assert self.truck_driver.available_cargos == {"Madrid": 100, "Barcelona": 500}
        assert isinstance(self.truck_driver.available_cargos, dict)
        assert self.truck_driver.drive_best_cargo_offer() == "Alex is driving 500 to Barcelona."
        assert self.truck_driver.earned_money == 585.0
        assert isinstance(self.truck_driver.earned_money, float)
        assert self.truck_driver.miles == 500
        assert isinstance(self.truck_driver.miles, int)
        assert isinstance(self.truck_driver.drive_best_cargo_offer(), str)
        assert self.truck_driver.earned_money == 1170.0
        assert isinstance(self.truck_driver.earned_money, float)
        assert self.truck_driver.miles == 1000
        assert isinstance(self.truck_driver.miles, int)

    def test_drive_best_cargo_offer_and_except_value_error(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        assert self.truck_driver.miles == 0
        assert isinstance(self.truck_driver.miles, int)
        assert self.truck_driver.drive_best_cargo_offer() == "There are no offers available."
        assert isinstance(self.truck_driver.drive_best_cargo_offer(), str)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        assert self.truck_driver.miles == 0
        assert isinstance(self.truck_driver.miles, int)

    def test_check_for_activities_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.check_for_activities(100)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_check_for_activities_and_raise_value_error_during_eat(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.check_for_activities(250)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_check_for_activities_and_raise_value_error_during_sleep(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.check_for_activities(1000)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_check_for_activities_and_raise_value_error_during_pump_gas(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.check_for_activities(1500)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_check_for_activities_and_raise_value_error_during_repair_truck(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.check_for_activities(10000)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_eat_with_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.earned_money = 20
        assert self.truck_driver.earned_money == 20
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.eat(250)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_eat_without_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.eat(100)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_eat_and_raise_value_error(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.eat(250)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_sleep_with_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.earned_money = 45
        assert self.truck_driver.earned_money == 45
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.sleep(1000)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_sleep_without_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.sleep(100)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_sleep_and_raise_value_error(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.sleep(1000)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_pump_gas_with_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.earned_money = 500
        assert self.truck_driver.earned_money == 500
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.pump_gas(1500)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_pump_gas_without_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.pump_gas(100)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_pump_gas_and_raise_value_error(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.pump_gas(1500)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_repair_truck_with_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.earned_money = 7500
        assert self.truck_driver.earned_money == 7500
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.repair_truck(10000)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_repair_truck_without_change_successfully(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        self.truck_driver.repair_truck(100)
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test_repair_truck_and_raise_value_error(self):
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)
        with self.assertRaises(ValueError) as content:
            self.truck_driver.repair_truck(10000)
        assert str(content.exception) == "Alex went bankrupt."
        assert self.truck_driver.earned_money == 0
        assert isinstance(self.truck_driver.earned_money, int)

    def test___repr___successfully(self):
        assert self.truck_driver.name == "Alex"
        assert isinstance(self.truck_driver.name, str)
        assert self.truck_driver.miles == 0
        assert isinstance(self.truck_driver.miles, int)
        assert self.truck_driver.__repr__() == "Alex has 0 miles behind his back."
        self.truck_driver.name = "Bobby"
        assert isinstance(self.truck_driver.name, str)
        assert self.truck_driver.__repr__() == "Bobby has 0 miles behind his back."
        self.truck_driver.miles = 100
        assert isinstance(self.truck_driver.miles, int)
        assert self.truck_driver.__repr__() == "Bobby has 100 miles behind his back."
        assert isinstance(self.truck_driver.__repr__(), str)


if __name__ == '__main__':
    unittest.main()
