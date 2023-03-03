from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []   # [pokemon objects]

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            pokemon_name = pokemon.name
            pokemon_health = pokemon.health
            return f"Caught {pokemon_name} with health {pokemon_health}"

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon_objects_list = [pokemon for pokemon in self.pokemons if pokemon.name == pokemon_name]
        if pokemon_objects_list:
            pokemon = pokemon_objects_list[0]
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self) -> str:
        trainer_name = self.name
        amount_of_pokemon_caught = len(self.pokemons)
        pokemon_details = "\n".join([f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons])
        return f"Pokemon Trainer {trainer_name}" \
               f"\nPokemon count {amount_of_pokemon_caught}" \
               f"\n{pokemon_details}"
