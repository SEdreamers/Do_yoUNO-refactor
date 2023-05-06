import pygame

class Sprites:
    def __init__(self):
        self.game_objects = []

    def add(self, game_object):
        self.game_objects.append(game_object)

    def remove(self, game_object):
        self.game_objects.remove(game_object)

    def update(self, event):
        for game_object in self.game_objects:
            game_object.handle_event(event)

    def draw(self, surface):
        for game_object in self.game_objects:
            game_object.draw(surface)
