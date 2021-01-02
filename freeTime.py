"""
Games
Youtube Video Downloader
Recent News [API]
Youtube Player
Whatsapp Forward Bot
Internet Speed Checker
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

def downloadPlaylistFromYoutube(playlistLink, filePath):
    import os
    # Importing os to create a directory in the name of the playlist 
    from pytube import Playlist 
    try:
        playlistObject = Playlist(playlistLink)
        # This creates a new playlist object 
    except:
        print("Error creating playlist object")
    filePath = filePath + "\\" + playlistObject.title
    # This will append the Playlist Title with the pre mentioned file path 
    os.makedirs(filePath)
    # This will create A folder with the name of the playlist 
    print("Downloading ", playlistObject.title)
    for videoURL in playlistObject.video_urls:
        downloadVideoFromYoutube(videoURL, filePath)
        # This will call each downloadVideoFromYoutube function for each video and save it inside the newly created function. 
    print("Downloaded ", playlistObject.title)   