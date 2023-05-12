class Event:
    def __init__(self, event_type, **kwargs):
        self.type = event_type
        self.kwargs = kwargs


class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def emit_event(self, event):
        if event.type in self.listeners:
            for listener in self.listeners[event.type]:
                listener(event)

    def emit_type(self, event_type, event, *args, **kwargs):
        if event_type in self.listeners:
            for handler in self.listeners[event_type]:
                handler(event, *args, **kwargs)
