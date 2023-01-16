from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_read_single_pokemon_details():
    response = client.get("/pokemon/v1/details/ditto")
    assert response.status_code == 200
    assert response.json() == {
        'base_happiness': 50,
        'color': 'purple',
        'height': 3,
        'moves': ['transform'],
        'name': 'ditto',
        'weight': 40
    }

def test_read_invalid_single_pokemon_details():
    response = client.get("/pokemon/v1/details/fakepokemon")
    assert response.status_code == 404

def test_read_pokemon_list_details():
    response = client.post("/pokemon/v1/collection/details/", json={
        "names": ["ditto", "pikachu", "squirtle"]
    })
    assert response.status_code == 200
    res = response.json()
    assert res['median'] == 50
    assert res['mean'] == 50
    assert res['average'] == 50
    assert len(res['pokemon']) == 3

def test_read_invalid_pokemon_list_details():
    response = client.post("/pokemon/v1/collection/details/", json={
        "names": ["fakepokemon1", "fakepokemon2", "fakepokemon3"]
    })
    assert response.status_code == 404
