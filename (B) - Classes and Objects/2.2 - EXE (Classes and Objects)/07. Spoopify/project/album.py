from project.song import Song
from typing import Tuple, List


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs: List[Song] = list(*songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song.single:   # if song.single == True:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:   # if self.published == True:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        try:
            song = [song_info for song_info in self.songs if song_info.name == song_name][0]
        except IndexError:
            return "Song is not in the album."
        if self.published:   # if self.published == True:
            return "Cannot remove songs. Album is published."
        else:
            self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:   # if self.published == True:
            return f"Album {self.name} is already published."
        else:   # elif self.published == False:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_info = "\n".join([f"== {song_info.get_info()}" for song_info in self.songs])
        return f"Album {self.name}" \
               f"\n{songs_info}"
