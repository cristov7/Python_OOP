from typing import Dict, List
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []       # all robots (objects) that are created
        self.services: List[BaseService] = []   # all services (objects) that are created

    @property   # getter
    def valid_service_types(self) -> Dict[str, MainService or SecondaryService]:
        valid_service_types_dict = {"MainService": MainService,
                                    "SecondaryService": SecondaryService}
        return valid_service_types_dict

    def add_service(self, service_type: str, name: str) -> [Exception, str]:
        if service_type not in self.valid_service_types.keys():
            raise Exception("Invalid service type!")
        else:
            service_class_name = self.valid_service_types[service_type]
            service_object = service_class_name(name)
            self.services.append(service_object)
            return f"{service_type} is successfully added."

    @property   # getter
    def valid_robot_types(self) -> Dict[str, MaleRobot or FemaleRobot]:
        valid_robot_types_dict = {"MaleRobot": MaleRobot,
                                  "FemaleRobot": FemaleRobot}
        return valid_robot_types_dict

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> [Exception, str]:
        if robot_type not in self.valid_robot_types.keys():
            raise Exception("Invalid robot type!")
        else:
            robot_class_name = self.valid_robot_types[robot_type]
            robot_object = robot_class_name(name, kind, price)
            self.robots.append(robot_object)
            return f"{robot_type} is successfully added."

    @staticmethod   # staticmethod
    def __get_robot_object_by_robot_name(robot_name: str, robots_list: List[BaseRobot]) -> [BaseRobot, None]:
        robot_objects_list = [robot_object for robot_object in robots_list
                              if robot_object.name == robot_name]
        if robot_objects_list:
            robot_object = robot_objects_list[0]
            return robot_object

    @staticmethod   # staticmethod
    def __get_service_object_by_service_name(service_name: str, services_list: List[BaseService]) -> [BaseService, None]:
        service_objects_list = [service_object for service_object in services_list
                                if service_object.name == service_name]
        if service_objects_list:
            service_object = service_objects_list[0]
            return service_object

    @staticmethod   # staticmethod
    def __add_robot_object_to_service(service_object: BaseService, robot_object: BaseRobot, robots_list: List[BaseRobot]) -> [str, Exception]:
        if len(service_object.robots) < service_object.capacity:
            robots_list.remove(robot_object)
            service_object.robots.append(robot_object)
            robot_name = robot_object.name
            service_name = service_object.name
            return f"Successfully added {robot_name} to {service_name}."
        else:
            raise Exception("Not enough capacity for this robot!")

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot_object = self.__get_robot_object_by_robot_name(robot_name, self.robots)
        service_object = self.__get_service_object_by_service_name(service_name, self.services)
        robot_class_name = robot_object.__class__.__name__
        service_class_name = service_object.__class__.__name__
        if robot_class_name == "FemaleRobot" and service_class_name == "SecondaryService":
            return self.__add_robot_object_to_service(service_object, robot_object, self.robots)
        elif robot_class_name == "MaleRobot" and service_class_name == "MainService":
            return self.__add_robot_object_to_service(service_object, robot_object, self.robots)
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> [str, Exception]:
        service_object = self.__get_service_object_by_service_name(service_name, self.services)
        robot_object = self.__get_robot_object_by_robot_name(robot_name, service_object.robots)
        if robot_object:
            service_object.robots.remove(robot_object)
            self.robots.append(robot_object)
            return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service_object = self.__get_service_object_by_service_name(service_name, self.services)
        [robot_object.eating() for robot_object in service_object.robots]
        number_of_robots_fed = len(service_object.robots)
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str) -> str:
        service_object = self.__get_service_object_by_service_name(service_name, self.services)
        total_price = sum([robot_object.price for robot_object in service_object.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self) -> str:
        services_list = [service_object.details() for service_object in self.services]
        return "\n".join(services_list)
