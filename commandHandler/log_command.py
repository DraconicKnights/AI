from datetime import datetime
from voice import VoiceControll
from voice_controll import VoiceManagementCommand


class LogCommand:

    def commandResponse(query):
        VoiceControll.speak('Log ready')
        print('Log is ready')

        newNote = VoiceManagementCommand.parseCommand().lower()
        now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with open('note_%s.txt' % now, 'w') as file:
            file.write(newNote)
        VoiceControll.speak('You have ended the log')
        

