import pygame
from UNO.engine.scene import Scene
from UNO.models.model import Model
# from lobby impor
# from scenes.story_map import StoryMapScene
# from scenes.settings import SettingsScene

class Start(Scene):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.running = True
        self.background_color = (0, 0, 0)
        self.default_color = (255, 255, 255)
        self.event_color = (255, 0, 0)
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        pygame.display.set_caption("Uno Game")

        # 메뉴 텍스트 생성
        game_title = font.render("Uno Game", True, self.default_color)
        single_player_text = font.render("Play Mode", True, self.event_color)
        story_mode_text = font.render("Story Mode", True, self.default_color)

        settings_text = font.render("Settings", True, self.default_color)
        exit_text = font.render("Exit", True, self.default_color)

        # 메뉴 위치 설정
        game_title_rect = game_title.get_rect()
        game_title_rect.centerx = screen.get_rect().centerx
        game_title_rect.y = self.model.screen_height // 12

        single_player_rect = single_player_text.get_rect()
        single_player_rect.centerx = screen.get_rect().centerx
        single_player_rect.y = self.model.screen_height * 0.3

        story_mode_rect = story_mode_text.get_rect()
        story_mode_rect.centerx = screen.get_rect().centerx
        story_mode_rect.y = self.model.screen_height * 0.47

        settings_rect = settings_text.get_rect()
        settings_rect.centerx = screen.get_rect().centerx
        settings_rect.y = self.model.screen_height * 0.64

        exit_rect = exit_text.get_rect()
        exit_rect.centerx = screen.get_rect().centerx
        exit_rect.y = self.model.screen_height * 0.81

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.handle_event(event)

            self.draw(screen)
            pygame.display.flip()

        pygame.quit()

    def draw(self, screen):
        screen.fill(self.background_color)

if __name__ == '__main__':
    main_scene = Start()
    main_scene.run()
