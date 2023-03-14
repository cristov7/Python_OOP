from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []           # [customer_objects]
        self.trainers: List[Trainer] = []             # [trainer_objects]
        self.equipment: List[Equipment] = []          # [equipment_objects]
        self.plans: List[ExercisePlan] = []           # [exercise_plan_objects]
        self.subscriptions: List[Subscription] = []   # [subscription_objects]

    def add_customer(self, customer: Customer) -> None:   # customer == customer_object
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:   # trainer == trainer_object
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:   # equipment == equipment_object
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:   # plan == plan_object
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:   # subscription == subscription_object
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def search_object(object_id: int, objects_list: list) -> [object, None]:
        current_objects_list = [current_object for current_object in objects_list
                                if current_object.id == object_id]
        if current_objects_list:
            current_object = current_objects_list[0]
            return current_object

    def subscription_info(self, subscription_id: int) -> [str, None]:
        subscription_object = self.search_object(subscription_id, self.subscriptions)
        if subscription_object:
            customer_id = subscription_object.customer_id
            customer_object = self.search_object(customer_id, self.customers)
            if customer_object:
                trainer_id = subscription_object.trainer_id
                trainer_object = self.search_object(trainer_id, self.trainers)
                if trainer_object:
                    plan_id = subscription_object.exercise_id
                    exercise_plan_object = self.search_object(plan_id, self.plans)
                    if exercise_plan_object:
                        equipment_id = exercise_plan_object.equipment_id
                        equipment_object = self.search_object(equipment_id, self.equipment)
                        if equipment_object:
                            subscription = subscription_object.__repr__()
                            customer = customer_object.__repr__()
                            trainer = trainer_object.__repr__()
                            equipment = equipment_object.__repr__()
                            exercise_plan = exercise_plan_object.__repr__()
                            return f"{subscription}" \
                                   f"\n{customer}" \
                                   f"\n{trainer}" \
                                   f"\n{equipment}" \
                                   f"\n{exercise_plan}"
