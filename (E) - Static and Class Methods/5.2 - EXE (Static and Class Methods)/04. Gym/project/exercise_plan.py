class ExercisePlan:
    id: int = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration   # minutes
        self.id = self.get_next_id()
        ExercisePlan.id += 1

    @staticmethod
    def get_next_id():
        next_id = ExercisePlan.id
        return next_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        duration = hours * 60   # minutes
        return cls(trainer_id, equipment_id, duration)

    def __repr__(self) -> str:
        exercise_plan_id = self.id
        duration = self.duration
        return f"Plan <{exercise_plan_id}> with duration {duration} minutes"


# from project.class_id_mixin import ClassIdMixin
#
#
# class ExercisePlan(ClassIdMixin):
#     id: int = 0
#
#     def __init__(self, trainer_id: int, equipment_id: int, duration: int):
#         self.trainer_id = trainer_id
#         self.equipment_id = equipment_id
#         self.duration = duration   # minutes
#         self.id = self.get_next_id()
#
#     @classmethod
#     def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
#         duration = hours * 60   # minutes
#         return cls(trainer_id, equipment_id, duration)
#
#     def __repr__(self) -> str:
#         exercise_plan_id = self.id
#         duration = self.duration
#         return f"Plan <{exercise_plan_id}> with duration {duration} minutes"
