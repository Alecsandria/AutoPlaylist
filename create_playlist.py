import json
import requests

from secrets import spotify_user_id, spotify_token

def createPlaylist():
    payload = json.dumps ({
            "name": "YouTube Vids",
            "description": "All Liked Videos from YouTube",
            "public": False
    })

    endpoint = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)

    response = requests.post(
        endpoint,
        data = payload,
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )

    json_response = response.json()
    print(json_response)
    return json_response["id"]

if __name__ == '__main__':
    createPlaylist()