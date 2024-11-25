import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afetrnoon")

    else:
        speak("Good Evening")

    speak("I am your assistant. please tell me how may i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please......")
        return "None"
    return query
    


if __name__=="__main__":
    wishMe()
    # while True:
    if 1:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=3)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'play music' in query:
            music_dir='D:\\rsk\\MUSIC'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"now the time is {strTime}")

        elif 'open code' in query:
            codepath="C:\\Users\\ravik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)  