from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

## Speech engine and Voice

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class VoiceControll():

    def speak(text, rate = 120):
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()