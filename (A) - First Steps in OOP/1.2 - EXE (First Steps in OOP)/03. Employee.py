class Employee:
    MONTHS = 12

    def __init__(self, employee_id: int, first_name: str, last_name: str, salary: int):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        # self.months = 12

    def get_full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def get_annual_salary(self) -> int:
        total_year_salary = self.salary * self.MONTHS   # Employee.MONTHS == self.MONTHS
        # total_year_salary = self.salary * self.months
        return total_year_salary

    def raise_salary(self, amount: int) -> int:
        self.salary += amount
        total_salary = self.salary
        return total_salary


# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())
