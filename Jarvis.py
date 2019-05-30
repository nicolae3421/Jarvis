import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
	print(words) 
	os.system("say" + words) 

talk(" Hello, how can I help you?")

def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		zadanie = r.recognize_google(audio, language="en-US").lower()
		print("You said: " + zadanie)
	except sr.UnknownValueError:
		talk(" I don't understant you")
		zadanie = command()

	return zadanie

def makeSomething(zadanie):
	if 'jarvis open youtube' in zadanie:
		talk("Already open")
		url = 'https://youtube.com'
		webbrowser.open(url)

	if 'jarvis open google' in zadanie:
		talk("Already open")
		url = 'https://google.com'
		webbrowser.open(url)

	if 'jarvis open euro truck' in zadanie:
		os.startfile('E:/steam/steamapps/common/Euro Truck Simulator 2/bin/win_x64/eurotrucks2.exe')
	if 'close euro truck' in zadanie:
		os.system('TASKKILL /F /IM eurotrucks2.exe')

	elif 'jarvis stop' in zadanie:
		talk("Yes, of course, not problems")
		sys.exit()
	elif 'jarvis what is your name' in zadanie:
		talk("My name is Jarvis")

while True:
	makeSomething(command())