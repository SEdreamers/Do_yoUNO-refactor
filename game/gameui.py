import pygame
from engine.scene import Scene
from engine.sprites import Sprite
from engine.button import Button


class GameUI(Scene):
    def __init__(self, model, screen, event_manager, deck, players, current_turn, direction):
        super().__init__(model, screen)
        self.event_manager = event_manager
        self.deck = deck
        print(type(deck))
        self.top_card = deck.get_top_card()
        self.players = players
        self.current_turn = current_turn
        self.direction = direction
        self.running = True

        font = pygame.font.SysFont("arial", self.model.screen_width // 20, True)
        self.computer_width = model.screen_width / 3.2
        self.computer_height = model.screen_height / 5
        self.deck_space = Sprite(model, screen, "res/images/green.jpg", 0, 0, model.screen_width,
                                 model.screen_height)
        self.hand_space = Sprite(model, screen, "res/images/skyblue.jpg", 0, model.screen_height * 0.6,
                                 self.model.screen_width - self.computer_width, model.screen_height * 0.4)
        self.computer_space = Sprite(model, screen, "res/images/black.jpg", model.screen_width - self.computer_width, 0,
                                     self.computer_width, model.screen_width)
        self.back_card = Sprite(model, screen, "res/images/cards/back_0.png", model.screen_width * 0.2,
                                model.screen_height * 0.2, model.screen_width / 11, model.screen_height / 7)
        self.top_card.set_pos(model.screen_width * 0.4, model.screen_height * 0.2)
        self.color_boxes = {
            "blue": Sprite(model, screen, "res/images/color_boxes/default/blue_box.png", model.screen_width * 0.55,
                           model.screen_height * 0.2, model.screen_width / 20, model.screen_height / 20),
            "green": Sprite(model, screen, "res/images/color_boxes/default/green_box.png",
                            model.screen_width * 0.55, model.screen_height * 0.2,
                            model.screen_width / 20, model.screen_height / 20),
            "yellow": Sprite(model, screen, "res/images/color_boxes/default/yellow_box.png",
                             model.screen_width * 0.55, model.screen_height * 0.2,
                             model.screen_width / 20, model.screen_height / 20),
            "red": Sprite(model, screen, "res/images/color_boxes/default/red_box.png", model.screen_width * 0.55,
                          model.screen_height * 0.2, model.screen_width / 20, model.screen_height / 20),
            "black": Sprite(model, screen, "res/images/color_boxes/black_box.png", model.screen_width * 0.55,
                            model.screen_height * 0.2, model.screen_width / 20, model.screen_height / 20)
        }
        self.uno_btn = Sprite(model, screen, "res/images/uno_btn.png", model.screen_width * 0.55,
                              model.screen_height * 0.285, model.screen_width / 14, model.screen_height / 18)
        self.object_list = [self.deck_space, self.hand_space, self.computer_space, self.back_card, self.uno_btn]
        for idx, card in enumerate(self.players[0].hand):
            card.set_pos(model.screen_width / 40 + idx * model.screen_width / 20, model.screen_height * 0.63)
        self.computer_back_card = Sprite(model, screen, "res/images/cards/back_0.png", 0,
                                         0, model.screen_width / 11, model.screen_height / 7)
        self.human_len_text = Button("0", model, screen, self.model.screen_width - self.computer_width -
                                     self.model.screen_width / 50, self.model.screen_height -
                                     self.model.screen_width / 50, 0, 0, font, (0, 0, 0))
        self.com_len_text = Button("0", model, screen, 0, 0, 0, 0, font, (0, 0, 255))

        self.card_flag = 0
        self.event_manager.subscribe('game_state_updated', self.on_game_state_updated)

    def set_card_pos(self):
        for idx, card in enumerate(self.players[0].hand):
            card.set_pos(self.model.screen_width / 40 + idx * self.model.screen_width / 20,
                         self.model.screen_height * 0.63)

    def on_game_state_updated(self, deck, players, current_turn, direction):
        self.deck = deck
        self.top_card = self.deck.cards[0]
        self.top_card.set_pos(self.model.screen_width * 0.4, self.model.screen_height * 0.2)
        self.players = players
        self.current_turn = current_turn
        self.direction = direction
        self.set_card_pos()

    def draw(self):
        for obj in self.object_list:
            obj.draw(self.screen)
        self.top_card.draw(self.screen)
        self.color_boxes[self.top_card.color].draw(self.screen)

        for idx, card in enumerate(self.players[0].hand):
            card.draw(self.screen)
        for i in range(1, len(self.players)):
            pygame.draw.line(self.screen, (255, 255, 255), (int(self.model.screen_width - self.computer_width),
                                                            i * int(self.computer_height)),
                             (int(self.model.screen_width), i * int(self.computer_height)),
                             int(self.model.screen_width / 120))
        interval = self.model.screen_width / 50
        for idx, player in enumerate(self.players[1:]):
            card_num = len(player.hand)
            for j in range(card_num):
                self.computer_back_card.set_pos(self.model.screen_width - self.computer_width + interval * (j + 1),
                                                idx * self.computer_height + interval)
                self.computer_back_card.draw(self.screen)
            self.com_len_text.change_text(f"{card_num}")
            self.com_len_text.set_pos(self.model.screen_width - interval,
                                      idx * self.computer_height + interval)
            self.com_len_text.draw(self.screen)

        self.human_len_text.change_text(f"{len(self.players[0].hand)}")
        self.human_len_text.draw(self.screen)

        pygame.display.flip()




