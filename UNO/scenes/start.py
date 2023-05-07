import pygame
from UNO.engine.scene import Scene
from UNO.models.model import Model
from UNO.engine.button import Button
from lobby import Lobby
from story import Story
from settings import Setting
# from scenes.story_map import StoryMapScene
# from scenes.settings import SettingsScene

class Start(Scene):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.model = Model()
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
        self.game_title = Button(center * 0.75, self.model.screen_height // 12,
                                 self.model.screen_width / 4, self.model.screen_width / 16,
                                 "Uno Game", font, self.default_color, None)
        self.single_player_button = Button(center * 0.75, int(self.model.screen_height * 0.3),
                                           self.model.screen_width / 4, self.model.screen_width / 16, "Single Play",
                                           font, self.default_color, self.single_player_button_click)

        self.story_mode_button = Button(center * 0.75, int(self.model.screen_height * 0.47),
                                        self.model.screen_width / 4, self.model.screen_width / 16, "Story Mode", font,
                                        self.default_color, self.story_mode_button_click)

        self.settings_button = Button(center * 0.75, int(self.model.screen_height * 0.64),
                                      self.model.screen_width / 4, self.model.screen_width / 16, "Settings", font,
                                      self.default_color, self.settings_button_click)

        self.exit_button = Button(center * 0.75, int(self.model.screen_height * 0.81),
                                  self.model.screen_width / 4, self.model.screen_width / 16, "Exit", font,
                                  self.default_color, self.exit_button_click)


    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.single_player_button.handle_event(event)
                self.story_mode_button.handle_event(event)
                self.settings_button.handle_event(event)
                self.exit_button.handle_event(event)

                if event.type == pygame.KEYDOWN:
                    self.on_key_down(event)

            self.draw(self.screen)

        pygame.quit()

    def draw(self, screen):
        screen.fill(self.background_color)
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Update button colors based on menu_flag and mouse position
        self.single_player_button.color = self.transparent_color\
            if self.single_player_button.rect.collidepoint(mouse_pos) or self.menu_flag == 0 else self.default_color
        self.story_mode_button.color = self.transparent_color \
            if self.story_mode_button.rect.collidepoint(mouse_pos) or self.menu_flag == 1 else self.default_color
        self.settings_button.color = self.transparent_color \
            if self.settings_button.rect.collidepoint(mouse_pos) or self.menu_flag == 2 else self.default_color
        self.exit_button.color = self.transparent_color \
            if self.exit_button.rect.collidepoint(mouse_pos) or self.menu_flag == 3 else self.default_color
        # Draw buttons
        self.game_title.draw(screen)
        self.single_player_button.draw(screen)
        self.story_mode_button.draw(screen)
        self.settings_button.draw(screen)
        self.exit_button.draw(screen)

        pygame.display.flip()

    def on_mouse_button_down(self, event):
        mouse_pos = event.pos
        if self.single_player_button.rect.collidepoint(mouse_pos):
            lobby = Lobby()
        elif self.story_mode_button.rect.collidepoint(mouse_pos):
            story = Story()
        elif self.settings_button.rect.collidepoint(mouse_pos):
            setting = Setting()
        elif self.exit_button.rect.collidepoint(mouse_pos):
            self.running = False

    def on_key_down(self, event):
        if event.key == pygame.K_UP:
            self.menu_flag -= 1
        elif event.key == pygame.K_DOWN:
            self.menu_flag += 1
        self.menu_flag %= 4

        # Update button hovered status based on menu_flag
        self.single_player_button.hovered = (self.menu_flag == 0)
        self.story_mode_button.hovered = (self.menu_flag == 1)
        self.settings_button.hovered = (self.menu_flag == 2)
        self.exit_button.hovered = (self.menu_flag == 3)

    def single_player_button_click(self):
        lobby = Lobby()

    def story_mode_button_click(self):
        story = Story()

    def settings_button_click(self):
        setting = Setting()

    def exit_button_click(self):
        self.running = False


if __name__ == '__main__':
    main_scene = Start()
    main_scene.run()
