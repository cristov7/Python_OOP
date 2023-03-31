class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Tom")

    def test_size_after_eating_successfully(self):
        self.cat.eat()
        size = self.cat.size
        expected_size = 1
        self.assertEqual(size, expected_size)

    def test_fed_after_eating_successfully(self):
        self.cat.eat()
        expected_fed = self.cat.fed
        self.assertTrue(expected_fed)

    def test_eat_and_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as content:
            self.cat.eat()
        result = str(content.exception)
        exception_result = "Already fed."
        self.assertEqual(result, exception_result)

    def test_sleep_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.cat.sleep()
        result = str(content.exception)
        exception_result = "Cannot sleep while hungry"
        self.assertEqual(result, exception_result)

    def test_sleep_successfully(self):
        self.cat.eat()
        self.cat.sleep()
        expected_sleepy = self.cat.sleepy
        self.assertFalse(expected_sleepy)


if __name__ == '__main__':
    unittest.main()
