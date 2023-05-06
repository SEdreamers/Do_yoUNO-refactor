import pygame

class Sprite:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)


