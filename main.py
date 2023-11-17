from datetime import datetime
import sys
from command import CommandControll
from event import EventControll
from voice import VoiceControll
from voice_controll import VoiceManagementCommand

print("python version: ", sys.version)

## Speech engine

activationWord = 'minutes'

## Main loop

if __name__  == '__main__':
    VoiceControll.speak('All systems are operational')

    while True:
        ## Parse commands
        query = VoiceManagementCommand.parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            ## Commands
            CommandControll.commandResolve(query)
        else:
            ## Events
            EventControll.eventResolve(query)
