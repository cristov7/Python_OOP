from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY: int = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self) -> str:   # implemented method
        service_name = self.name
        robot_names = " ".join(robot_object.name for robot_object in self.robots) if self.robots else "none"
        return f"{service_name} Secondary Service:" \
               f"\nRobots: {robot_names}"
