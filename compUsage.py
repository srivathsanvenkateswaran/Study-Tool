'''
Recycle bin cleaner
sort and store the files with same extension
Translator
clipboard manager
sticky notes
URL shortener and unshortener


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

