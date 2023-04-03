from typing import List
from project.band import Band
from project.band_members.musician import Musician
from project.concert import Concert
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer


class ConcertTrackerApp:
    @property   # getter
    def valid_musician_types(self) -> dict:
        return {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []           # contain all the bands (objects)
        self.musicians: List[Musician] = []   # contain all the musicians (objects)
        self.concerts: List[Concert] = []     # contain all the concerts (objects)

    def create_musician(self, musician_type: str, name: str, age: int) -> [ValueError, Exception, str]:
        musician_name = name
        if musician_type not in self.valid_musician_types.keys():
            raise ValueError("Invalid musician type!")
        elif name in [name for musician_object in self.musicians
                      if musician_object.name == name]:
            raise Exception(f"{musician_name} is already a musician!")
        else:
            class_name = self.valid_musician_types[musician_type]
            musician_object = class_name(name, age)
            self.musicians.append(musician_object)
            return f"{musician_name} is now a {musician_type}."

    def create_band(self, name: str) -> [Exception, str]:
        band_name = name
        if name in [name for band_object in self.bands
                    if band_object.name == name]:
            raise Exception(f"{band_name} band is already created!")
        else:
            band_object = Band(name)
            self.bands.append(band_object)
            return f"{band_name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> [Exception, None]:
        concert_place = place
        concert_genre = genre
        if place in [place for concert_object in self.concerts
                     if concert_object.place == place]:
            raise Exception(f"{concert_place} is already registered for {concert_genre} concert!")
        else:
            concert_object = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(concert_object)
            return f"{concert_genre} concert in {concert_place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> [Exception, str]:
        musician_objects_list = [musician_object for musician_object in self.musicians
                                 if musician_object.name == musician_name]
        if not musician_objects_list:
            raise Exception(f"{musician_name} isn't a musician!")
        else:
            band_objects_list = [band_object for band_object in self.bands
                                 if band_object.name == band_name]
            if not band_objects_list:
                raise Exception(f"{band_name} isn't a band!")
            else:
                musician_object = musician_objects_list[0]
                band_object = band_objects_list[0]
                band_object.members.append(musician_object)
                return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> [Exception, str]:
        band_objects_list = [band_object for band_object in self.bands
                             if band_object.name == band_name]
        if not band_objects_list:
            raise Exception(f"{band_name} isn't a band!")
        else:
            band_object = band_objects_list[0]
            musician_objects_list = [musician_object for musician_object in band_object.members
                                     if musician_object.name == musician_name]
            if not musician_objects_list:
                raise Exception(f"{musician_name} isn't a member of {band_name}!")
            else:
                musician_object = musician_objects_list[0]
                band_object.members.remove(musician_object)
                return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def check_singers_qualified(singers_objects_list: list, genre: str) -> bool:
        qualified_members_list = []
        for singer_object in singers_objects_list:
            if genre == "Rock" and "sing high pitch notes" in singer_object.skills:
                qualified_members_list.append(True)
            elif genre == "Metal" and "sing low pitch notes" in singer_object.skills:
                qualified_members_list.append(True)
            elif genre == "Jazz" and "sing high pitch notes" in singer_object.skills and \
                    "sing low pitch notes" in singer_object.skills:
                qualified_members_list.append(True)
            else:
                qualified_members_list.append(False)
        if all(qualified_members_list):
            return True
        else:
            return False

    @staticmethod
    def check_drummers_qualified(drummers_objects_list: list, genre: str) -> bool:
        qualified_members_list = []
        for drummer_object in drummers_objects_list:
            if genre == "Rock" and "play the drums with drumsticks" in drummer_object.skills:
                qualified_members_list.append(True)
            elif genre == "Metal" and "play the drums with drumsticks" in drummer_object.skills:
                qualified_members_list.append(True)
            elif genre == "Jazz" and "play the drums with drum brushes" in drummer_object.skills:
                qualified_members_list.append(True)
            else:
                qualified_members_list.append(False)
        if all(qualified_members_list):
            return True
        else:
            return False

    @staticmethod
    def check_guitarists_qualified(guitarists_objects_list: list, genre: str) -> bool:
        qualified_members_list = []
        for guitarist_object in guitarists_objects_list:
            if genre == "Rock" and "play rock" in guitarist_object.skills:
                qualified_members_list.append(True)
            elif genre == "Metal" and "play metal" in guitarist_object.skills:
                qualified_members_list.append(True)
            elif genre == "Jazz" and "play jazz" in guitarist_object.skills:
                qualified_members_list.append(True)
            else:
                qualified_members_list.append(False)
        if all(qualified_members_list):
            return True
        else:
            return False

    def start_concert(self, concert_place: str, band_name: str) -> [Exception, str]:
        band_object = next(iter([band_object for band_object in self.bands
                                 if band_object.name == band_name]))
        concert_object = next(iter([concert_object for concert_object in self.concerts
                                    if concert_object.place == concert_place]))
        singers_objects_list = [member_object for member_object in band_object.members
                                if type(member_object) == Singer]
        drummers_objects_list = [member_object for member_object in band_object.members
                                 if type(member_object) == Drummer]
        guitarists_objects_list = [member_object for member_object in band_object.members
                                   if type(member_object) == Guitarist]
        if not all([singers_objects_list, drummers_objects_list, guitarists_objects_list]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        else:
            concert_genre = concert_object.genre
            singers_qualified = self.check_singers_qualified(singers_objects_list, concert_genre)
            drummers_qualified = self.check_drummers_qualified(drummers_objects_list, concert_genre)
            guitarists_qualified = self.check_guitarists_qualified(guitarists_objects_list, concert_genre)
            if not all([singers_qualified, drummers_qualified, guitarists_qualified]):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            else:
                audience = concert_object.audience
                ticket_price = concert_object.ticket_price
                expenses = concert_object.expenses
                profit = (audience * ticket_price) - expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert_genre} concert in {concert_place}."
