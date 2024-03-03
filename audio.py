import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import time
from speech_recognition import WaitTimeoutError

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises.. Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=5)  # Adjust for ambient noise
        try:
            recordedaudio = recognizer.listen(source, timeout=10)  # Listen for 10 seconds
        except WaitTimeoutError:
            print("Timeout waiting for phrase to start. Please try again.")
            return
        print('Ask me anything..')
        time.sleep(1)  # Add a delay to avoid immediate second listen
        try:
            recordedaudio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
        except WaitTimeoutError:
            print("Timeout waiting for phrase to continue. Please try again.")
            return

    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))

    except Exception as ex:
        print(ex)
    if 'chrome' in text:
        a = 'Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        program = 'https://www.chrome.com'
        subprocess.Popen([program])

    if 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        engine.say(current_time)
        engine.runAndWait()

    if 'play' in text:
        a = 'Opening Browser..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text.replace('play', ''))

    if 'youtube' in text:
        b = 'Opening YouTube..'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com')
    # ... (rest of the code)

while True:
    cmd()
