import pygame
from engine.scene import Scene
import res.prefabs.button as button

class Multi(Scene):
    def __init__(self, model, screen):
        super().__init__(model, screen)
        self.running = True
        self.menu_flag = 0
        self.model = model
        self.screen = screen
        self.background_color = (0, 0, 0)
        self.default_color = (255, 255, 255)
        self.transparent_color = (255, 0, 0)
        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        pygame.display.set_caption("Uno Game")
        center = self.screen.get_rect().centerx
        # create buttons
        self.game_title = button.Button("Multi Play", model, screen, center * 0.75, self.model.screen_height // 12,
                                        self.model.screen_width / 4, self.model.screen_width / 16,
                                        font, self.default_color)
        self.server_button = button.ServerPlay("Server", model, screen, center * 0.75,
                                               int(self.model.screen_height * 0.3),
                                               self.model.screen_width / 4, self.model.screen_width / 16,
                                               font, self.default_color)

        self.client_button = button.ClientPlay("Client", model, screen, center * 0.75,
                                              int(self.model.screen_height * 0.47), self.model.screen_width / 4,
                                              self.model.screen_width / 16, font, self.default_color)

        self.exit_button = button.Exit("Exit", model, screen, center * 0.75, int(self.model.screen_height * 0.81),
                                       self.model.screen_width / 4, self.model.screen_width / 16, font,
                                       self.default_color)
        self.button_list = [self.game_title, self.server_button, self.client_button, self.exit_button]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.event_manager.emit_event(event)
                elif event.type == pygame.KEYDOWN:
                    self.event_manager.emit_event(event)

            self.draw(self.game_title, self.button_list, self.menu_flag, self.background_color,
                      self.transparent_color, self.default_color)

        pygame.quit()

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
            self.button_list[self.menu_flag + 1].on_clicked()
        self.menu_flag %= 3

        # Update button hovered status based on menu_flag
        self.server_button.hovered = (self.menu_flag == 0)
        self.client_button.hovered = (self.menu_flag == 1)
        self.exit_button.hovered = (self.menu_flag == 2)

