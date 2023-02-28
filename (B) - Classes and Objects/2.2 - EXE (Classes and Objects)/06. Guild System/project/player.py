from typing import Dict


class Player:
    NOT_IN_OTHER_GUILD_WORD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}   # {skills : mana cost}
        self.guild = Player.NOT_IN_OTHER_GUILD_WORD

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self) -> str:
        skills_info = "\n".join([f"==={skill_name} - {skill_mana_cost}"
                                 for skill_name, skill_mana_cost in self.skills.items()])
        return f"Name: {self.name}" \
               f"\nGuild: {self.guild}" \
               f"\nHP: {self.hp}" \
               f"\nMP: {self.mp}" \
               f"\n{skills_info}"
