from typing import List
from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot


class RobotsManagingApp:
    VALID_SERVICES_TYPES: dict = {"MainService": MainService,
                                  "SecondaryService": SecondaryService}

    VALID_ROBOTS_TYPES: dict = {"MaleRobot": MaleRobot,
                                "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []       # all robots (objects) that are created
        self.services: List[BaseService] = []   # all services (objects) that are created

    def add_service(self, service_type: str, name: str) -> [Exception, str]:
        if service_type not in self.VALID_SERVICES_TYPES.keys():
            raise Exception("Invalid service type!")
        else:
            class_name = self.VALID_SERVICES_TYPES[service_type]
            service_object = class_name(name)
            self.services.append(service_object)
            return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> [Exception, str]:
        if robot_type not in self.VALID_ROBOTS_TYPES.keys():
            raise Exception("Invalid robot type!")
        else:
            class_name = self.VALID_ROBOTS_TYPES[robot_type]
            robot_object = class_name(name, kind, price)
            self.robots.append(robot_object)
            return f"{robot_type} is successfully added."

    def __get_robot_object_by_robot_name(self, robot_name: str) -> [BaseRobot, None]:
        robot_objects_list = [robot_object for robot_object in self.robots
                              if robot_object.name == robot_name]
        if robot_objects_list:
            robot_object = robot_objects_list[0]
            return robot_object

    def __get_service_object_by_service_name(self, service_name: str) -> [BaseService, None]:
        service_objects_list = [service_object for service_object in self.services
                                if service_object.name == service_name]
        if service_objects_list:
            service_object = service_objects_list[0]
            return service_object

    def add_robot_to_service(self, robot_name: str, service_name: str) -> [str, Exception]:
        robot_object = self.__get_robot_object_by_robot_name(robot_name)
        service_object = self.__get_service_object_by_service_name(service_name)
        robot_class_name = robot_object.__class__.__name__
        service_class_name = service_object.__class__.__name__
        if robot_class_name == "FemaleRobot" and service_class_name == "SecondaryService":
            if len(service_object.robots) < service_object.capacity:
                self.robots.remove(robot_object)
                service_object.robots.append(robot_object)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        elif robot_class_name == "MaleRobot" and service_class_name == "MainService":
            if len(service_object.robots) < service_object.capacity:
                self.robots.remove(robot_object)
                service_object.robots.append(robot_object)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> [str, Exception]:
        service_object = self.__get_service_object_by_service_name(service_name)
        robot_objects_list = [robot_object for robot_object in service_object.robots
                              if robot_object.name == robot_name]
        if robot_objects_list:
            robot_object = robot_objects_list[0]
            service_object.robots.remove(robot_object)
            self.robots.append(robot_object)
            return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service_object = self.__get_service_object_by_service_name(service_name)
        for robot_object in service_object.robots:
            robot_object.eating()
        number_of_robots_fed = len(service_object.robots)
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str) -> str:
        service_object = self.__get_service_object_by_service_name(service_name)
        total_price = sum([robot_object.price for robot_object in service_object.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self) -> str:
        services_list = []
        for service_object in self.services:
            service_details = service_object.details()
            services_list.append(service_details)
        return "\n".join(services_list)
