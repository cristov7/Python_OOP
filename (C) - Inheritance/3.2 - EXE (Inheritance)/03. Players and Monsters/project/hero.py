class Hero:
    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __str__(self) -> str:
        name = self.username
        class_name = self.__class__.__name__
        level = self.level
        return f"{name} of type {class_name} has level {level}"
