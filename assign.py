'''
Task notifier and website alarm
crop images and convert to pdf
screen recorder
image to text
label for assignments
scientific calculator
'''

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



