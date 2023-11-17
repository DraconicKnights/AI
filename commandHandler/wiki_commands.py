from datetime import datetime
from voice import VoiceControll
import webbrowser
import wikipedia
import wolframalpha


def search_wiki(query = ''):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('No wikipedia results')
        return 'No Results received'
        
    try:
        wikiPage = wikipedia.page(searchResults[0])

    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])

        print(wikiPage.title)
        wikiSum = str(wikiPage.summary)
    return wikiSum

class WikiCommand:
    
    def commandResponse(query):
        query = ' '.join(query[1:])
        VoiceControll.speak('Querying the universal databank')
        VoiceControll.speak(search_wiki(query))