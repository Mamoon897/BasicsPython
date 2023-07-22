import os
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
a= input("enter something :")
print(type(a))
print(a)
speak(a)