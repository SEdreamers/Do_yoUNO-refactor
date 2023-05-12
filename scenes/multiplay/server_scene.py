import pygame
from engine.scene import Scene
from res.prefabs.inputbox import InputBox
from network.server import Server
import res.prefabs.button as button
import threading


class ServerScene(Scene):
    def __init__(self, model, screen):
        super().__init__(model, screen)
        self.running = True
        self.input_box = InputBox(100, 100, 200, 32)
        self.click_box = InputBox(100, 300, 140, 32)
        self.font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        self.clock = pygame.time.Clock()
        self.server = None
        self.done = False
        self.start_button = button.GameStart("Start", self.model, self.screen, 100, 400, 50, 50, self.font,
                                             (255, 255, 255))

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
                    if self.start_button.rect.collidepoint(event.pos):
                        try:
                            self.server.send_game_state()
                            print(f"{self.server.clients}")
                        except Exception as e:
                            print(f"An error occurred when sending the 'game_start' event: {e}")
            self.screen.fill((30, 30, 30))
            box.draw(self.screen)
            self.click_box.draw(self.screen)
            self.start_button.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

    def submit(self):
        try:
            ip, port = self.input_box.submitted.split(":")
            self.server = Server(ip, port, self.screen, self.model, self.event_manager)
            threading.Thread(target=self.server.start).start()
        except Exception as e:
            print(f"An error occurred when starting the server: {e}")




