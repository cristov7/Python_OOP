from project.player import Player
from typing import List


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []   # [players of the guild]

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != Player.NOT_IN_OTHER_GUILD_WORD:
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player = [player_info for player_info in self.players if player_info.name == player_name][0]
        except IndexError:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player)
        player.guild = Player.NOT_IN_OTHER_GUILD_WORD
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        players_info = "\n".join(player_info.player_info() for player_info in self.players)
        return f"Guild: {self.name}" \
               f"\n{players_info}"
