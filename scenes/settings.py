import pygame
from engine.scene import Scene
from models.model import Model
from engine.button import Button
class Setting(Scene):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.model = Model()
        self.running = True
        self.background_color = (0, 0, 0)
        self.default_color = (255, 255, 255)
        self.transparent_color = (255, 0, 0)

        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        screen_font = pygame.font.SysFont("arial", self.model.screen_width // 40, True)
        center = self.screen.get_rect().centerx
        self.screen_sizes = [(400, 300), (600, 450), (800, 600), (1000, 750)]
        self.menu_flag = 0
        # create buttons
        self.title = Button(center * 0.75, self.model.screen_height / 12,
                            self.model.screen_width / 4, self.model.screen_width / 16,
                            "Settings", font, self.default_color, None)
        self.blind_text = Button(center * 0.75, self.model.screen_height / 2.4,
                                 self.model.screen_width / 4, self.model.screen_width / 16,
                                 "Color Blind Mode", font, self.default_color, None)
        self.default_text = Button(center * 0.75, self.model.screen_height / 1.714,
                                   self.model.screen_width / 4, self.model.screen_width / 16, "Default Setting",
                                   font, self.default_color, None)
        self.back_text = Button(center * 0.75, self.model.screen_height / 1.333,
                                self.model.screen_width / 4, self.model.screen_width / 16, "Go Back", font,
                                self.default_color, None)

        self.exit_text = Button(center * 0.75, self.model.screen_height / 1.111,
                                self.model.screen_width / 4, self.model.screen_width / 16, "Exit", font,
                                self.default_color, None)

        self.size1 = Button(self.model.screen_width / 10, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size1", screen_font,
                            self.default_color, None)

        self.size2 = Button(self.model.screen_width / 3, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size2", screen_font,
                            self.default_color, None)

        self.size3 = Button(self.model.screen_width / 1.7, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size3", screen_font,
                            self.default_color, None)

        self.size4 = Button(self.model.screen_width / 1.2, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size4", screen_font,
                            self.default_color, None)
        self.button_list = [self.blind_text, self.default_text, self.back_text, self.exit_text,
                            self.size1, self.size2, self.size3, self.size4]
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for button in self.button_list:
                    button.handle_event(event)
                if event.type == pygame.KEYDOWN:
                    self.on_key_down(event)
            self.draw(self.screen)

        pygame.quit()

    def draw(self, screen):
        screen.fill(self.background_color)
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Update button colors based on menu_flag and mouse position
        self.title.color = self.default_color
        for index, button in enumerate(self.button_list):
            button.color = self.transparent_color if button.rect.collidepoint(mouse_pos) or self.menu_flag == index \
                else self.default_color
        # Draw buttons
        self.title.draw(screen)
        for button in self.button_list:
            button.draw(screen)
        pygame.display.flip()

    def on_mouse_button_down(self, event):
        pass

    def on_key_down(self, event):
        if event.key == pygame.K_UP:
            self.menu_flag -= 1
        elif event.key == pygame.K_DOWN:
            self.menu_flag += 1
        self.menu_flag %= 8

        # Update button hovered status based on menu_flag
        for index, button in enumerate(self.button_list):
            button.hovered = (self.menu_flag == index)

if __name__ == '__main__':
    main_scene = Setting()
    main_scene.run()
