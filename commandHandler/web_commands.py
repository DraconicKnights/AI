from datetime import datetime
from voice import VoiceControll
import webbrowser
import wikipedia
import wolframalpha

edge_path = r" C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

class WebCommands:

    def commandResponse(query):
        VoiceControll.speak('Going to...')
        query = ' '.join(query[2:])
        webbrowser.get('edge').open_new(query)