import pygame
from engine.game_object import GameObject


class Sprite(GameObject):
    def __init__(self,  model, screen, image_path, x=0, y=0, width=0, height=0):
        super().__init__(model, x, y, width, height)
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        # image 바꾸기 default -> color blind mode
        pass


