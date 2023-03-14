class Equipment:
    id: int = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        Equipment.id += 1

    @staticmethod
    def get_next_id():
        next_id = Equipment.id
        return next_id

    def __repr__(self) -> str:
        equipment_id = self.id
        name = self.name
        return f"Equipment <{equipment_id}> {name}"


# from project.class_id_mixin import ClassIdMixin
#
#
# class Equipment(ClassIdMixin):
#     id: int = 0
#
#     def __init__(self, name: str):
#         self.name = name
#         self.id = self.get_next_id()
#
#     def __repr__(self) -> str:
#         equipment_id = self.id
#         name = self.name
#         return f"Equipment <{equipment_id}> {name}"
