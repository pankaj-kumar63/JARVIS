import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
# command=["google.com","facebook.com","youtube.com"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir How can I help you")
    elif hour>=12 and hour<18:
        speak("Good Afternon! Sir How can I help you")
    else:
        speak("Good Evening !Sir How can I help you ")

def takeCom():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
       print("Recognizing...")
       query=r.recognize_google(audio,language='en-in')
       print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return  "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    # server.ehlo()
    # server.starttls()
    server.login('pankajkumar9ptl@gmail.com','')
    server.sendmail('pankajkumar9ptl@gmail.com',to,content)
    server.quit()


if __name__=="__main__":
    wishMe()
    # takeCom()


    while True:
    # if 1:
        query = takeCom().lower()

        #Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
        elif 'open google' in query:
                    webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
        elif 'open w3school' in query:
                    webbrowser.open("w3school.com")
        elif 'open whatsapp' in query:
                    webbrowser.open("web.whatsapp.com")

        elif'hollywood movie' in query:
            movies_dir='E:\movies\hollywood'
            movies=os.listdir(movies_dir)
            print(movies)
            os.startfile(os.path.join(movies_dir,movies[random.randint(1,len(movies))]))

        elif'bollywood movie' in query:
            movies_dir='E:\\movies\\bollywood'
            movies=os.listdir(movies_dir)
            print(movies)
            os.startfile(os.path.join(movies_dir,movies[random.randint(1,len(movies))]))

        elif'music' in query:
            music_dir='E:\\music'
            music=os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir,music[random.randint(1,len(music))]))


        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is:{strTime}")

        elif ' open vs code' in query:
            codePath="C:\\Users\\pankaj kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to lovely' in query:
            try:
                speak("what should I say?")
                content=takeCom()
                to="pankajkumar9ptl@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry pankaj could not sent your email!")

        elif 'how are you' in query:
            speak("i'm fine what about you?")

        elif 'you are so sweet' in query or 'nice to talk you' in query:
            speak("thank you Pankaj")

        elif 'quit' in query or 'good bye' in query:
            speak("goodbye baby")
            exit()

        elif 'shutdown the pc' in query:
            speak("ok baby Shutting down the pc...")
            os.system("shutdown /p")

        # elif f"{query}" in query:
        #     webbrowser.open(f"{query}")
        # exit()

