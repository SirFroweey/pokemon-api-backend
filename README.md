# Back-end Project

Demo project for active candidacy!

## Installation
1. Create a _python3_ virtualenv named `.venv` or your preferred name via `python3 -m virtualenv .venv`.
2. Activate the *virtualenv* and install project dependencies via `pip install -r requirements.txt` inside the root folder.
3. Run the app via `uvicorn app.main:app --reload` from within' the projects root folder.

## Automatic tests
1. CD into root project directory
2. Run `pytest tests/`.

## Endpoints

GET - `http://127.0.0.1:8000/pokemon/v1/details/{pokemon}`
> Retrieves the details pertaining to the given pokemon.
- `pokemon` is a string denoting the pokemon to retrieve details for.

POST - `http://127.0.0.1:8000/pokemon/v1/collection/details/`
> Retrieves a collection of details for the given list of pokemon. Requires a JSON payload.
- `names` is an array of strings denoting the list of pokemon to retrieve details for.
