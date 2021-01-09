'''
To Do Task
Study with Me Videos [Need to improve playVideo]

Study Music
Countdown timer
Google Search
'''

def studyMusic():
    pass

#To Do Task code link available in Discord Server

def playVideosInFolder(filePath):
    # Needs improvement
    import os
    import vlc
    import time
    os.chdir(filePath)
    dir = os.listdir(os.getcwd())
    dir.sort()
    video = dir[0]
    # creating a vlc instance
    vlc_instance = vlc.Instance()
    # creating a media player
    player = vlc_instance.media_player_new()
    # creating a media
    media = vlc_instance.media_new(video)
    # setting media to the player
    player.set_media(media)
    # play the video
    player.play()
    # wait time
    time.sleep(50)
    # getting the duration of the video
    duration = player.get_length()
    # printing the duration of the video
    print("Duration : " + str(duration))

        # PROBLEM:   The video plays but there is no audio and also we can't control the video [Pause, Play etc]. 


def studyWithMeVideos():
    import freeTime
    import os
    filePath = '/home/srivathsan/Videos'
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
    playVideo(filePath)
    #This will play the given file



# studyWithMeVideos()  
playVideosInFolder('/home/srivathsan/Videos')
        









