import get_client

def getLikedVideos():
    youtube_client = get_client.getYouTubeClient()
    request = youtube_client.videos().list(
        part="snippet,contentDetails,statistics",
        myRating="like"
    )

    response = request.execute()
    print(response)

if __name__ == '__main__':
    getLikedVideos()