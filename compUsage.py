'''
Recycle bin cleaner
sort and store the files with same extension
clipboard manager
sticky notes
URL shortener and unshortener

pip install trash-cli
pip install winshell
pip install contextlib
pip install urllib3

'''

def clearRecycleBin():
	import sys
	from os import system
	#checking the platform
	if sys.platform == 'linux':
		#using trash-cli module, trash-empty {days} this will delete 7 days old files alone
		system('sudo trash-empty 7')
	elif sys.platform == 'win32':
		#if the platform is windows this will be executed
		import winshell
		winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
	else:
		pass

def sortAndstoreFiles(path):
	import os
	import shutil
	
	# This will create a properly organized
	# list with all the filename that is
	# there in the directory
	list_ = os.listdir(path)
	
	# This will go through each and every file
	for file_ in list_:
		name, ext = os.path.splitext(file_)
	
		# This is going to store the extension type
		ext = ext[1:]
	
		# This forces the next iteration,
		# if it is the directory
		if ext == '':
			continue
	
		# This will move the file to the directory
		# where the name 'ext' already exists
		if os.path.exists(path+'/'+ext):
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
	
		# This will create a new directory,
		# if the directory does not already exist
		else:
			os.makedirs(path+'/'+ext)
			shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)


def shorten(url):
	import contextlib
	from urllib.parse import urlencode
	from urllib.request import urlopen
  	
  	#shortening url with tinyurl api
	request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
  	with contextlib.closing(urlopen(request_url)) as response:
	return response.read().decode('utf-8 ')

def unshorten(url):
	import requests

	#returns the unshortened url
    return requests.head(url, allow_redirects=True).url



