import pygame
from scenes.lobby import Lobby
from models.model import Model

if __name__ == '__main__':
    model = Model()
    screen = pygame.display.set_mode((model.screen_width, model.screen_height))
    UNO = Lobby(model, screen)
    UNO.run()
