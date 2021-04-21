#!/usr/bin/python3

import tkinter

#user defined modules

#module - 1
import assign
'''
functions of assign.py:

1.def TaskNotifier(site, time, task) - popup required in tkinter
2.def cropper(path) - path is path of image to crop
3.def ConvertToPdf(filename) - filename of pdf - converts all cropped image -> pdf
4.def ScreenRecorder(filename) - screenrecorder - filename of output file

'''

#module - 2
import compUsage
'''
functions of compUsage.py

1.def clearRecycleBin() - clears recycle bin - no args
2.def sortAndstoreFiles(path) - path is the path of the folder where all mixed files present
3.def shorten(url) - shorten the url
4.def unshorten(url) - unshorten the url

'''

#module - 3
import freeTime
'''
functions of freeTime.py

1.def downloadVideoFromYoutube(videoLink, filePath) - path to store the downloaded file
2.def downloadPlaylistFromYoutube(playlistLink, user) - user is the user name of linux
3.def checkInternetSpeed() - Internet speedchecker
4.def getNews(apiToken) - gnews api key
5.def streamYoutubeVideos(videoURL) - streams yt video
6.def snakesGame() - snake game

'''

#module - 4
import improve
'''
functions of improve.py

1.def SafeEyes(command) - commands - enable,disable,settings,status

'''

#module - 5
import office
'''
functions of office.py

1.def createPDF(pdfFileName, textToBeEntered) - text will be passed as str
2.def txtToPDF(txtFileName) - name of text file to convert to pdf
3.def docxToPDF(docxFileName) - name of docx file to convert to pdf
4.def docxToTxt(docxFileName) - name of docx file to convert as txt
5.def pdfToDocx(pdfFileName) - name of pdf file to convert as docx
6.def pptToPDF(pptFileName, pdfFileName, formatType = 32) - file names of ppt and pdf
7.def pdfToTxt(pdfFileName) - file name of pdf to convert as text
8.def excelToPDF(excelFileName) - file name of excel
9.def unZipFile(zipFileName) - unzip the zip file - name of zip
10.def compressToZip(folderName) - folder to be zipped path
11.def openImage(imageName) - open image in path
12.def compressImage(imageName) - compress the size of the image

'''

#module - 6
import study
'''
functions of study.py

1.def studyMusic() - plays study music
2.def playVideosInFolder(filePath) - plays local videos in path
3.def studyWithMeVideos(user) - user - username
4.def streamStudyWithMeVideos() - plays study with me videos

'''

#################################################################

