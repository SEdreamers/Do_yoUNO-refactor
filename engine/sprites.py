import pygame
from engine.game_object import GameObject

class Sprite(GameObject):
    def __init__(self, image_path, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = pygame.rect(x, y, width, height)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


