import unittest
from list import IntegerList


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_object = IntegerList(1, "2", 2, 3.0, 3, 3.5, "4", 4, 5)

    def test_get_data_and_return_the_list(self):
        result = self.integer_object.get_data()
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected_result)

    def test_add_an_element_and_return_the_list(self):
        result = self.integer_object.add(6)
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected_result)

    def test_add_an_element_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.integer_object.add("6")
        result = str(content.exception)
        expected_result = "Element is not Integer"
        self.assertEqual(result, expected_result)

    def test_remove_index_and_return_the_value(self):
        result = self.integer_object.remove_index(4)
        expected_result = 5
        self.assertEqual(result, expected_result)

    def test_remove_index_and_raise_index_error(self):
        with self.assertRaises(IndexError) as content:
            self.integer_object.remove_index(100)
        result = str(content.exception)
        expected_result = "Index is out of range"
        self.assertEqual(result, expected_result)

    def test_get_and_return_the_specific_element(self):
        result = self.integer_object.get(0)
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_get_and_raise_index_error(self):
        with self.assertRaises(IndexError) as content:
            self.integer_object.get(100)
        result = str(content.exception)
        expected_result = "Index is out of range"
        self.assertEqual(result, expected_result)

    def test_insert_successfully(self):
        result = self.integer_object.insert(0, 0)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_insert_and_raise_index_error(self):
        with self.assertRaises(IndexError) as content:
            self.integer_object.insert(100, 100)
        result = str(content.exception)
        expected_result = "Index is out of range"
        self.assertEqual(result, expected_result)

    def test_insert_and_raise_value_error(self):
        with self.assertRaises(ValueError) as content:
            self.integer_object.insert(0, "0")
        result = str(content.exception)
        expected_result = "Element is not Integer"
        self.assertEqual(result, expected_result)

    def test_get_biggest_and_return_the_value(self):
        result = self.integer_object.get_biggest()
        expected_result = 5
        self.assertEqual(result, expected_result)

    def test_get_index_and_return_the_index(self):
        result = self.integer_object.get_index(1)
        expected_result = 0
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
