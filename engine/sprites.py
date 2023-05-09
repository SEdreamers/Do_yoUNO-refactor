import pygame
from engine.game_object import GameObject


class Sprite(GameObject):
    def __init__(self, image_path, model, x, y, width, height):
        super().__init__(model)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect = pygame.rect(x, y, width, height)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        # image 바꾸기
        pass


