from fastapi import APIRouter, HTTPException
from http.client import HTTPException

from ..api_models import PokemonCollection, PokemonDetails, PokemonList
from ..utils import get_average, get_mean, get_median
from integrations.pokeapi import PokeAPI


poke_api = PokeAPI()
router = APIRouter()


@router.get("/details/{name}")
def get_pokemon_details(name: str):
    return poke_api.pokemon_details(name)


@router.post("/collection/details/")
def pokemon_collection_details(pokemon_list: PokemonList):
    pokemon_list_response = []
    base_happiness_list = []

    for pokemon_name in pokemon_list.names:
        details = poke_api.pokemon_details(pokemon_name)
        pokemon_list_response.append(details)
        base_happiness_list.append(details.base_happiness)

    if not len(pokemon_list_response):
        return None

    collection = PokemonCollection(
        pokemon=pokemon_list_response,
        average=get_average(base_happiness_list),
        mean=get_mean(base_happiness_list),
        median=get_median(base_happiness_list)
    )

    return collection
