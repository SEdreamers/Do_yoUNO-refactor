import pygame
class GameObject():
    def __init__(self, model, x, y, width, height):
        self.model = model
        self.rect = pygame.Rect(x, y, width, height)

    def on_clicked(self):
        pass

    def update(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        for component in self.components:
            component.draw(surface)
