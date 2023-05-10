import pygame
from engine.scene import Scene
from engine.sprites import Sprite
from res.prefabs.deck import Deck


class GameUI(Scene):
    def __init__(self, model, screen, top_card, players, current_turn, direction):
        super().__init__(model, screen)
        self.top_card = top_card
        self.players = players
        self.current_turn = current_turn
        self.direction = direction
        self.running = True
        computer_width = self.model.screen_width / 3.333
        computer_height = self.model.screen_height / 5
        self.deck_space = Sprite(model, screen, "res/images/green.jpg", 0, 0, self.model.screen_width,
                                 self.model.screen_height)
        self.hand_space = Sprite(model, screen, "res/images/skyblue.jpg", 0, self.model.screen_height * 0.6,
                                 self.model.screen_width - computer_width, self.model.screen_height * 0.4)
        self.computer_space = Sprite(model, screen, "res/images/black.jpg", self.model.screen_width - computer_width, 0,
                                     computer_width + 1, self.model.screen_width)
        self.back_card = Sprite(model, screen, "res/images/cards/default_mode/back_0.png",
                                self.model.screen_width * 0.2, self.model.screen_height * 0.2,
                                self.model.screen_width / 10, self.model.screen_height / 10)
    def run(self):
        while self.running:
            self.draw()

    def handle_events(self):
        pass

    def on_mouse_button_down(self, event):
        pass

    def on_key_down(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.deck_space.image, self.deck_space.rect)
        self.screen.blit(self.hand_space.image, self.hand_space.rect)
        self.screen.blit(self.computer_space.image, self.computer_space.rect)
        self.screen.blit(self.back_card.image, self.back_card.rect)
        pygame.display.flip()

    def handout_cards(self, nums):
        pass

