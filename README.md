# Back-end Project

Demo project for active candidacy!

This project provides a total of two API endpoints and has been shipped with the ability to integrate with a PSQL database instance if the need arises.

## Installation
1. Create a _python3_ virtualenv named `.venv` or your preferred name via `python3 -m virtualenv .venv`.
2. Activate the *virtualenv* and install project dependencies via `pip install -r requirements.txt` inside the root folder.
3. Run the app via `uvicorn app.main:app --reload` from within' the projects root folder.
4. Point your web browser or Postman client to `http://127.0.0.1:8000/pokemon/v1/details/ditto` to begin using the API.

## Automatic tests
1. CD into root project directory
2. Run `pytest tests/`.

```
$ pytest tests/                            
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/test/Desktop/poke_demo/backend
collected 6 items                                                              

tests/test_pokeapi.py ..                                                 [ 33%]
tests/test_v1_api.py ....                                                [100%]

============================== 6 passed in 2.51s ===============================
```

## Endpoints

GET - `http://127.0.0.1:8000/pokemon/v1/details/{pokemon}`
> Retrieves the details pertaining to the given pokemon.
- `pokemon` is a string denoting the pokemon to retrieve details for.

POST - `http://127.0.0.1:8000/pokemon/v1/collection/details/`
> Retrieves a collection of details for the given list of pokemon. Requires a JSON payload.
- `names` is an array of strings denoting the list of pokemon to retrieve details for.

## Usage examples
![alt text](https://i.imgur.com/jZcWyBb.png)

![alt text](https://i.imgur.com/5rASuxK.png)
