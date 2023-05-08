import pygame
from engine.event import EventManager
from models.model import Model
class Scene(EventManager):
    def __init__(self):
        super().__init__()
        self.model = Model()

        # Subscribe event handlers
        self.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_button_down)
        self.subscribe(pygame.KEYDOWN, self.on_key_down)

    def run(self, event):
        # read event and create event object
        pass
    def draw(self, screen):
        # Draw the scene
        pass
    def change(self):
        # scene 바꿔주기
        pass

    def on_mouse_button_down(self):
        pass
    def on_key_down(self):
        pass