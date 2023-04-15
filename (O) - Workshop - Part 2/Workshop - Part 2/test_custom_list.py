import unittest
from custom_list import CustomList


class CustomListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomList()

    def test___init___successfully(self):
        assert self.custom_list.custom_list == []
        assert isinstance(self.custom_list.custom_list, list)

    def test_append_successfully(self):
        assert self.custom_list.append("Hello!") == ["Hello!"]
        assert isinstance(self.custom_list.custom_list, list)
        assert self.custom_list.append("Bye!") == ["Hello!", "Bye!"]

    def test_remove_successfully(self):
        self.custom_list.custom_list = ["A", "B", "C"]
        assert self.custom_list.custom_list == ["A", "B", "C"]
        assert self.custom_list.remove(1) == "B"

    def test_remove_and_raise_index_error(self):
        with self.assertRaises(IndexError) as content:
            error = self.custom_list.remove(0)
        assert str(content.exception) == "'0' is invalid index!"

    def test_get_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert self.custom_list.get(2) == 3

    def test_get_and_raises_index_error(self):
        with self.assertRaises(IndexError) as content:
            error = self.custom_list.get(2)
        assert str(content.exception) == "'2' is invalid index!"

    def test_extend_successfully(self):
        assert self.custom_list.extend([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert isinstance(self.custom_list.custom_list, list)

    def test_insert_successfully(self):
        assert self.custom_list.insert(0, "Hello!") == ["Hello!"]
        assert self.custom_list.custom_list == ["Hello!"]
        assert isinstance(self.custom_list.custom_list, list)

    def test_pop_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert self.custom_list.pop() == 5

    def test_pop_and_raise_index_error(self):
        with self.assertRaises(IndexError) as content:
            error = self.custom_list.pop()
        assert str(content.exception) == "Can't pop from empty list!"

    def test_clear_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        self.custom_list.clear()
        assert self.custom_list.custom_list == []

    def test_index_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert self.custom_list.index(5) == 4

    def test_index_and_raise_index_error(self):
        with self.assertRaises(ValueError) as content:
            error = self.custom_list.index("Hello!")
        assert str(content.exception) == "'Hello!' is not in list!"

    def test_count_successfully(self):
        assert self.custom_list.count("Hello!") == 0
        self.custom_list.custom_list = ["Hello!", "Hello!", "Hello!", "3 times!"]
        assert self.custom_list.count("Hello!") == 3

    def test_reverse_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert self.custom_list.reverse() == [5, 4, 3, 2, 1]

    def test_copy_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert self.custom_list.copy() == [1, 2, 3, 4, 5]

    def test_size_successfully(self):
        assert self.custom_list.size() == 0
        self.custom_list.custom_list = [1, 2, 3]
        assert self.custom_list.custom_list == [1, 2, 3]
        assert self.custom_list.size() == 3

    def test_add_first_successfully(self):
        self.custom_list.add_first("Bye!")
        assert self.custom_list.custom_list == ["Bye!"]
        self.custom_list.add_first("Hello!")
        assert self.custom_list.custom_list == ["Hello!", "Bye!"]

    def test_dictionize_successfully(self):
        assert self.custom_list.dictionize() == {}
        self.custom_list.custom_list = [1, 2, 3, 4]
        assert self.custom_list.dictionize() == {1: 2, 3: 4}
        self.custom_list.custom_list += [5]
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.dictionize() == {1: 2, 3: 4, 5: " "}

    def test_move_successfully(self):
        self.custom_list.custom_list = [1, 2, 3, 4, 5]
        assert self.custom_list.custom_list == [1, 2, 3, 4, 5]
        assert self.custom_list.move(2) == [3, 4, 5, 1, 2]

    def test_move_and_raise_index_error(self):
        with self.assertRaises(IndexError) as content:
            error = self.custom_list.move(2)
        assert str(content.exception) == "'2' is invalid amount!"

    def test_sum_successfully(self):
        assert self.custom_list.sum() == 0
        self.custom_list.custom_list = [1, 2.5, "Hello!"]
        assert self.custom_list.custom_list == [1, 2.5, "Hello!"]
        assert self.custom_list.sum() == 9.5

    def test_overbound_successfully(self):
        self.custom_list.custom_list = [1, 2.5, "Hello!"]
        assert self.custom_list.custom_list == [1, 2.5, "Hello!"]
        assert self.custom_list.overbound() == 2

    def test_overbound_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            error = self.custom_list.overbound()
        assert str(content.exception) == "Can't return index from an empty list!"

    def test_underbound_successfully(self):
        self.custom_list.custom_list = [1, 2.5, "Hello!"]
        assert self.custom_list.custom_list == [1, 2.5, "Hello!"]
        assert self.custom_list.underbound() == 0

    def test_underbound_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            error = self.custom_list.underbound()
        assert str(content.exception) == "Can't return index from an empty list!"

    def test_is_empty_successfully(self):
        assert self.custom_list.is_empty() is True
        self.custom_list.custom_list = [1, 2, 3]
        assert self.custom_list.is_empty() is False

    def test_remove_all_occurrences_successfully(self):
        self.custom_list.custom_list = [0, 1, 0, 2, 0, 3, 0]
        assert self.custom_list.remove_all_occurrences(0) == [1, 2, 3]


if __name__ == '__main__':
    unittest.main()
