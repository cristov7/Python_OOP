from typing import List
from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE: int = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List = [[] for page in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for page_list_index in range(len(self.photos)):
            page = self.photos[page_list_index]
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[page_list_index].append(label)
                page_number = page_list_index + 1
                slot_number = len(self.photos[page_list_index])
                return f"{label} photo added successfully on page {page_number} slot {slot_number}"
            else:
                continue
        return "No more free slots"

    def display(self) -> str:
        separation_dashes = "-" * 11
        marked_photo = "[]"
        photo_album_list = [separation_dashes]
        for page_list in self.photos:
            count_photos = len(page_list)
            marked_photos = " ".join([marked_photo
                                      for photo in range(count_photos)])
            full_page = marked_photos + "\n" + separation_dashes
            photo_album_list.append(full_page)
        photo_album = "\n".join(photo_album_list)
        return f"{photo_album}"


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
