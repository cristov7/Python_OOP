from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []   # [player_objects]

    def assign_player(self, player: Player) -> str:   # player == player_object
        player_name = player.name
        if player in self.players:
            return f"Player {player_name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player_name} is in another guild."
        else:   # elif player not in self.players and player.guild == "Unaffiliated":
            self.players.append(player)
            guild_name = self.name
            player.guild = self.name
            return f"Welcome player {player_name} to the guild {guild_name}"

    def kick_player(self, player_name: str) -> str:
        players_objects_list = [player_object for player_object in self.players
                                if player_object.name == player_name]
        if players_objects_list:   # if len(players_objects_list) > 0:
            player_object = players_objects_list[0]
            self.players.remove(player_object)
            player_object.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        else:   # elif len(players_objects_list) == 0:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        guild_name = self.name
        players_info = "\n".join([player_object.player_info()
                                  for player_object in self.players])
        return f"Guild: {guild_name}" \
               f"\n{players_info}"
