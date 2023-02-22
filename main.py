# pyinstaller --onefile some.py

import telebot
import os
import webbrowser
import psutil

bot = telebot.TeleBot('')
operagx_path = 'C:/Users/1/AppData/Local/Programs/Opera GX/opera.exe %s'


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

	if message.text == "/help":
		bot.send_message(message.from_user.id, '''

			/sublime
			/sublime_close

			/browser
			/browser_close

			/cmd
			/cmd_close

			/off
			/sleep
			''')

	elif message.text == '/sublime':
		os.startfile('C:/Program Files/Sublime Text/sublime_text.exe')

	elif message.text == '/browser':
		webbrowser.get(operagx_path).open("opera://startpage")

	elif message.text == '/cmd':
		os.startfile('C:/WINDOWS/system32/cmd.exe')

	elif message.text == '/sublime_close':
		for process in (process for process in psutil.process_iter() if process.name()=="sublime_text.exe"):
			process.kill()

	elif message.text == '/browser_close':
		for process in (process for process in psutil.process_iter() if process.name()=="opera.exe"):
			process.kill()

	elif message.text == '/cmd_close':
		for process in (process for process in psutil.process_iter() if process.name()=="cmd.exe"):
			process.kill()

	elif message.text == '/off':
		os.system("shutdown /s /t 00")

	elif message.text == '/sleep':
		os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

bot.polling(none_stop=True, interval=0)
