from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []   # [animal_objects]
        self.workers: List[Worker] = []   # [worker_objects]

    def add_animal(self, animal: Animal, price: int) -> str:   # animal == animal_object
        if len(self.animals) < self.__animal_capacity:
            if price < self.__budget:
                self.__budget -= price
                self.animals.append(animal)
                name = animal.name
                type_of_animal = animal.__class__.__name__
                return f"{name} the {type_of_animal} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:   # worker == worker_object
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            name = worker.name
            type_of_worker = worker.__class__.__name__
            return f"{name} the {type_of_worker} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        worker_objects_list = [worker_object for worker_object in self.workers
                               if worker_object.name == worker_name]
        if worker_objects_list:
            worker_object = worker_objects_list[0]
            self.workers.remove(worker_object)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_workers_salaries = sum([worker_object.salary for worker_object in self.workers])
        if total_workers_salaries <= self.__budget:
            self.__budget -= total_workers_salaries
            left_budget = self.__budget
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animals_expenses = sum([animal_object.money_for_care for animal_object in self.animals])
        if total_animals_expenses <= self.__budget:
            self.__budget -= total_animals_expenses
            left_budget = self.__budget
            return f"You tended all the animals. They are happy. Budget left: {left_budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        total_animals_count = len(self.animals)
        lions_info_list = []
        tigers_info_list = []
        cheetahs_info_list = []
        for animal_object in self.animals:
            if animal_object.__class__.__name__ == "Lion":
                lions_info_list.append(animal_object.__repr__())
            elif animal_object.__class__.__name__ == "Tiger":
                tigers_info_list.append(animal_object.__repr__())
            elif animal_object.__class__.__name__ == "Cheetah":
                cheetahs_info_list.append(animal_object.__repr__())
            else:
                continue
        animals_status_list = [f"You have {total_animals_count} animals"]
        if lions_info_list:
            amount_of_lions = len(lions_info_list)
            animals_status_list.append(f"----- {amount_of_lions} Lions:")
            lions_info = "\n".join(lions_info_list)
            animals_status_list.append(lions_info)
        if tigers_info_list:
            amount_of_tigers = len(tigers_info_list)
            animals_status_list.append(f"----- {amount_of_tigers} Tigers:")
            tigers_info = "\n".join(tigers_info_list)
            animals_status_list.append(tigers_info)
        if cheetahs_info_list:
            amount_of_cheetahs = len(cheetahs_info_list)
            animals_status_list.append(f"----- {amount_of_cheetahs} Cheetahs:")
            cheetahs_info = "\n".join(cheetahs_info_list)
            animals_status_list.append(cheetahs_info)
        return "\n".join(animals_status_list)

    def workers_status(self) -> str:
        total_workers_count = len(self.workers)
        keepers_info_list = []
        caretakers_info_list = []
        vets_info_list = []
        for worker_object in self.workers:
            if worker_object.__class__.__name__ == "Keeper":
                keepers_info_list.append(worker_object.__repr__())
            elif worker_object.__class__.__name__ == "Caretaker":
                caretakers_info_list.append(worker_object.__repr__())
            elif worker_object.__class__.__name__ == "Vet":
                vets_info_list.append(worker_object.__repr__())
            else:
                continue
        workers_status_list = [f"You have {total_workers_count} workers"]
        if keepers_info_list:
            amount_of_keepers = len(keepers_info_list)
            workers_status_list.append(f"----- {amount_of_keepers} Keepers:")
            keepers_info = "\n".join(keepers_info_list)
            workers_status_list.append(keepers_info)
        if caretakers_info_list:
            amount_of_keepers = len(caretakers_info_list)
            workers_status_list.append(f"----- {amount_of_keepers} Caretakers:")
            caretakers_info = "\n".join(caretakers_info_list)
            workers_status_list.append(caretakers_info)
        if vets_info_list:
            amount_of_vets = len(vets_info_list)
            workers_status_list.append(f"----- {amount_of_vets} Vets:")
            vets_info = "\n".join(vets_info_list)
            workers_status_list.append(vets_info)
        return "\n".join(workers_status_list)
