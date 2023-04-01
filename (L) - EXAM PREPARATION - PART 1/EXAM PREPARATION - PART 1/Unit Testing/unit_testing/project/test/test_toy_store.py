from project.toy_store import ToyStore
import unittest


class ToyStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test___init___successfully(self):
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_add_toy_shelf_does_not_exist_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.toy_store.add_toy("H", "Funko")
        result = str(content.exception)
        expected_result = "Shelf doesn't exist!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_add_toy_toy_is_already_in_shelf_and_raise_exception(self):
        self.toy_store.toy_shelf["A"] = "Funko"
        with self.assertRaises(Exception) as content:
            self.toy_store.add_toy("A", "Funko")
        result = str(content.exception)
        expected_result = "Toy is already in shelf!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": "Funko", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_add_toy_shelf_is_already_taken_and_raise_exception(self):
        self.toy_store.toy_shelf["A"] = "Funko"
        with self.assertRaises(Exception) as content:
            self.toy_store.add_toy("A", "Funko-Pop")
        result = str(content.exception)
        expected_result = "Shelf is already taken!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": "Funko", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_add_toy_successfully(self):
        result = self.toy_store.add_toy("A", "Funko")
        expected_result = "Toy:Funko placed successfully!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": "Funko", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_remove_toy_shelf_does_not_exist_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.toy_store.remove_toy("H", "Funko")
        result = str(content.exception)
        expected_result = "Shelf doesn't exist!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_remove_toy_toy_in_that_shelf_does_not_exists_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.toy_store.remove_toy("A", "Funko")
        result = str(content.exception)
        expected_result = "Toy in that shelf doesn't exists!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)

    def test_remove_toy_successfully(self):
        self.toy_store.toy_shelf["A"] = "Funko"
        result = self.toy_store.remove_toy("A", "Funko")
        expected_result = "Remove toy:Funko successfully!"
        self.assertEqual(result, expected_result)
        toy_shelf = self.toy_store.toy_shelf
        expected_toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(toy_shelf, expected_toy_shelf)


if __name__ == '__main__':
    unittest.main()
