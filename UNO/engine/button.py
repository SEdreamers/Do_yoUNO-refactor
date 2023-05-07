import pygame
from UNO.engine.game_object import GameObject


class Button(GameObject):
    def __init__(self, x, y, width, height, text, font, text_color, button_color, callback):
        super().__init__(text, x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.callback = callback

    def draw(self, surface):
        rendered_text = self.font.render(self.text, True, self.text_color)
        text_rect = rendered_text.get_rect(center=self.rect.center)
        surface.blit(rendered_text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()
