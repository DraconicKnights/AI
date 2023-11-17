from commandHandler.speech_commands import SpeechCommands
from commandHandler.web_commands import WebCommands
from commandHandler.wiki_commands import WikiCommand
from commandHandler.log_command import LogCommand

class CommandControll:
    
    def commandResolve(query):
            
        if query[0] == 'say':
            SpeechCommands.commandResponse(query)
            
        if query[0] == 'web' and query[1] == 'search':
            WebCommands.commandResponse(query)

        if query[0] == 'wikipedia':
            WikiCommand.commandResponse(query)

        if query[0] == 'startlog':
            LogCommand.commandResponse(query)
                 
