import os
import requests
from dotenv import load_dotenv
    


def get_games(api_key):
    url = "https://api.rawg.io/api/games"
    params = {
        "key": api_key,
        "genres": "strategy",
        "page_size": "10",
        "metacritic": "80, 100",
        "tags": "multiplayer"
    }
    response = requests.get(url, params=params)
    games = response.json()["results"]
    return games


def get_screenshots(game_pk, api_key):
    url = f"https://api.rawg.io/api/games/{game_pk}/screenshots"
    params = {
        "key": api_key,
    }
    response = requests.get(url, params=params)
    screenshots = response.json()["results"]
    return screenshots


def get_stores(game_pk, api_key):
    url = f"https://api.rawg.io/api/games/{game_pk}/stores"
    params = {
        "key": api_key,
    }
    response = requests.get(url, params=params)
    stores = response.json()["results"]
    return stores


def main(): 
    load_dotenv()
    api_key = os.getenv("API_KEY")
    games = get_games(api_key)
    for game in games:
        print(f"""
    Название игры: {game["name"]}
    Дата выхода: {game["released"]}
    Ссылка на игру: https://rawg.io/games/{game["slug"]}
    """)
        print("Скриншоты для игры:")
        screenshots = get_screenshots(game["slug"], api_key)
        for screenshot in screenshots:
            print(screenshot["image"])
        print("Где купить:")
        stores = get_stores(game["slug"], api_key)
        for store in stores:
            print(store["url"])



if __name__ == "__main__":
    main()
