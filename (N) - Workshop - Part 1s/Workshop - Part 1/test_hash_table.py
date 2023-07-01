import unittest
from hash_table import HashTable


class TestCustomHashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.hash_table = HashTable()

    def test_correct_initializing(self):
        assert self.hash_table._HashTable__max_capacity == 4
        assert self.hash_table._HashTable__keys == [None] * 4
        assert self.hash_table._HashTable__values == [None] * 4

    def test__getitem__correct(self):
        self.hash_table["name"] = "Peter"
        assert self.hash_table["name"] == "Peter"

    def test__getitem_invalid_key_raises_key_error(self):
        with self.assertRaises(KeyError) as content:
            error = self.hash_table["KEY"]
        assert str(content.exception) == "'KEY is not a valid key!'"

    def test_correct_overwrite_on_key(self):
        self.hash_table["name"] = "Peter"
        self.hash_table["name"] = "Diyan"
        assert self.hash_table["name"] == "Diyan"

    def test_resizing_table_when_full(self):
        self.hash_table["1"] = "1"
        self.hash_table["2"] = "2"
        self.hash_table["3"] = "3"
        self.hash_table["4"] = "4"
        self.hash_table["5"] = "5"
        assert self.hash_table._HashTable__max_capacity == 8

    def test_index_generate_correct(self):
        assert self.hash_table._HashTable__calc_index("name") == 1

    def test_collision_and_no_free_space_to_the_end_of_the_array_starts_from_the_beginning(self):
        self.hash_table["name"] = "Peter"
        self.hash_table["age"] = 25
        self.hash_table["is_pet_owner"] = True
        self.hash_table["is_driver"] = False
        assert self.hash_table._HashTable__keys.index("is_driver") == 0

    def test_get_on_non_existing_key_without_default_value_returns_none(self):
        assert self.hash_table.get("KEY") is None

    def test_get_on_non_existing_key_with_default_value_returns_default_value(self):
        assert self.hash_table.get("KEY", "not valid")


if __name__ == "__main__":
    unittest.main()
