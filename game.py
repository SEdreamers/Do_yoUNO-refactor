import pygame
class Game:
    def __init__(self):
        pygame.init()
        self.running = True
    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        pass
    def update(self):
        pass
    def render(self):
        pass

