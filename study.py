'''
To Do Task
Study with Me Videos

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
    from moviepy.editor import VideoFileClip
    os.chdir(filePath)
    dir = os.listdir(os.getcwd())
    dir.sort()
    for video in dir:
        videoDuration = VideoFileClip(video).duration
        videoDuration = int(videoDuration) + 1
        print(f'Going to play {video} of duration {videoDuration}')
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
        # wait time
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
    pass









