import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


    speak("I am Jarvis sir. please tell me How may I help you")

def takeCommand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en -in")
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__== "__main__":
    
    wishMe()
    while True:
        query= takeCommand().lower()
    #Logic for executing tasks based on query

    if 'wikipedia' in query:
        speak('searching Wikipedia...')
        query = query.replase("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According To wikipedia")
        speak(results)




