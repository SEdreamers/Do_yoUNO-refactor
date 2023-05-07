import pygame
from engine.scene import Scene
from models.model import Model
from engine.button import Button
class Setting(Scene):
    def __init__(self):
        pygame.init()
        super().__init__()
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
        self.title = Button(center * 0.75, self.model.screen_height / 12,
                            self.model.screen_width / 4, self.model.screen_width / 16,
                            "Settings", font, self.default_color, None)
        self.blind_text = Button(center * 0.75, self.model.screen_height / 2.4,
                                 self.model.screen_width / 4, self.model.screen_width / 16,
                                 "Color Blind Mode", font, self.default_color, self.blind_click)
        self.default_text = Button(center * 0.75, self.model.screen_height / 1.714,
                                   self.model.screen_width / 4, self.model.screen_width / 16, "Default Setting",
                                   font, self.default_color, self.default_click)
        self.back_text = Button(center * 0.75, self.model.screen_height / 1.333,
                                self.model.screen_width / 4, self.model.screen_width / 16, "Go Back", font,
                                self.default_color, self.go_back_click)

        self.exit_text = Button(center * 0.75, self.model.screen_height / 1.111,
                                self.model.screen_width / 4, self.model.screen_width / 16, "Exit", font,
                                self.default_color, self.exit_button_click)

        self.size1 = Button(self.model.screen_width / 10, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size1", screen_font,
                            self.default_color, self.size1_click)

        self.size2 = Button(self.model.screen_width / 3, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size2", screen_font,
                            self.default_color, self.size2_click)

        self.size3 = Button(self.model.screen_width / 1.7, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size3", screen_font,
                            self.default_color, self.size3_click)

        self.size4 = Button(self.model.screen_width / 1.2, self.model.screen_height / 4,
                            self.model.screen_width / 30, self.model.screen_width / 60, "size4", screen_font,
                            self.default_color, self.size4_click)
        self.button_list = [self.title, self.blind_text, self.default_text, self.back_text, self.exit_text,
                            self.size1, self.size2, self.size3, self.size4]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for button in self.button_list[1:]:
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
        for index, button in enumerate(self.button_list[1:]):
            button.color = self.transparent_color if button.rect.collidepoint(mouse_pos) or self.menu_flag == index \
                else self.default_color
        # Draw buttons
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
        for index, button in enumerate(self.button_list[1:]):
            button.hovered = (self.menu_flag == index)
    def blind_click(self):
        self.model.color_blind_mode = not self.model.color_blind_mode
        self.model.save_data()

    def default_click(self):
        self.model.screen_width = 800
        self.model.screen_height = 600
        self.model.color_blind_mode = False
        self.model.background_volume = 0.3
        self.model.total_volume = 0.3
        self.model.player_numbers = 3
        self.model.save_data
    def go_back_click(self):
        pass
        # 전에 있던 창(main or game 화면)

    def exit_button_click(self):
        self.running = False

    def size1_click(self):
        self.model.screen_width = 400
        self.model.screen_height = 300
        self.model.save_data()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        self.update_size()
    def size2_click(self):
        self.model.screen_width = 600
        self.model.screen_height = 450
        self.model.save_data()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        self.update_size()
    def size3_click(self):
        self.model.screen_width = 800
        self.model.screen_height = 600
        self.model.save_data()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        self.update_size()
    def size4_click(self):
        self.model.screen_width = 1000
        self.model.screen_height = 750
        self.model.save_data()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        self.update_size()
    def update_size(self):
        center = self.screen.get_rect().centerx
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        screen_font = pygame.font.SysFont("arial", self.model.screen_width // 40, True)
        text = [12, 2.4, 1.714, 1.333, 1.111]
        size = [10, 3, 1.7, 1.2]
        for button, index in zip(self.button_list[:5], text):
            button.update(center * 0.75, self.model.screen_height / index,
                          self.model.screen_width / 4, self.model.screen_width / 16, font)
        for button, index in zip(self.button_list[5:], size):
            button.update(self.model.screen_width / index, self.model.screen_height / 4,
                          self.model.screen_width / 30, self.model.screen_width / 60, screen_font)

if __name__ == '__main__':
    main_scene = Setting()
    main_scene.run()
