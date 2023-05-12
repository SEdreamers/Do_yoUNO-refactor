import pygame

from res.prefabs.deck import Deck
from engine.player import Human, Computer


class GameLogic:
    def __init__(self, model, screen, event_manager):
        self.model = model
        self.screen = screen
        self.event_manager = event_manager
        self.deck = Deck(model, screen)
        self.players = []
        self.current_turn = 0
        self.direction = 1  # 1 for forward, -1 for reverse
        self.back_card = pygame.Rect(model.screen_width * 0.2,
                                     model.screen_height * 0.2, model.screen_width / 11, model.screen_height / 7)
        self.uno_btn = pygame.Rect(model.screen_width * 0.55,
                                   model.screen_height * 0.285, model.screen_width / 14, model.screen_height / 18)
        self.event_manager.subscribe('play_card', self.on_play_card)
        self.event_manager.subscribe('back_card', self.on_draw_card)
        self.event_manager.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_button_down)

    def add_human_player(self, name):
        human_player = Human(self.model, self.screen, name)
        self.players.append(human_player)

    def add_ai_player(self, name):
        ai_player = Computer(self.model, self.screen, name)
        self.players.append(ai_player)

    def next_turn(self):
        self.current_turn = (self.current_turn + self.direction) % len(self.players)

    def reverse_direction(self):
        self.direction *= -1

    def draw_card(self):
        return self.deck.draw_card()

    def on_draw_card(self, event):
        print(f"Handling back_card event: {event}")
        card = self.draw_card()
        self.players[self.current_turn].hand.append(card)
        self.next_turn()
        print(self.players[self.current_turn - 1].hand)

    def on_play_card(self, event, card):
        self.deck.cards = self.deck.cards[1:] + [self.deck.cards[0]]
        self.deck.play_card(card)
        self.players[self.current_turn].hand.remove(card)

        # Perform card actions
        card_action = card.get_action()
        if card_action == "skip":
            self.next_turn()
        elif card_action == "draw_two":
            next_player = self.players[(self.current_turn + self.direction) % len(self.players)]
            for _ in range(2):
                next_player.draw_card(self.deck)
            self.next_turn()
        elif card_action == "reverse":
            self.reverse_direction()
            self.next_turn()
        # elif card_action == "wild":
        #     # Implement color selection logic
        #     # if isinstance(self.players[self.current_turn], Human):
        #     color = self.prompt_for_color()
        #     card.set_color(color)
        #     # else:
        #     #     card.set_color(self.players[self.current_turn].choose_color())
        #     self.next_turn()
        # elif card_action == "wild_draw_four":
        #     # Implement color selection logic
        #     color = self.prompt_for_color()
        #     card.set_color(color)
        #     next_player = self.players[(self.current_turn + self.direction) % len(self.players)]
        else:
            self.next_turn()
        print(self.players[self.current_turn - 1].hand)

    def update(self):
        # Check if any player has emptied their hand and won the game
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} has won the game!")
                # Emit a 'game_over' event
                self.event_manager.emit('game_over', winner=player.name)

    def on_mouse_button_down(self, event):
        x, y = event.pos
        if self.back_card.collidepoint(x, y):
            self.event_manager.emit_type('back_card', event)
            self.update_state()

        # Check if any card in player's hand is clicked
        for card in reversed(self.players[0].hand):
            if card.rect.collidepoint(x, y):
                if self.deck.cards[0].is_playable_on(card):
                    self.event_manager.emit_type('play_card', event, card)
                    self.update_state()
                    break

        # Check if uno button is clicked
        if self.uno_btn.collidepoint(x, y):
            # Perform whatever action you want to do when uno button is clicked
            pass

    # def prompt_for_color(self):
    #     colors = ['red', 'green', 'blue', 'yellow']
    #     color_buttons = {color: pygame.Rect(x * 100, 0, 100, 100) for x, color in enumerate(colors)}
    #
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False
    #             elif event.type == pygame.MOUSEBUTTONDOWN:
    #                 for color, rect in color_buttons.items():
    #                     if rect.collidepoint(event.pos):
    #                         return color

    def update_state(self):
        self.event_manager.emit_type('game_state_updated', self.deck, self.players, self.current_turn, self.direction)


