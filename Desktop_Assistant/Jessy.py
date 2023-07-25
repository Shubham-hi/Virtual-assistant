from pickle import TRUE
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
from plyer import notification
import time
import pywhatkit as kwt
from youtubesearchpython import Search


engine= pyttsx3.init("sapi5")
voice= engine.getProperty("voices")
# print(voice[0].id)
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<12:
      speak("Good morning sir!")
    elif hour>=12 and hour<18:
      speak("Good afternoon sir!")
    else:
      speak("Good evening sir!")
    
    speak("i am Jessy sir! How may i help you")

def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold=1
    audio=r.listen(source)
  
  try:
    print("Recognizing...")
    query=r.recognize_google(audio,language="en-in")
    print(f"User said: {query}\n")
  
  except Exception as e:
    print(e)
    print("Say that again please....")
    return "None"
  return query




if __name__=="__main__":   
 speak(" ")
 wishMe()
 while True:
  query=takeCommand().lower()

  if "wikipedia" in query:
    speak("Searching Wikipedia... ")
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak("Acoordin to wikipedia")
    print(results)
    speak(results)
  
  elif "open youtube" in query:
     speak("Sir what do you want to search")
     a=takeCommand()
     kwt.playonyt(a)
    #  webbrowser.open("youtube.com" )

  elif "open google" in query:
     webbrowser.open("google.com")
  
  elif "play music" in query:
    music_dir="E:\\CODING STUFF\\songs"
    songs=os.listdir(music_dir)
    len1=len(songs)
    print(songs)
    ran=random.randint(0,len1)
    os.startfile(os.path.join(music_dir,songs[ran]))
  
  elif "the time" in query:
    strtime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strtime}")
    print(strtime)
   
  elif "open vs code" in query:
    location="E:\\Microsoft VS Code\\Code.exe"
    os.startfile(location)

  elif "quit" in query:
    quit()
  
  if "reminder" in query:
   speak("sir plz say time in seconds")
   K=takeCommand()
   k=int(K)
   while True:
       notification.notify(
             title="Its Exercise Time",
             message='''Shubham u have done lots of work for the day
             now it time to relax and chill time''',
             app_icon="C:\\Users\\Bansa\\Downloads\\exercise_boxing_sport_icon_133366.ico",
             timeout=5
       )
       time.sleep(k)
      