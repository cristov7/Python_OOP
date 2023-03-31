import unittest
from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Tom", "Cat", "Meow")   # Arrange

    def test___init___successfully(self):
        name = self.mammal.name                      # Act
        expected_name = "Tom"                        # Act
        self.assertEqual(name, expected_name)        # Assert
        mammal_type = self.mammal.type
        expected_mammal_type = "Cat"
        self.assertEqual(mammal_type, expected_mammal_type)
        sound = self.mammal.sound
        expected_sound = "Meow"
        self.assertEqual(sound, expected_sound)
        # kingdom = self.mammal._Mammal__kingdom
        # expected_kingdom = "animals"
        # self.assertEqual(kingdom, expected_kingdom)

    def test_make_sound_successfully(self):
        result = self.mammal.make_sound()
        expected_result = "Tom makes Meow"
        self.assertEqual(result, expected_result)

    def test_get_kingdom_successfully(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_info_successfully(self):
        result = self.mammal.info()
        expected_result = "Tom is of type Cat"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
