import pygame
from engine.scene import Scene


class Story(Scene):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        self.background = (255, 255, 255)
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill(self.background)
            pygame.display.flip()

    def draw(self):
        pass