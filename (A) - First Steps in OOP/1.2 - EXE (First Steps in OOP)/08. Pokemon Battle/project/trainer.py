from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []   # [pokemon objects]

    def add_pokemon(self, pokemon: Pokemon) -> str:   # pokemon == pokemon_object
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:   # elif pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            pokemon_name = pokemon.name
            pokemon_health = pokemon.health
            return f"Caught {pokemon_name} with health {pokemon_health}"

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon_objects_list = [pokemon_object for pokemon_object in self.pokemons
                                if pokemon_object.name == pokemon_name]
        if pokemon_objects_list:   # if len(pokemon_objects_list) > 0:
            pokemon_object = pokemon_objects_list[0]
            self.pokemons.remove(pokemon_object)
            return f"You have released {pokemon_name}"
        else:   # elif len(pokemon_objects_list) == 0:
            return "Pokemon is not caught"

    def trainer_data(self) -> str:
        trainer_name = self.name
        amount_of_pokemon_caught = len(self.pokemons)
        pokemon_details = "\n".join([f"- {pokemon_object.pokemon_details()}"
                                     for pokemon_object in self.pokemons])
        return f"Pokemon Trainer {trainer_name}" \
               f"\nPokemon count {amount_of_pokemon_caught}" \
               f"\n{pokemon_details}"
