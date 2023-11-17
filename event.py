from events.hello import HelloResponse

class EventControll:

    def eventResolve(query):
        if query[0] == "hello":
            HelloResponse.helloCommand(query)