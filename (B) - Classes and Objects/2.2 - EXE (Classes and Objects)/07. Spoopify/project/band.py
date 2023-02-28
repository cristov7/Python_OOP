from project.album import Album
from typing import List


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            album = [album_info for album_info in self.albums if album_info.name == album_name][0]
        except IndexError:
            return f"Album {album_name} is not found."
        if album.published:   # if album.published == True:
            return "Album has been published. It cannot be removed."
        else:
            self.albums.remove(album)
            return f"Album {album_name} has been removed."

    def details(self) -> str:
        album_details = "\n".join([album_info.details() for album_info in self.albums])
        return f"Band {self.name}" \
               f"\n{album_details}"
