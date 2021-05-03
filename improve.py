'''
safe eyes
Audiobook from Youtube [Play audiobook from Youtube and play the Audio file]

next update:
website blocker
audiobook (need to find best module)
book recommender

pip install safeeyes
'''

def SafeEyes(command):
	import os
	if command == 'enable':
		os.system('safeeyes &')
	if command == 'disable':
		os.system('safeeyes -d')
	if command == 'settings':
		os.system('safeeyes -s')
	if commmand == 'status':
		os.system('safeeyes --status')


#### need to add
