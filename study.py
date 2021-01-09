'''
To Do Task
Study with Me Videos [Need to improve playVideo]

Study Music
Countdown timer
Google Search
'''
studyWithMeVideoFlag = 0

def studyMusic():
    pass

#To Do Task code link available in Discord Server

def playVideo(filePath):
    # Needs improvement
    import os
    import cv2
    import numpy
    dir = os.listdir(filePath)
    for video in dir:
        captureObject = cv2.VideoCapture(filePath+'\\'+video)
        if(captureObject.isOpened() == False):
            print('Error opening video')
        
        while(captureObject.isOpened()):
            ret, frame = captureObject.read()
            if(ret == True):
                cv2.imshow('Frame', frame)
                if(cv2.waitKey(25) & 0xFF == ord('q')):
                    break
            else:
                break
        captureObject.release()
        cv2.destroyAllWindows()

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



studyWithMeVideos()  

        









