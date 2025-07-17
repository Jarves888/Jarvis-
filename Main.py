import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Girish bhai...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(language='en-in')
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, couldn't hear properly.")
        return ""

while True:
    query = take_command()
    if 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"Time is {time}")
    elif 'stop' in query or 'exit' in query:
        speak("Bye Girish bhai!")
        break
    else:
        speak("Sorry, I don't understand yet.")
