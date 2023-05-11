from engine.game_object import GameObject

class Button(GameObject):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(model, x, y, width, height)
        self.text = text
        self.screen = screen
        self.font = font
        self.color = color
        self.hovered = False

    def draw(self, surface):
        rendered_text = self.font.render(self.text, True, self.color)
        text_rect = rendered_text.get_rect(center=self.rect.center)
        surface.blit(rendered_text, text_rect)

    def update(self, x, y, width, height, font):
        super().update(x, y, width, height)
        self.font = font

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def change_text(self, text):
        self.text = text

    # Override
    def on_clicked(self):
        pass
