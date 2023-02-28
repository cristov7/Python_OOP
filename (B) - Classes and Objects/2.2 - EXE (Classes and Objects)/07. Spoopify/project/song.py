class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self) -> str:
        song_name = self.name
        song_length = self.length
        return f"{song_name} - {song_length}"
