import pygame
from engine.scene import Scene


class Story(Scene):
    def __init__(self, model):
        super().__init__(model)
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        self.background = (0, 0, 255)
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill(self.background)
            pygame.display.flip()

    def draw(self):
        pass