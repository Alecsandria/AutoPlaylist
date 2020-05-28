import get_client
import get_my_playlists
import search_for_item

import youtube_dl

song_info = {}

def getPlaylistItems():
    youtube_client = get_client.getYouTubeClient()

    request = youtube_client.playlistItems().list(
        part="contentDetails,snippet",
        playlistId="{}".format(get_my_playlists.getMyPlaylists("Lit Tunes"))
    )
    response = request.execute()

    songs = response["items"]
    

    for song in songs:
        video_title = song["snippet"]["title"]
        video_id = song["contentDetails"]["videoId"]
        youtube_url = "https://www.youtube.com/watch?v={}".format(video_id)

        # use youtube_dl to collect the song name & artist name
        ydl = youtube_dl.YoutubeDL({'nocheckcertificate': True})
        with ydl:
            video = ydl.extract_info(
                youtube_url, 
                download=False
            )
        # print('extract_info: ', video)
        song_name = video["track"]
        artist_name = video["artist"]
        print('song_name: ', song_name)

        if ',' in artist_name:
            artist_name = artist_name.replace(',', '')
        print('artist_name', artist_name)

        song_info[video_title] = {
            "youtube_url": youtube_url,
            "song_name": song_name,
            "artist_name": artist_name,
            "spotify_uri": search_for_item.searchForItem(artist_name, song_name)
        }
    print('song_info: ', song_info)
    return(song_info)