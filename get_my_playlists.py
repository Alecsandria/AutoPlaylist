import get_client

def getMyPlaylists(playlistName):
    youtube_client = get_client.getYouTubeClient()

    request = youtube_client.playlists().list(
        part="contentDetails,snippet,id",
        mine=True
    )
    response = request.execute()

    playlists = response["items"]

    for playlist in playlists:
        playlistTitle = playlist["snippet"]["title"]
        playlistId = playlist["id"]

        if(playlistTitle == playlistName):
            print("playlist items", playlistTitle)
            print("playlistId", playlistId)
            break
        
    return playlistId

if __name__ == '__main__':
    getMyPlaylists("Lit Tunes")