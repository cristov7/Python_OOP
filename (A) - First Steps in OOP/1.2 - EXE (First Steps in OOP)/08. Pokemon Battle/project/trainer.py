from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            pokemon = [x for x in self.pokemons if x.name == pokemon_name][0]
            # pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        except IndexError:
        # except StopIteration:
            return "Pokemon is not caught"
        # try:
        #     pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
        #     self.pokemons.remove(pokemon)
        #     return f"You have released {pokemon_name}"
        # except StopIteration:
        #     return "Pokemon is not caught"

    def trainer_data(self) -> str:
        output_list = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        convert_pokemons_list = [f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons]
        output_list.extend(convert_pokemons_list)
        return "\n".join(output_list)
        # pokemons_data = "\n".join(f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons)
        # return f"Pokemon Trainer {self.name}" \
        #        f"\nPokemon count {len(self.pokemons)}" \
        #        f"\n{pokemons_data}"
