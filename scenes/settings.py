import pygame
from engine.scene import Scene
import res.prefabs.button as button


class Settings(Scene):
    def __init__(self, model, screen):
        super().__init__(model, screen)
        self.running = True
        self.background_color = (0, 0, 0)
        self.default_color = (255, 255, 255)
        self.transparent_color = (255, 0, 0)

        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        screen_font = pygame.font.SysFont("arial", self.model.screen_width // 40, True)
        center = self.screen.get_rect().centerx
        self.menu_flag = 0
        # create buttons
        self.title = button.Button("Settings", model, screen, center * 0.75, self.model.screen_height / 12,
                                   self.model.screen_width / 4, self.model.screen_width / 16,
                                   font, self.default_color)
        self.blind_text = button.Blind("Color Blind Mode", model, screen, center * 0.75, self.model.screen_height / 2.4,
                                       self.model.screen_width / 4, self.model.screen_width / 16,
                                       font, self.default_color)
        self.default_text = button.Default("Default Setting", model, screen, center * 0.75,
                                           self.model.screen_height / 1.714, self.model.screen_width / 4,
                                           self.model.screen_width / 16, font, self.default_color)
        self.back_text = button.Back("Go Back", model, screen, center * 0.75, self.model.screen_height / 1.333,
                                     self.model.screen_width / 4, self.model.screen_width / 16,  font,
                                     self.default_color)

        self.exit_text = button.Exit("Exit", model, screen, center * 0.75, self.model.screen_height / 1.111,
                                     self.model.screen_width / 4, self.model.screen_width / 16, font,
                                     self.default_color)

        self.size1 = button.Size("size1", model, screen, 1, self.model.screen_width / 10,
                                 self.model.screen_height / 4, self.model.screen_width / 30,
                                 self.model.screen_width / 60,  screen_font, self.default_color)

        self.size2 = button.Size("size2", model, screen, 2, self.model.screen_width / 3,
                                 self.model.screen_height / 4, self.model.screen_width / 30,
                                 self.model.screen_width / 60, screen_font, self.default_color)

        self.size3 = button.Size("size3", model, screen, 3, self.model.screen_width / 1.7,
                                 self.model.screen_height / 4, self.model.screen_width / 30,
                                 self.model.screen_width / 60,  screen_font, self.default_color)

        self.size4 = button.Size("size4", model, screen, 4, self.model.screen_width / 1.2,
                                 self.model.screen_height / 4, self.model.screen_width / 30,
                                 self.model.screen_width / 60, screen_font, self.default_color)

        self.button_list = [self.title, self.blind_text, self.default_text, self.back_text, self.exit_text,
                            self.size1, self.size2, self.size3, self.size4]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.event_manager.emit(event)

                elif event.type == pygame.KEYDOWN:
                    self.event_manager.emit(event)
            self.draw(self.title, self.button_list, self.menu_flag, self.background_color,
                      self.transparent_color, self.default_color)
        pygame.quit()

    def on_mouse_button_down(self, event):
        for but in self.button_list:
            if but.rect.collidepoint(event.pos):
                but.on_clicked()
                self.update_size()

    def on_key_down(self, event):
        if event.key == pygame.K_UP:
            self.menu_flag -= 1
        elif event.key == pygame.K_DOWN:
            self.menu_flag += 1
        elif event.key == pygame.K_RETURN:
            self.button_list[self.menu_flag + 1].on_clicked()
            self.update_size()
        self.menu_flag %= 8

        # Update button hovered status based on menu_flag
        for index, butt in enumerate(self.button_list[1:]):
            butt.hovered = (self.menu_flag == index)

    def update_size(self):
        center = self.screen.get_rect().centerx
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        screen_font = pygame.font.SysFont("arial", self.model.screen_width // 40, True)
        text = [12, 2.4, 1.714, 1.333, 1.111]
        size = [10, 3, 1.7, 1.2]
        for butt, index in zip(self.button_list[:5], text):
            butt.update(center * 0.75, self.model.screen_height / index,
                        self.model.screen_width / 4, self.model.screen_width / 16, font)
        for butt, index in zip(self.button_list[5:], size):
            butt.update(self.model.screen_width / index, self.model.screen_height / 4,
                        self.model.screen_width / 30, self.model.screen_width / 60, screen_font)


if __name__ == '__main__':
    main_scene = Settings()
    main_scene.run()
