import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'who is' in query:
            speak('Searching Wikipedia...')
            person = query.replace("who is", "")
            results = wikipedia.summary(person, 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'song' in query:
            codpath = "C:\\Users\\Balaji\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codpath)
            speak("here is spotify. choose your song")
        elif 'goodbye jarvis' in query:
            speak("have a good day sir")
            break
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'say' in query:
            speak(query)
        elif 'good' in query:
            speak('thankyou')
        elif 'hello' in query:
            speak('hi. how are you?')


