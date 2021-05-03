"""
Youtube Video Downloader
Youtube Playlist Downloader 
Internet Speed Checker
Recent News [API]
Youtube Player

next update:
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
    downloadInternetSpeed = speedtestObject.download()
    downloadInternetSpeed = downloadInternetSpeed / 1000000
    print('Upload Speed: ', round(downloadInternetSpeed, 2), ' Mb per second')
    print('Testing your Upload Speed....')
    uploadInternetSpeed = speedtestObject.upload()
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

def rockPaperScissor(userOption, computerOption):
    global userPoints, computerPoints
    if(userOption==computerOption):
        winner='Match Drawn'
    else:
        if(userOption=='Rock'):
            if(computerOption=='Paper'):
                winner='Computer Won'
                computerPoints+=1
            else:
                winner='You Won'
                userPoints+=1
        elif(userOption=='Paper'):
            if(computerOption=='Rock'):
                winner='You Won'
                userPoints+=1
            else:
                winner='Computer Won'
                computerPoints+=1
        else:
            if(computerOption=='Rock'):
                winner='Computer Won'
                computerPoints+=1
            else:
                winner='You Won'
                userPoints+=1
    return winner

def snakeWaterGun(userOption, computerOption):
    global userPoints, computerPoints
    if(userOption==computerOption):
        winner='Match Drawn'
    else:
        if(userOption=='Snake'):
            if(computerOption=='Water'):
                winner='You Won'
                userPoints+=1
            else:
                winner='Computer Won'
                computerPoints+=1
        elif(userOption=='Water'):
            if(computerOption=='Snake'):
                winner='Computer Won'
                computerPoints+=1
            else:
                winner='You Won'
                userPoints+=1
        else:
            if(computerOption=='Snake'):
                winner='You Won'
                userPoints+=1
            else:
                winner='Computer Won'
                computerPoints+=1
    return winner

def invokeSnakeWaterGun():
    import random
    numberOfIterations=int(input("Enter the Number of Times you want to play: "))
    iterationNumber=0
    userPoints, computerPoints = 0,0
    nameList = ['Snake','Water','Gun']
    while(iterationNumber<numberOfIterations):
        userOption = int(input('Enter 1 for Snake, 2 for Water, 3 for Gun: '))
        if(userOption==1):
            userOption='Snake'
        elif(userOption==2):
            userOption='Water'
        else:
            userOption='Gun'
        computerOption=random.choice(nameList)
        winner=snakeWaterGun(userOption, computerOption)
        print(f"You chose {userOption}\nComputer chose {computerOption}\n{winner} this battle\n\n")
        print(f"Your Points till now: {userPoints}\nComputer Points till now: {computerPoints}")
        iterationNumber+=1
    if(userPoints>computerPoints):
        print("\n\nYou won the game")
    elif(computerOption>userPoints):
        print("\n\nComputer won the game")
    else:
        print("\n\nMatch Drawn")

def invokeRockPaperScissor():
    import random
    numberOfIterations=int(input("Enter the Number of Times you want to play: "))
    iterationNumber=0
    userPoints, computerPoints = 0,0
    nameList = ['Rock','Paper','Scissor']
    while(iterationNumber<numberOfIterations):
        userOption = int(input('Enter 1 for Rock, 2 for Paper, 3 for Scissor: '))
        if(userOption==1):
            userOption='Rock'
        elif(userOption==2):
            userOption='Paper'
        else:
            userOption='Scissor'
        computerOption=random.choice(nameList)
        winner=rockPaperScissor(userOption, computerOption)
        print(f"You chose {userOption}\nComputer chose {computerOption}\n{winner}\n\n")
        print(f"Your Points till now: {userPoints}\nComputer Points till now: {computerPoints}")
        iterationNumber+=1
    if(userPoints>computerPoints):
        print("\n\nYou won the game")
    elif(computerOption>userPoints):
        print("\n\nComputer won the game")
    else:
        print("\n\nMatch Drawn")
    
def snakesGame():
    import curses
    from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
    from random import randint


    curses.initscr()
    # Initializing the curses. 
    win = curses.newwin(20, 60, 0, 0)
    
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT                                                    # Initializing values
    score = 0

    snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
    food = [10,20]                                                     # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27:                                                   # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
        win.timeout(int(150 - (len(snake)/5 + len(snake)/10)%120))          # Increases the speed of Snake as its length increases
        
        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event 


        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # If snake crosses the boundaries, make it enter from the other side
        if snake[0][0] == 0: snake[0][0] = 18
        if snake[0][1] == 0: snake[0][1] = 58
        if snake[0][0] == 19: snake[0][0] = 1
        if snake[0][1] == 59: snake[0][1] = 1

        # Exit if snake crosses the boundaries (Uncomment to enable)
        #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

        # If snake runs over itself
        if snake[0] in snake[1:]: break

        
        if snake[0] == food:                                            # When snake eats the food
            food = []
            score += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snake: food = []
            win.addch(food[0], food[1], '*')
        else:    
            last = snake.pop()                                          # [1] If it does not eat the food, length decreases
            win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], '#')
        
    curses.endwin()
    print("\nScore - " + str(score))

