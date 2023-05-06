import pygame
from UNO.engine.scene import Scene
from UNO.models.model import Model
from UNO.engine.button import Button
# from lobby impor
# from scenes.story_map import StoryMapScene
# from scenes.settings import SettingsScene

class Start(Scene):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.model = Model()
        self.running = True

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
                                 "Uno Game", font, self.default_color, self.transparent_color, None)
        self.single_player_button = Button(center * 0.75, int(self.model.screen_height * 0.3),
                                           self.model.screen_width / 4, self.model.screen_width / 16, "Single Play",
                                           font, self.default_color, self.transparent_color, None)

        self.story_mode_button = Button(center * 0.75, int(self.model.screen_height * 0.47),
                                        self.model.screen_width / 4, self.model.screen_width / 16, "Story Mode", font,
                                        self.default_color, self.transparent_color, None)

        self.settings_button = Button(center * 0.75, int(self.model.screen_height * 0.64),
                                      self.model.screen_width / 4, self.model.screen_width / 16, "Settings", font,
                                      self.default_color, self.transparent_color, None)

        self.exit_button = Button(center * 0.75, int(self.model.screen_height * 0.81),
                                  self.model.screen_width / 4, self.model.screen_width / 16, "Exit", font,
                                  self.default_color, self.transparent_color, None)

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # self.handle_event(event)

            self.draw(self.screen)
            # Draw buttons
            self.game_title.draw(self.screen)
            self.single_player_button.draw(self.screen)
            self.story_mode_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.exit_button.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def draw(self, screen):
        screen.fill(self.background_color)

    def on_mouse_button_down(self, event):
        pass

    def on_mouse_button_up(self, event):
        pass

    def on_key_down(self, event):
        pass

    def on_key_up(self, event):
        pass

if __name__ == '__main__':
    main_scene = Start()
    main_scene.run()
