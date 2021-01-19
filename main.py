import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
from time import sleep
from word2number import w2n

"""The recognoser"""
listener = sr.Recognizer()

#initialising engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
name = 'Kumar'
engine.say('Hi I am Donut')
engine.say('I am here to assist you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    try:
        with sr.Microphone() as source:
            print("listening")
            listener.pause_threshold =1
            listener.energy_threshold = 2500
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'kumar' in command:
                command = command.replace('kumar','')
                talk(command)
            print(command)
        return command
    except:
        pass

def run():
    try:
        command = takecommand()
        if 'play' in command:
            song = command.replace('play','')
            print('playing')
            pywhatkit.playonyt(song)
            talk('playing'+song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The time is'+time)
            print(time)
        elif 'who is' in command:
            if('who is' in command):
                person = command.replace('who is','')
            info = wikipedia.summary(person,3)
            print(info)
            talk(info)
        elif 'joke' in command:
            joke = (pyjokes.get_joke())
            print(joke)
            talk(joke)
        elif('open' in command):
            if('youtube' in command):
                talk("Here you go to Youtube")
                webbrowser.open("youtube.com")
            elif('facebook' in command):
                talk("Here you go to facebook")
                webbrowser.open("facebook.com")
            elif('google' in command):
                talk("Here you go to google")
                webbrowser.open("google.com")
            elif('stackoverflow' in command):
                talk("here you go to stack overflow")
                webbrowser.open('stackoverflow.com')
            elif('resume' in command):
                talk("opening resume")
                codepath = "C:\\Users\\MANIKANTA KUMAR\\Desktop\\Manikanta_resume.pdf"
                os.startfile(codepath)
            elif('notepad' in command):
                talk('opening notepad')
                try:
                    codepath = 'C:\\Program Files\\notepad++.exe'
                    os.startfile(codepath)
                except:
                    talk("i cannot open it right now  beacause" )
            elif 'chrome' in command:
                talk('opening Google chrome')
                try:
                    codepath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                    os.startfile(codepath)
                except:
                    talk("cannot open it")
            elif 'explorer' in command:
                talk('opening Internet Explorer')
                try:
                    codepath = 'C:\\Program Files (x86)\\Internet Explorer\\iexplorer.exe'
                    os.startfile(codepath)
                except:
                    talk("cannot open it")
            elif('Cricket' in command):
                talk('opening cricket')
                codepath = 'D:\\games\\Cricket 2007.exe'
                os.startfile(codepath)
        elif 'search' in command:
            command = command.replace('search','')
            webbrowser.open(command)
        elif 'note' in command:
            if 'take ' in command:
                talk("what is the file name")
                a = takecommand()
                file = open(a+".txt",'w')
                talk("what should i write")
                content = takecommand()
                file.write(content)
                talk("content is written to file"+a)
            elif 'get' in command:
                talk("what is the file name")
                a = takecommand()
                try:
                    file = open(a+".txt",'r')
                    talk(file.read())
                except:
                    talk("there is no such file named"+a)
        elif 'where is' in command:
            place = command.replace('where is','')
            talk("you have asked for"+place)
            webbrowser.open("http://www.google.com/maps/place/"+place)





        else:
            talk('please say the command again')
    except:
        pass
while (True):
    run()