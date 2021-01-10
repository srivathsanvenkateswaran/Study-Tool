'''
To Do Task
Study with Me Videos
Study Music

Countdown timer
Google Search
'''

def studyMusic():
    import pafy
    import vlc
    import time
    # Importing required modules 
    url = 'https://www.youtube.com/watch?v=VIvRmTRtAxQ'
    # Youtube URL 
    audio = pafy.new(url)
    # Create a new Audio Object 
    best = audio.getbestaudio()
    # get the best version of Audio from the audio object 
    playurl = best.url
    # Get the URL from the best stream 
    Instance = vlc.Instance()
    # creating a vlc instance 
    player = Instance.media_player_new()
    # Creating a new Media Player 
    Media = Instance.media_new(playurl)
    # Creating a new media Instance 
    Media.get_mrl()
    # Store the MRL inside the Media Instance 
    player.set_media(Media)
    # Set the Media inside the Media Player 
    player.play()
    # Play the Media Player 
    # player.set_pause(1)   [WE CAN MAKE A PAUSE BUTTON AND THEN PAUSE THE AUDIO PLAYBACK USING THIS COMMAND]
    time.sleep(audio.length + 1)
    # waiting till the audio finishes playing. 

#To Do Task code link available in Discord Server

def playVideosInFolder(filePath):
    # Needs improvement
    import os
    import vlc
    import time
    from moviepy.editor import VideoFileClip
    os.chdir(filePath)
    # Changing into the directory which contains all the videos. 
    dir = os.listdir(os.getcwd())
    # getting the names of all the videos present inside the directory 
    dir.sort()
    # sorting the videos according to their names. [OPTIONAL]
    for video in dir:
        # Loop through each video inside the directory 
        videoDuration = VideoFileClip(video).duration
        # Getting the duration of the current video because it will be helpful to halt the code till the video finishes playing 
        videoDuration = int(videoDuration) + 1
        # Adjusting the value obtained after converting float into int
        print(f'Going to play {video} of duration {videoDuration}')
        # Printing the name of the video which is about to play [For Testing purpose]
        vlc_instance = vlc.Instance()
        # creating a vlc instance
        player = vlc_instance.media_player_new()
        # creating a media player
        media = vlc_instance.media_new(video)
        # creating a media
        player.set_media(media)
        # setting media to the player
        player.play()
        # play the video
        time.sleep(videoDuration)
        # wait time for the video to finish playing
        print(f'Played {video}')
        # print in terminal about the video played. [Testing]

def studyWithMeVideos(user):
    import freeTime
    import os
    filePath = f'/home/{user}/Videos'
    os.chdir(filePath)
    # this is the path where the study with me videos will be saved. 
    try:
        dir = os.listdir(filePath + '/StudyWithMeVideos')
        # This will throw an error when there is not directory. If there is no directory, then there will be no videos and hence, we will download the videos. [The Download function will create a directory in the playlist name]
    except FileNotFoundError:
        studyWithMePlaylistLink = 'https://www.youtube.com/playlist?list=PL0TgZHwr16z_x7loDhs3vzzgo_j-6FetI'
        # We will update the string with a playlist which contains a lot of Study With Me videos. 
        freeTime.downloadPlaylistFromYoutube(studyWithMePlaylistLink, 'srivathsan')
        # This will download the Playlist under the specified path. 
    playVideosInFolder(filePath+'/StudyWithMeVideos')
    #This will play the given file

def streamStudyWithMeVideos():
    import os
    from pytube import Playlist 
    import freeTime
    # importing required modules 
    studyWithMePlaylistLink = 'https://www.youtube.com/playlist?list=PL0TgZHwr16z_x7loDhs3vzzgo_j-6FetI'
    # StudyWithMe videos playlist link 
    try:
        playlistObject = Playlist(studyWithMePlaylistLink)
        # This creates a new playlist object 
    except:
        print("Error creating playlist object")
    print("Starting to Play videos in ", playlistObject.title)
    for videoURL in playlistObject.video_urls:
        freeTime.streamYoutubeVideos(videoURL)
        # This will call streamYoutubeVideos function for each video and save it streamed using VLC Media Player. 
    









