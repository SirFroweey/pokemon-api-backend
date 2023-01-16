import unittest

from fastapi import HTTPException

from backend.integrations.pokeapi import PokeAPI


class PokeAPI_Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.api = PokeAPI()
        return super().setUp()

    def test_pokemon_exists(self):
        api_response = self.api.pokemon_details('ditto')
        self.assertEqual(api_response.name, 'ditto')
        self.assertEqual(api_response.height, 3)
        self.assertEqual(api_response.weight, 40)
        self.assertEqual(api_response.color, 'purple')
        self.assertListEqual(api_response.moves, ['transform'])
        self.assertEqual(api_response.base_happiness, 50)

    def test_test_pokemon_does_not_exist(self):
        with self.assertRaises(HTTPException):
            self.api.pokemon_details('invalidpokemonname')

if __name__ == '__main__':
    unittest.main()
