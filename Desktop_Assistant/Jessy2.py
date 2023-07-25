from pickle import TRUE
from re import T
from turtle import title
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
from word2number import w2n # used to convert a string one ,two, threee to 1,2,3
from plyer import notification
import time


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

# def takeCommand_To_do():
#     r=sr.Recognizer()
#     with sr.Microphone as Mr:
#         print("Listening....")
  
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
      


 