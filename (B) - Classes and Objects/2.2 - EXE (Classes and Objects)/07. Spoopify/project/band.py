from typing import List
from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []   # [album_objects]

    def add_album(self, album: Album) -> str:
        band_name = self.name
        album_name = album.name
        if album in self.albums:
            return f"Band {band_name} already has {album_name} in their library."
        else:   # elif album not in self.albums:
            self.albums.append(album)
            return f"Band {band_name} has added their newest album {album_name}."

    def remove_album(self, album_name: str) -> str:
        album_objects_list = [album_object for album_object in self.albums
                              if album_object.name == album_name]
        if album_objects_list:   # if len(album_objects_list) > 0:
            album_object = album_objects_list[0]
            if album_object.published:   # if album_object.published == True:
                return "Album has been published. It cannot be removed."
            else:   # elif album_object.published == False:
                self.albums.remove(album_object)
                return f"Album {album_name} has been removed."
        else:   # elif len(album_objects_list) == 0:
            return f"Album {album_name} is not found."

    def details(self) -> str:
        name = self.name
        album_details = "\n".join([album_object.details()
                                   for album_object in self.albums])
        return f"Band {name}" \
               f"\n{album_details}"
