from typing import List, Union, Dict
from pydantic import BaseModel


class PokemonDetails(BaseModel):
    name: str
    height: int
    weight: int
    color: str
    moves: List[str]
    base_happiness: int


class PokemonCollection(BaseModel):
    average: int
    mean: int
    median: int
    pokemon: List[PokemonDetails]

    class Config:
        pass


class PokemonList(BaseModel):
    names: List[str]