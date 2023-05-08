import pygame
from engine.scene import Scene
import res.prefabs.button as button

class Lobby(Scene):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.running = True
        self.menu_flag = 0
        self.background_color = (0, 0, 0)
        self.default_color = (255, 255, 255)
        self.transparent_color = (255, 0, 0)
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        pygame.display.set_caption("Uno Game")
        center = self.screen.get_rect().centerx
        # create buttons
        self.game_title = button.Button("Uno Game", center * 0.75, self.model.screen_height // 12,
                                        self.model.screen_width / 4, self.model.screen_width / 16,
                                        font, self.default_color)
        self.single_player_button = button.SinglePlayer("Single Play", center * 0.75,
                                                        int(self.model.screen_height * 0.3),
                                                        self.model.screen_width / 4, self.model.screen_width / 16,
                                                        font, self.default_color)

        self.story_mode_button = button.StoryMode("Story Mode", center * 0.75, int(self.model.screen_height * 0.47),
                                                  self.model.screen_width / 4, self.model.screen_width / 16, font,
                                                  self.default_color)

        self.settings_button = button.Settings("Settings", center * 0.75, int(self.model.screen_height * 0.64),
                                               self.model.screen_width / 4, self.model.screen_width / 16, font,
                                               self.default_color)

        self.exit_button = button.Exit("Exit", center * 0.75, int(self.model.screen_height * 0.81),
                                       self.model.screen_width / 4, self.model.screen_width / 16, font,
                                       self.default_color)
        self.button_list = [self.single_player_button, self.story_mode_button, self.settings_button, self.exit_button]


    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.on_mouse_button_down(event)
                elif event.type == pygame.KEYDOWN:
                    self.on_key_down(event)

            self.draw(self.screen)

        pygame.quit()

    def draw(self, screen):
        screen.fill(self.background_color)
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Update button colors based on menu_flag and mouse position
        for idx, but in enumerate(self.button_list):
            but.color = self.transparent_color \
                if but.rect.collidepoint(mouse_pos) or self.menu_flag == idx else self.default_color

        # Draw buttons
        self.game_title.draw(screen)
        for but in self.button_list:
            but.draw(screen)

        pygame.display.flip()

    def on_mouse_button_down(self, event):
        for but in self.button_list:
            if but.rect.collidepoint(event.pos):
                but.on_clicked()

    def on_key_down(self, event):
        if event.key == pygame.K_UP:
            self.menu_flag -= 1
        elif event.key == pygame.K_DOWN:
            self.menu_flag += 1
        elif event.key == pygame.K_RETURN:
            self.button_list[self.menu_flag].on_clicked()
        self.menu_flag %= 4

        # Update button hovered status based on menu_flag
        self.single_player_button.hovered = (self.menu_flag == 0)
        self.story_mode_button.hovered = (self.menu_flag == 1)
        self.settings_button.hovered = (self.menu_flag == 2)
        self.exit_button.hovered = (self.menu_flag == 3)


if __name__ == '__main__':
    main_scene = Lobby()
    main_scene.run()
