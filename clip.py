import pyperclip
import time

last_string = pyperclip.paste()
clear_str = """Walling, Rob; Taber, Mike. Start Small, Stay Small: A Developer's Guide to Launching a Startup"""


while True:
	time.sleep(0.02)
	string = pyperclip.paste()
	if string != last_string and string != '':
		clear_index = string.find(clear_str)
		if clear_index >= 0:
			string = string[0:clear_index]
			pyperclip.copy(string)
		print(string)
		last_string = string