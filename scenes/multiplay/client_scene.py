import pygame
from engine.scene import Scene
from res.prefabs.inputbox import InputBox
from network.client import Client


class ClientScene(Scene):
    def __init__(self, model, screen):
        super().__init__(model, screen)
        self.running = True
        self.input_box = InputBox(100, 100, 140, 32)
        self.click_box = InputBox(100, 300, 140, 32)
        self.clock = pygame.time.Clock()
        self.done = False
        self.client = None
        # self.event_manager.subscribe('start_game', self.on_mouse_button_down)

    def run(self):
        while not self.done:
            box = self.input_box
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                box.handle_event(event)
                box.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click_box.rect.collidepoint(event.pos):
                        print("ok")
                        self.submit()

            self.screen.fill((30, 30, 30))
            box.draw(self.screen)
            self.click_box.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

    def submit(self):
        ip, port = self.input_box.submitted.split(":")
        self.client = Client(ip, port, self.model, self.screen, self.event_manager, "name")
        if self.client.game_ui is not None:
            self.client.start_game()






