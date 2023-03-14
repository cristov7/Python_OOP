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

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            name = animal.name
            type_of_animal = animal.__class__.__name__
            return f"{name} the {type_of_animal} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            name = worker.name
            type_of_worker = worker.__class__.__name__
            return f"{name} the {type_of_worker} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        worker_objects_list = [worker_object for worker_object in self.workers
                               if worker_object.name == worker_name]
        if worker_objects_list:
            worker_object = worker_objects_list[0]
            self.workers.remove(worker_object)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        workers_salaries = sum([worker_object.salary for worker_object in self.workers])
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            left_budget = self.__budget
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        animal_expenses = sum([animal_object.money_for_care for animal_object in self.animals])
        if self.__budget >= animal_expenses:
            self.__budget -= animal_expenses
            left_budget = self.__budget
            return f"You tended all the animals. They are happy. Budget left: {left_budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self) -> str:
        total_animals_count = len(self.animals)
        lions_objects_list = [animal_object.__repr__() for animal_object in self.animals
                              if animal_object.__class__.__name__ == "Lion"]
        amount_of_lions = len(lions_objects_list)
        lions = "\n".join(lions_objects_list)
        tigers_objects_list = [animal_object.__repr__() for animal_object in self.animals
                               if animal_object.__class__.__name__ == "Tiger"]
        amount_of_tigers = len(tigers_objects_list)
        tigers = "\n".join(tigers_objects_list)
        cheetahs_objects_list = [animal_object.__repr__() for animal_object in self.animals
                                 if animal_object.__class__.__name__ == "Cheetah"]
        amount_of_cheetahs = len(cheetahs_objects_list)
        cheetahs = "\n".join(cheetahs_objects_list)
        return f"You have {total_animals_count} animals" \
               f"\n----- {amount_of_lions} Lions:" \
               f"\n{lions}" \
               f"\n----- {amount_of_tigers} Tigers:" \
               f"\n{tigers}" \
               f"\n----- {amount_of_cheetahs} Cheetahs:" \
               f"\n{cheetahs}"

    def workers_status(self):
        total_workers_count = len(self.workers)
        keeper_objects_list = [worker_object.__repr__() for worker_object in self.workers
                               if worker_object.__class__.__name__ == "Keeper"]
        amount_of_keepers = len(keeper_objects_list)
        keepers = "\n".join(keeper_objects_list)
        caretaker_objects_list = [worker_object.__repr__() for worker_object in self.workers
                                  if worker_object.__class__.__name__ == "Caretaker"]
        amount_of_caretakers = len(caretaker_objects_list)
        caretakers = "\n".join(caretaker_objects_list)
        vet_objects_list = [worker_object.__repr__() for worker_object in self.workers
                            if worker_object.__class__.__name__ == "Vet"]
        amount_of_vets = len(vet_objects_list)
        vets = "\n".join(vet_objects_list)
        return f"You have {total_workers_count} workers" \
               f"\n----- {amount_of_keepers} Keepers:" \
               f"\n{keepers}" \
               f"\n----- {amount_of_caretakers} Caretakers:" \
               f"\n{caretakers}" \
               f"\n----- {amount_of_vets} Vets:" \
               f"\n{vets}"
