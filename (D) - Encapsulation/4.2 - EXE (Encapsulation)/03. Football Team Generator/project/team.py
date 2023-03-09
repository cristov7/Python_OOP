from typing import List
from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []   # [player_objects]

    def add_player(self, player: Player) -> str:   # player == player_object
        name = player.name
        if player in self.__players:
            return f"Player {name} has already joined"
        else:
            self.__players.append(player)
            team_name = self.__name
            return f"Player {name} joined team {team_name}"

    def remove_player(self, player_name: str) -> [object, str]:
        player_objects_list = [player_object for player_object in self.__players
                               if player_object.name == player_name]
        if player_objects_list:
            player_object = player_objects_list[0]
            self.__players.remove(player_object)
            return player_object
        else:
            return f"Player {player_name} not found"
