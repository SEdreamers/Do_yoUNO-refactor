import pygame
from engine.game_object import GameObject

class Sprite(GameObject):
    def __init__(self, image_path, position):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)


