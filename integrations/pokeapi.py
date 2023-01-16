from fastapi import HTTPException

from pokemon.api_models import PokemonDetails

from random import sample as random_sample

import requests


class PokeAPI:
    """Interface for https://pokeapi.co
    """
    def __init__(self):
        self.base_address = "https://pokeapi.co/api/v2/"

    def _get_pokemon_details(self, pokemon_name: str):
        req = requests.get(f"{self.base_address}/pokemon/{pokemon_name}")
        if not req.status_code == 200:
            return
        return req.json()
    
    def _get_species_details(self, id: int):
        req = requests.get(f"{self.base_address}/pokemon-species/{id}")
        if not req.status_code == 200:
            return
        return req.json()

    def pokemon_details(self, name: str):
        pokemon_details = self._get_pokemon_details(name)

        if not pokemon_details:
            raise HTTPException(404, "Not found")

        species_details = self._get_species_details(pokemon_details['id'])

        name = pokemon_details['name']
        height = pokemon_details['height']
        weight = pokemon_details['weight']

        # Collect a total of two random move names
        moves = pokemon_details['moves']
        if len(moves) > 2:
            moves = random_sample(moves, 2)

        move_names = []
        for move_dict in moves:
            move_names.append(move_dict['move']['name'])

        color = species_details['color']['name']
        base_happiness = species_details['base_happiness']
        
        response_model = PokemonDetails(
            name=name,
            height=height,
            weight=weight,
            color=color,
            moves=move_names,
            base_happiness=base_happiness
        )

        return response_model
