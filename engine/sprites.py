import pygame
from engine.game_object import GameObject


class Sprite(GameObject):
    def __init__(self,  model, screen, image_path, x, y, width, height):
        super().__init__(model, x, y, width, height)
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        # image 바꾸기 default -> color blind mode
        pass


