class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def test___init___successfully(self):
        worker = Worker("Alex", 2500, 100)
        name = worker.name
        expected_name = "Alex"
        self.assertEqual(name, expected_name)
        salary = worker.salary
        expected_salary = 2500
        self.assertEqual(salary, expected_salary)
        energy = worker.energy
        expected_energy = 100
        self.assertEqual(energy, expected_energy)
        money = worker.money
        expected_money = 0
        self.assertEqual(money, expected_money)

    def test_work_and_raise_exception(self):
        worker = Worker("Alex", 2500, 0)
        with self.assertRaises(Exception) as content:
            worker.work()
        result = str(content.exception)
        expected_result = "Not enough energy."
        self.assertEqual(result, expected_result)

    def test_work_successfully(self):
        worker = Worker("Alex", 2500, 100)
        worker.work()
        energy = worker.energy
        expected_energy = 99
        self.assertEqual(energy, expected_energy)
        money = worker.money
        expected_money = 2500
        self.assertEqual(money, expected_money)

    def test_rest_successfully(self):
        worker = Worker("Alex", 2500, 100)
        worker.rest()
        energy = worker.energy
        expected_energy = 101
        self.assertEqual(energy, expected_energy)

    def test_get_info_successfully(self):
        worker = Worker("Alex", 2500, 100)
        result = worker.get_info()
        expected_result = "Alex has saved 0 money."
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
