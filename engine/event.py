class Event:
    def __init__(self, type, **attributes):
        self.type = type
        self.attributes = attributes

    def __getattr__(self, attr):
        if attr in self.attributes:
            return self.attributes[attr]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")


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

    def emit(self, event):
        if event.type in self.listeners:
            for listener in self.listeners[event.type]:
                listener(event)
