import pygame

class GameObject():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def on_clicked(self):
        self.eventManager.emit(pygame.MOUSEBUTTONDOWN)

    def update(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        for component in self.components:
            component.draw(surface)
