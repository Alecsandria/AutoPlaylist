import json
import requests

from secrets import spotify_token

def searchForItem(artist, song_name):
    endpoint = "https://api.spotify.com/v1/search"
    params = {
        "q": "{} {}".format(
            artist,
            song_name
        ),
        "type": "track,artist"
    }
        
    response = requests.get(
        endpoint,
        params = params,
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )

    json_response = response.json()
    # print(json_response)
    songs = json_response["tracks"]["items"]

    return songs[0]["uri"]