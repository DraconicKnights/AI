from datetime import datetime
from voice import VoiceControll
from voice_controll import VoiceManagementCommand
import random

hello_array = [
    "Hello",
    "Welcome",
    "How are you",
    "Guten Tag",
    "Hi, I am Minuetes"
]

class HelloResponse:
    
    def helloCommand(query):
        VoiceControll.speak(random.choice(hello_array))