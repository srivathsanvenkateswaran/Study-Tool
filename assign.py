'''
Task notifier and website alarm
crop images and convert to pdf
screen recorder
image to text
label for assignments
scientific calculator
'''

#Task notifier/alarm
def TaskNotifier(site, time, task):
	import time
	import webbrowser

	Set_Alarm = time
	url = site
	Actual_Time = time.strftime("%I:%M:%S")

	while (Actual_Time != Set_Alarm):
        Actual_Time = time.strftime("%I:%M:%S")
        time.sleep(1)

	if (Actual_Time == Set_Alarm):
		popup(task)

    #popup will open with task given at that time

#function to crop images
def cropper(path):
	import cv2
	import os
	import sys
	import shutil
	from PIL import Image

	if sys.platform == 'linux':
		try:
			os.system('mkdir cropped')
		except:
			shutil.rmtree(os.getcwd+"//cropped")
	elif sys.platform == 'win32':
		try:
			os.system('md cropped')
		except:
			shutil.rmtree(os.getcwd+"//cropped")
	else:
		pass

	refPt = []
	cropping = False
	def click_and_crop(event, x, y, flags, param):

		global refPt, cropping

		if event == cv2.EVENT_LBUTTONDOWN:
			refPt = [(x, y)]
			cropping = True
		elif event == cv2.EVENT_LBUTTONUP:
			refPt.append((x, y))
			poi = open("co-ordinates.txt","w")
			left,top = refPt[0]
			right,bottom = refPt[1]
			poi.write(str(refPt[0][1])+','+str(refPt[1][1])+','+str(refPt[0][0])+','+str(refPt[1][0]))
			poi.close()
			cropping = False
			cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 3)
			cv2.imshow("image", image)


	image = cv2.imread(path)
	clone = image.copy()
	cv2.namedWindow("image", cv2.WINDOW_NORMAL)
	cv2.setMouseCallback("image", click_and_crop)

	while True:

		cv2.imshow("image", image)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("r"):
			image = clone.copy()
		elif key == ord("c"):
			break

	if len(refPt) == 2:
		def filename(i = '1'):
			arr = os.listdir(os.getcwd()+"//cropped")
			if "{}.jpg".format(i) in arr:
				i = int(i)
				i = i + 1
				filename(str(i))
			else:
				return i

		name = str(filename())
		roi = clone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
		cv2.imshow("ROI", roi)
		cv2.imwrite(os.getcwd()+"//cropped//{}.jpg".format(name), roi)
		cv2.waitKey(0)

	cv2.destroyAllWindows()


#converting cropped images to pdf
def ConvertToPdf(filename):
	from PIL import Image
	import os

	'''
	im = Image.open(file)
	im1 = im.convert('RGB')

	open other images and convert and append in list using loop

	imagelist = [im2,im3,im4]
	im1.save('filename.pdf',save_all=True, append_images=imagelist)

	'''

	image1 = Image.open(os.getcwd+"//cropped//1.jpg")
	im1 = image1.convert('RGB')

	arr = os.listdir(os.getcwd + "//cropped")
	arr.pop(0)

	imagelist = []

	for i in arr:
		image = Image.open(os.getcwd+"//cropped//{}".format(i))
		im = image.convert('RGB')
		imagelist.append(im)

	im1.save('{}.pdf'.format(filename), save_all=True, append_images=imagelist)

#screen_recorder
def ScreenRecorder(filename):
	import pyautogui
	import cv2
	import numpy as np

	width = pyautogui.size().width
	height = pyautogui.size().height
	a = [width, height]
	resolution = tuple(a)

	filename = "recordings/{}.avi".format(filename)

	# Specify video codec
	codec = cv2.VideoWriter_fourcc(*"XVID")

	# Specify frames rate. We can choose any
	# value and experiment with it
	fps = 5

	# Creating a VideoWriter object
	out = cv2.VideoWriter(filename, codec, fps, resolution)

	# Create an Empty window
	cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

	# Resize this window
	cv2.resizeWindow("Live", 480, 270)

	while True:
	        # Take screenshot using PyAutoGUI
	        img = pyautogui.screenshot()

	        # Convert the screenshot to a numpy array
	        frame = np.array(img)

	        # Convert it from BGR(Blue, Green, Red) to
	        # RGB(Red, Green, Blue)
	        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	        # Write it to the output file
	        out.write(frame)

	        # Optional: Display the recording screen
	        cv2.imshow('Live', frame)

	        # Stop recording when we press 'q'
	        if cv2.waitKey(1) == ord('q'):
	                break

	# Release the Video writer
	out.release()

	# Destroy all windows
	cv2.destroyAllWindows()


