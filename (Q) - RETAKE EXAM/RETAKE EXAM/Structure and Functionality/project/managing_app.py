from typing import List, Dict
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.route import Route
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []             # all users (objects) that are created
        self.vehicles: List[BaseVehicle] = []   # all vehicles (objects) that are created
        self.routes: List[Route] = []           # all routes (objects) that are created

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        if [user_object for user_object in self.users
           if user_object.driving_license_number == driving_license_number]:
            return f"{driving_license_number} has already been registered to our platform."
        else:
            user_object = User(first_name, last_name, driving_license_number)
            self.users.append(user_object)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    @property   # getter
    def valid_type_vehicles(self) -> Dict[str, PassengerCar or CargoVan]:
        valid_type_vehicles_dict: Dict[str, PassengerCar or CargoVan] = {"PassengerCar": PassengerCar,
                                                                         "CargoVan": CargoVan}
        return valid_type_vehicles_dict

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in self.valid_type_vehicles.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."
        elif [vehicle_object for vehicle_object in self.vehicles
              if vehicle_object.license_plate_number == license_plate_number]:
            return f"{license_plate_number} belongs to another vehicle."
        else:
            vehicle_class = self.valid_type_vehicles[vehicle_type]
            vehicle_object = vehicle_class(brand, model, license_plate_number)
            self.vehicles.append(vehicle_object)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        if [route_object for route_object in self.routes
           if route_object.start_point == start_point and
           route_object.end_point == end_point and
           route_object.length == length]:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        elif [route_object for route_object in self.routes
              if route_object.start_point == start_point and
              route_object.end_point == end_point and
              route_object.length < length]:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."
        else:
            route_id = len(self.routes) + 1
            route_object = Route(start_point, end_point, length, route_id)
            self.routes.append(route_object)
            longer_route_objects_list = [route_object for route_object in self.routes
                                         if route_object.start_point == start_point and
                                         route_object.end_point == end_point and
                                         route_object.length > length]
            if longer_route_objects_list:
                longer_route_object = longer_route_objects_list[0]
                longer_route_object.is_locked = True
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool) -> str:
        user_object = [user_object for user_object in self.users
                       if user_object.driving_license_number == driving_license_number][0]
        vehicle_object = [vehicle_object for vehicle_object in self.vehicles
                          if vehicle_object.license_plate_number == license_plate_number][0]
        route_object = [route_object for route_object in self.routes
                        if route_object.route_id == route_id][0]
        if user_object.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        elif vehicle_object.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        elif route_object.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        else:
            mileage = route_object.length
            vehicle_object.drive(mileage)
            if is_accident_happened:
                vehicle_object.change_status()
                user_object.decrease_rating()
            else:
                user_object.increase_rating()
            vehicle_info = vehicle_object.__str__()
            return vehicle_info

    def repair_vehicles(self, count: int) -> str:
        damaged_vehicle_objects_dict = {vehicle_object: [vehicle_object.brand, vehicle_object.model]
                                        for vehicle_object in self.vehicles
                                        if vehicle_object.is_damaged}
        sorted_damaged_vehicle_objects_list = list(sorted(damaged_vehicle_objects_dict.items(), key=lambda x: (x[1][0], x[1][1])))
        count_damaged_vehicle_objects = len(sorted_damaged_vehicle_objects_list)
        if count_damaged_vehicle_objects < count:
            count = count_damaged_vehicle_objects
        for index_damage_vehicle_vehicle_object in range(count):
            vehicle_object_tuple = sorted_damaged_vehicle_objects_list[index_damage_vehicle_vehicle_object]
            vehicle_object = vehicle_object_tuple[0]
            vehicle_object.change_status()
            vehicle_object.recharge()
        count_of_repaired_vehicles = count
        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self) -> str:
        users_list = ["*** E-Drive-Rent ***"]
        user_objects_dict = {user_object: user_object.rating for user_object in self.users}
        sorted_user_objects_dict = dict(sorted(user_objects_dict.items(), key=lambda x: x[1], reverse=True))
        [users_list.append(user_object.__str__())
         for user_object, user_object_rating in sorted_user_objects_dict.items()]
        users = "\n".join(users_list)
        return users
