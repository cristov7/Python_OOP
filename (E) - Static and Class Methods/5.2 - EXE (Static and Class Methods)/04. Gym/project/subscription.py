class Subscription:
    id: int = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()
        Subscription.id += 1

    @staticmethod
    def get_next_id():
        next_id = Subscription.id
        return next_id

    def __repr__(self) -> str:
        subscription_id = self.id
        date = self.date
        return f"Subscription <{subscription_id}> on {date}"


# from project.class_id_mixin import ClassIdMixin
#
#
# class Subscription(ClassIdMixin):
#     id: int = 0
#
#     def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
#         self.date = date
#         self.customer_id = customer_id
#         self.trainer_id = trainer_id
#         self.exercise_id = exercise_id
#         self.id = self.get_next_id()
#
#     def __repr__(self) -> str:
#         subscription_id = self.id
#         date = self.date
#         return f"Subscription <{subscription_id}> on {date}"
