from voice import VoiceControll
import speech_recognition as sr

class VoiceManagementCommand:

    def parseCommand():
        listener = sr.Recognizer()
        print('Listening for a command')

        with sr.Microphone() as source:
            listener.pause_thresh = 2
            input_speech = listener.listen(source)

        try:
            print('Forwarding Commands')
            query = listener.recognize_google(input_speech, language='en_GB')
            print(f'The input speech was: (query)')
        except Exception as exception:
            print(" i didn't understand that")
            VoiceControll.speak("i didn't understand that")
            print(exception)
            return 'None'
            
        return query