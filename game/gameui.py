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
        computer_width = model.screen_width / 3.333
        computer_height = model.screen_height / 5
        self.deck_space = Sprite(model, screen, "res/images/green.jpg", 0, 0, model.screen_width,
                                 model.screen_height)
        self.hand_space = Sprite(model, screen, "res/images/skyblue.jpg", 0, model.screen_height * 0.6,
                                 self.model.screen_width - computer_width, model.screen_height * 0.4)
        self.computer_space = Sprite(model, screen, "res/images/black.jpg", model.screen_width - computer_width, 0,
                                     computer_width + 1, model.screen_width)
        self.back_card = Sprite(model, screen, "res/images/cards/back_0.png", model.screen_width * 0.2,
                                model.screen_height * 0.2, model.screen_width / 11, model.screen_height / 8)
        self.top_card.rect = (model.screen_width * 0.4, model.screen_height * 0.2, model.screen_width / 11,
                              model.screen_height / 8)
        self.color_boxes = {
            "blue": Sprite(model, screen, "res/images/color_boxes/default/blue_box.png", self.model.screen_width / 25,
                           self.model.screen_height, self.model.screen_width / 8, self.model.screen_width / 2),
            "green": Sprite(model, screen, "res/images/color_boxes/default/green_box.png", self.model.screen_width / 25,
                            self.model.screen_height, self.model.screen_width / 8, self.model.screen_width / 2),
            "yellow": Sprite(model, screen, "res/images/color_boxes/default/yellow_box.png",
                             self.model.screen_width / 25, self.model.screen_height, self.model.screen_width / 8,
                             self.model.screen_width / 2),
            "red": Sprite(model, screen, "res/images/color_boxes/default/red_box.png", self.model.screen_width / 25,
                          self.model.screen_height, self.model.screen_width / 8, self.model.screen_width / 2),
            "black": Sprite(model, screen, "res/images/color_boxes/black_box.png", self.model.screen_width / 25,
                          self.model.screen_height, self.model.screen_width / 8, self.model.screen_width / 2)
        }


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
        print(self.top_card.rect)
        self.screen.blit(self.top_card.image, self.top_card.rect)
        self.screen.blit(self.color_boxes[self.top_card.color].image, self.color_boxes[self.top_card.color].rect)
        pygame.display.flip()

    def handout_cards(self, nums):
        pass


