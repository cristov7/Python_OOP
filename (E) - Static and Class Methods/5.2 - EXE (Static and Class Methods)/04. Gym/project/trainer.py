class Trainer:
    id: int = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        Trainer.id += 1

    @staticmethod
    def get_next_id():
        next_id = Trainer.id
        return next_id

    def __repr__(self) -> str:
        trainer_id = self.id
        name = self.name
        return f"Trainer <{trainer_id}> {name}"


# from project.class_id_mixin import ClassIdMixin
#
#
# class Trainer(ClassIdMixin):
#     id: int = 0
#
#     def __init__(self, name: str):
#         self.name = name
#         self.id = self.get_next_id()
#
#     def __repr__(self) -> str:
#         trainer_id = self.id
#         name = self.name
#         return f"Trainer <{trainer_id}> {name}"
