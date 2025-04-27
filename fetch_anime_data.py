import requests
import pandas as pd
import sqlite3
import os

def fetch_anime_data(query="naruto"):
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=20"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

    data = response.json().get('data', [])
    anime_list = []
    for anime in data:
        anime_list.append({
            'title': anime.get('title', 'N/A'),
            'type': anime.get('type', 'N/A'),
            'episodes': anime.get('episodes', 'N/A'),
            'score': anime.get('score', 'N/A'),
            'studio': anime['studios'][0]['name'] if anime.get('studios') else 'N/A',
            'year': anime.get('year', 'N/A')
        })
    return anime_list

def save_to_database(anime_list, db_name="anime.db"):
    if not anime_list:
        print("No anime data to save.")
        return
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame(anime_list)
    df.to_sql("anime", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Saved {len(anime_list)} anime entries to {db_name}")

def main():
    query = input("Enter an anime to search: ")
    anime_list = fetch_anime_data(query)
    save_to_database(anime_list)

if __name__ == "__main__":
    main()
