from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}   # {skill_name : mana_cost}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills.keys():
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            player_name = self.name
            return f"Skill {skill_name} added to the collection of the player {player_name}"

    def player_info(self) -> str:
        player_name = self.name
        guild_name = self.guild
        hp = self.hp
        mp = self.mp
        skill_info = "\n".join([f"==={skill_name} - {mana_cost}"
                                for skill_name, mana_cost in self.skills.items()])
        return f"Name: {player_name}" \
               f"\nGuild: {guild_name}" \
               f"\nHP: {hp}" \
               f"\nMP: {mp}" \
               f"\n{skill_info}"
