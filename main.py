import create_playlist
import get_client
import get_my_playlists
import get_liked_videos
from get_items_from_playlist import getPlaylistItems, song_info
import search_for_item
from secrets import spotify_token

import youtube_dl
import requests

import json

class main:

    def __init(self):
        self.song_info = {}


    def add_song_to_playlist(self):
        # populate dictionary of playlist songs
        getPlaylistItems()
        print('main: ', song_info.items())

        #collet all song uris
        uris = [info["spotify_uri"]
            for song, info in song_info.items()]

        #create playlist
        playlist_id = create_playlist.createPlaylist()

        #add songs
        payload = json.dumps(uris)
        endpoint = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

        response = requests.post(
            endpoint,
            data = payload, 
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        json_response = response.json()

        return json_response

if __name__ == '__main__':
    cp = main()
    cp.add_song_to_playlist()