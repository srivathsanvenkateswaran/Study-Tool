"""
Youtube Video Downloader
Youtube Playlist Downloader 
Internet Speed Checker
Recent News [API]
Youtube Player

Games
Whatsapp Forward Bot
"""

def downloadVideoFromYoutube(videoLink, filePath):
    # In the final product, we will also get the resolution as an argument [Input from the user]
    from pytube import YouTube
    try:
        youtubeObject = YouTube(videoLink)
        # This will create a Youtube object from the video. 
    except:
        print("Connection Error!")
    videoStreamObjectsArray = youtubeObject.streams.filter(progressive = True)
    # This gets the streams from Youtube Object and then filters only those which has both video and audio codec [Progressive Stream ]
    # Youtube Supports DASH Streaming [Adaptive Stream] and hence, it has separate Audio or Video codec and then merges and plays them 
    videoStreamObjectsArray.order_by('resolution')
    # This sorts the video streams by resolution
    videoStreamObject = videoStreamObjectsArray[-1]
    # This will give the first object from the Streams available
    try:
        videoStreamObject.download(filePath)
        # here we download the video and then save it with the given file path 
    except:
        print("Error")

def downloadPlaylistFromYoutube(playlistLink, user):
    import os
    # Importing os to create a directory in the name of the playlist 
    from pytube import Playlist 
    filePath = '/home/' + user + '/Videos'
    os.chdir(filePath)
    try:
        playlistObject = Playlist(playlistLink)
        # This creates a new playlist object 
    except:
        print("Error creating playlist object")
    filePath = filePath + "/" + playlistObject.title
    # This will append the Playlist Title with the pre mentioned file path 
    os.makedirs(filePath)
    # This will create A folder with the name of the playlist 
    print("Downloading ", playlistObject.title)
    for videoURL in playlistObject.video_urls:
        downloadVideoFromYoutube(videoURL, filePath)
        # This will call downloadVideoFromYoutube function for each video and save it inside the newly created function. 
    print("Downloaded ", playlistObject.title) 

def checkInternetSpeed():
    # The Choice is to choose between upload speed, download speed and ping count. We will pass the choice integer based on the button choosed by the user in GUI. 
    import speedtest 
    speedtestObject = speedtest.Speedtest()
    print('Testing your Download Speed....')
    # Instantiating a speedtest object 
    downloadInternetSpeed = speedtestObject.upload()
    downloadInternetSpeed = downloadInternetSpeed / 1000000
    print('Upload Speed: ', round(downloadInternetSpeed, 2), ' Mb per second')
    print('Testing your Upload Speed....')
    uploadInternetSpeed = speedtestObject.download()
    uploadInternetSpeed = uploadInternetSpeed / 1000000
    print('Download Speed: ', round(uploadInternetSpeed, 2), ' Mb per second')
    print('Testing your Ping....')
    serverNames = []
    speedtestObject.get_servers(serverNames)
    print('Your Ping is: ', speedtestObject.results.ping, ' ms')

def getNews(apiToken):
    import requests
    # Importing request module 
    newsAPIUrl = f'https://gnews.io/api/v4/search?q=example&lang=en&country=in&max=10&token={apiToken}'
    # this is the url for API request 
    response = requests.get(newsAPIUrl)
    # This will get the response from the API 
    if(response.status_code == 200):
        # The script will parse the JSON if the response code is 200. 
        jsonResponse = response.json()
        # Get the json format from the response 
        jsobArticlesList = jsonResponse['articles']
        # Fetch the list of articles from the jsonResponse
        articlesList = []
        # creating an empty list which we will use to add all the articles 
        for jsonArticle in jsobArticlesList:
            articleObject = [
                jsonArticle['title'],
                jsonArticle['description'],
                jsonArticle['url']
            ]
            #Here, Each article has Title, Description and URL in 0, 1, 2 index respectively. 
            articlesList.append(articleObject)
            # Finally, we add the articleObject to the articlesList.
    else:
        print("Error: Response Code : ", response.status_code)
    return articlesList

def streamYoutubeVideos(videoURL):
    import pafy
    import vlc
    import time
    # Importing the required modules 
    video = pafy.new(videoURL)
    # creating a pafy video object 
    videoDuration = video.length
    # get the video duration 
    best = video.getbest()
    # get the best version of the video. 
    playurl = best.url
    # get the url of the video 
    Instance = vlc.Instance()
    # create a vlc instance
    player = Instance.media_player_new()
    # create a new media player 
    Media = Instance.media_new(playurl)
    # create a new Media Instance 
    Media.get_mrl()
    # Store the MRL inside Media Object 
    player.set_media(Media)
    # Set the Media to the media player 
    player.play()
    # Play the video 
    time.sleep(videoDuration)
    # wait till the video ends 






