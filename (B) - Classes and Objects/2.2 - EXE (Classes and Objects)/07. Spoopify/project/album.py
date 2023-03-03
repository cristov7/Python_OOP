from typing import Tuple, List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):   # (song_objects)
        self.name = name
        self.songs: List[Song] = list(*songs)   # [song_objects]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song.single:   # if song.single == True:
            song_name = song.name
            return f"Cannot add {song_name}. It's a single"
        elif self.published:   # elif self.published == True:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:   # elif song.single == False and self.published == False and song not in self.songs:
            self.songs.append(song)
            song_name = song.name
            name = self.name
            return f"Song {song_name} has been added to the album {name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:   # if self.published == True:
            return "Cannot remove songs. Album is published."
        else:   # elif self.published == False:
            song_object_list = [song_object for song_object in self.songs
                                if song_object.name == song_name]
            if song_object_list:   # if len(song_object_list) > 0:
                song_object = song_object_list[0]
                self.songs.remove(song_object)
                album_name = self.name
                return f"Removed song {song_name} from album {album_name}."
            else:   # elif len(song_object_list) == 0:
                return "Song is not in the album."

    def publish(self) -> str:
        name = self.name
        if self.published:   # if self.published == True:
            return f"Album {name} is already published."
        else:   # elif self.published == False:
            self.published = True
            return f"Album {name} has been published."

    def details(self) -> str:
        name = self.name
        songs_info = "\n".join([f"== {song_object.get_info()}"
                                for song_object in self.songs])
        return f"Album {name}" \
               f"\n{songs_info}"
