import pyttsx3  #Text to speech library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5') #microsoft speech api hepls in recognition of voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

def takecommand(): #it takes microphone input from user and converts to string
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    contacts = {"yagami": "yagami@gmail.com", "stefan": "stefan@gmail.com"} #write here the person name with repect to their email whom you want to send email
    # we can import contacts from goggle in .csv file and import them in project and convert them into dictionary
    send= contacts[to]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #extended hello to start the process of sending email
    server.starttls() # transport layer service
    server.login('Type_Your_email_here', 'Your_password_here')
    server.sendmail('Type_Your_email_here',send,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
 
        elif 'play music' in query:
            music_dir ='C:\\Anas New\\Musicc' # Change this directory as per your convinience
            songs= os.listdir(music_dir)
            n= songs.__len__()
            r= random.choice(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open chrome' in query:
            codePath ="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("To whom should I send this email Sir?")
                to = takecommand()
                speak("What should I say?")
                content = takecommand()
                sendEmail(to, content)
                speak("Your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")

        elif 'quit' in query:
            speak("Shutting down in 3 2 1")
            exit()



