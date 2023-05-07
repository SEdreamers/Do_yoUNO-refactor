import pygame
from UNO.engine.event import Event, EventManager

class Scene(EventManager):
    def __init__(self):
        super().__init__()

        # Subscribe event handlers
        self.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_button_down)
        self.subscribe(pygame.KEYDOWN, self.on_key_down)

    def run(self, event):
        # read event and create event object
        pass
    def draw(self, screen):
        # Draw the scene
        pass
