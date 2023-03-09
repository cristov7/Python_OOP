class Worker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        name = self.name
        age = self.age
        salary = self.salary
        return f"Name: {name}, Age: {age}, Salary: {salary}"
