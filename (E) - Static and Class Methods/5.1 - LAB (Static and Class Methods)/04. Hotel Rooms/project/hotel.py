from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []   # [room_objects]
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:   # room = object_room
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> [str, None]:
        room_objects_list = [room_object for room_object in self.rooms
                             if room_object.number == room_number]
        if room_objects_list:
            room_object = room_objects_list[0]
            info = room_object.take_room(people)
            if info:
                return info
            else:
                self.guests += people

    def free_room(self, room_number: int) -> [str, None]:
        room_objects_list = [room_object for room_object in self.rooms
                             if room_object.number == room_number]
        if room_objects_list:
            room_object = room_objects_list[0]
            current_guests = room_object.guests
            info = room_object.free_room()
            if info:
                return info
            else:
                self.guests -= current_guests

    def status(self) -> str:
        name = self.name
        guests = self.guests
        free_rooms_list = [str(room_object.number) for room_object in self.rooms
                           if not room_object.is_taken]
        taken_rooms_list = [str(room_object.number) for room_object in self.rooms
                            if room_object.is_taken]
        free_rooms = ", ".join(free_rooms_list)
        taken_rooms = ", ".join(taken_rooms_list)
        return f"Hotel {name} has {guests} total guests" \
               f"\nFree rooms: {free_rooms}" \
               f"\nTaken rooms: {taken_rooms}"
