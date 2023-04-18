from project.robot import Robot
import unittest


class RobotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot("123", "Education", 1000, 99.99)
        self.robot_2 = Robot("456", "Humanoids", 10_000, 5000.00)

    def test_class_attributes_successfully(self):
        assert self.robot.ALLOWED_CATEGORIES == ['Military', 'Education', 'Entertainment', 'Humanoids']
        assert isinstance(self.robot.ALLOWED_CATEGORIES, list)
        assert self.robot.PRICE_INCREMENT == 1.5
        assert isinstance(self.robot.PRICE_INCREMENT, float)

    def test___init___successfully(self):
        assert self.robot.robot_id == "123"
        assert isinstance(self.robot.robot_id, str)
        assert self.robot.category == "Education"
        assert isinstance(self.robot.category, str)
        assert self.robot.available_capacity == 1000
        assert isinstance(self.robot.available_capacity, int)
        assert self.robot.price == 99.99
        assert isinstance(self.robot.price, float)
        assert self.robot.hardware_upgrades == []
        assert isinstance(self.robot.hardware_upgrades, list)
        assert self.robot.software_updates == []
        assert isinstance(self.robot.software_updates, list)

    def test_category_successfully(self):
        assert self.robot.category == "Education"
        self.robot.category = "Humanoids"
        assert self.robot.category == "Humanoids"
        assert isinstance(self.robot.category, str)

    def test_category_and_raise_value_error(self):
        assert self.robot.category == "Education"
        with self.assertRaises(ValueError) as content:
            self.robot.category = "Battlebot"
        assert str(content.exception) == "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        assert self.robot.category == "Education"

    def test_price_successfully(self):
        assert self.robot.price == 99.99
        self.robot.price = 999.99
        assert self.robot.price == 999.99
        assert isinstance(self.robot.price, float)

    def test_price_and_raise_value_error(self):
        assert self.robot.price == 99.99
        with self.assertRaises(ValueError) as content:
            self.robot.price = -0.99
        assert str(content.exception) == "Price cannot be negative!"
        assert self.robot.price == 99.99

    def test_upgrade_and_return_robot_was_not_upgraded(self):
        assert self.robot.hardware_upgrades == []
        self.robot.hardware_upgrades.append("monitor")
        assert self.robot.hardware_upgrades == ["monitor"]
        assert isinstance(self.robot.hardware_upgrades, list)
        assert self.robot.upgrade("monitor", 499.99) == "Robot 123 was not upgraded."
        assert self.robot.hardware_upgrades == ["monitor"]
        assert isinstance(self.robot.hardware_upgrades, list)
        assert isinstance(self.robot.upgrade("monitor", 499.99), str)

    def test_upgrade_and_return_robot_was_upgraded(self):
        assert self.robot.hardware_upgrades == []
        assert self.robot.upgrade("monitor", 499.99) == 'Robot 123 was upgraded with monitor.'
        assert self.robot.hardware_upgrades == ["monitor"]
        assert isinstance(self.robot.hardware_upgrades, list)
        assert self.robot.price == 849.975
        assert isinstance(self.robot.price, float)
        assert isinstance(self.robot.upgrade("hard drive", 399.99), str)

    def test_update_and_return_robot_was_not_updated(self):
        assert self.robot.software_updates == []
        self.robot.software_updates.append(10.0)
        assert self.robot.software_updates == [10.0]
        assert isinstance(self.robot.software_updates, list)
        assert self.robot.update(9.7, 100) == "Robot 123 was not updated."
        assert self.robot.software_updates == [10.0]
        assert isinstance(self.robot.software_updates, list)
        assert self.robot.update(10.0, 100) == "Robot 123 was not updated."
        assert self.robot.software_updates == [10.0]
        assert isinstance(self.robot.software_updates, list)
        assert self.robot.update(100.0, 1001) == "Robot 123 was not updated."
        assert self.robot.software_updates == [10.0]
        assert isinstance(self.robot.software_updates, list)
        assert isinstance(self.robot.update(100.0, 1001), str)

    def test_update_and_return_robot_was_updated(self):
        assert self.robot.software_updates == []
        assert self.robot.update(10.0, 100) == 'Robot 123 was updated to version 10.0.'
        assert self.robot.software_updates == [10.0]
        assert isinstance(self.robot.software_updates, list)
        assert self.robot.available_capacity == 900
        assert isinstance(self.robot.available_capacity, int)
        assert isinstance(self.robot.update(100.0, 100), str)

    def test___gt___successfully(self):
        assert self.robot.price == 99.99
        assert self.robot_2.price == 5000.00
        self.assertEqual(self.robot < self.robot_2, f'Robot with ID 456 is more expensive than Robot with ID 123.')

    def test___eq___successfully(self):
        assert self.robot.price == 99.99
        assert self.robot_2.price == 5000.00
        self.robot.price = 5000.00
        assert self.robot.price == 5000.00
        assert isinstance(self.robot.price, float)
        self.assertEqual(self.robot > self.robot_2, f'Robot with ID 123 costs equal to Robot with ID 456.')

    def test___lt___successfully(self):
        assert self.robot.price == 99.99
        assert self.robot_2.price == 5000.00
        self.assertEqual(self.robot > self.robot_2, f'Robot with ID 123 is cheaper than Robot with ID 456.')


if __name__ == "__main__":
    unittest.main()
