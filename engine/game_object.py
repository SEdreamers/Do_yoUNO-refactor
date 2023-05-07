import pygame
class Listener:
    def __init__(self):
        self.event_handlers = {}

    def on(self, event, handler):
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(handler)

    def emit(self, event, *args, **kwargs):
        if event in self.event_handlers:
            for handler in self.event_handlers[event]:
                handler(*args, **kwargs)

class GameObject(Listener):
    def __init__(self, name, x, y, width, height, components=None):
        super().__init__()
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.components = components if components else []

    def on_clicked(self):
        self.emit('clicked', self)

    def on_hover(self):
        self.emit('hover', self)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for component in self.components:
                if component.collidepoint(x, y):
                    self.on_clicked()
        elif event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            for component in self.components:
                if component.collidepoint(x, y):
                    self.on_hover()

    def update(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        for component in self.components:
            component.draw(surface)
