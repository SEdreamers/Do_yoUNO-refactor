import pygame

from engine.button import Button
from engine.event import EventManager
from game import Game
from scenes.story import Story
from scenes.settings import Settings


class SinglePlayer(Button):
    def __init__(self, text, x, y, width, height, font, color):
        super().__init__(self, x, y, width, height, font, color)
        self.text = text
        self.event_manager = EventManager()
    def on_clicked(self):
        game = Game()
        game.run()

class StoryMode(Button):
    def __init__(self, text, x, y, width, height, font, color):
        super().__init__(self, x, y, width, height, font, color)
        self.text = text
    def on_clicked(self):
        story = Story()
        story.run()


class Settings(Button):
    def __init__(self, text, x, y, width, height, font, color):
        super().__init__(self, x, y, width, height, font, color)
        self.text = text

    def on_clicked(self):
        settings = Settings()
        settings.run()


class Exit(Button):
    pass
