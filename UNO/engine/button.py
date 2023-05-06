import pygame
from game_object import GameObject

class Button(GameObject):
    def __init__(self, name, position, size, text, font, text_color, bg_color, hover_color, action=None):
        self.size = size
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.action = action
        self.hovering = False

        self.surface = pygame.Surface(size)
        self.surface.set_colorkey((0, 0, 0))
        self.rect = self.surface.get_rect()
        self.rect.topleft = position

        super().__init__(name, position)

    def on_clicked(self):
        super().on_clicked()
        if self.action:
            self.action()

    def on_hover(self):
        super().on_hover()
        self.hovering = True

    def draw(self, surface):
        self.surface.fill((0, 0, 0))

        # Change the button color based on its state
        color = self.hover_color if self.hovering else self.bg_color
        pygame.draw.rect(self.surface, color, pygame.Rect(0, 0, *self.size))

        # Render the text on the button
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.surface.blit(text_surface, text_rect)

        surface.blit(self.surface, self.rect)

    def handle_event(self, event):
        super().handle_event(event)
        self.hovering = False
