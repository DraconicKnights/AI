from datetime import datetime
from voice import VoiceControll

class SpeechCommands:

    def commandResponse(query):
        if 'hello' in query:
            VoiceControll.speak('Hello')
        else:
            query.pop(0) ## Remove say
            speech = ' '.join(query)
            VoiceControll.speak(speech)