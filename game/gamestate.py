from res.prefabs.deck import Deck
from engine.player import Human, Computer


class GameState:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        self.deck = Deck(model, screen)
        self.players = []
        self.current_turn = 0
        self.direction = 1  # 1 for forward, -1 for reverse

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

    def play_card(self, player, card):
        current_card = self.deck.get_top_card()

        # Check if the card is valid to play
        if card.is_playable_on(current_card):
            player.play_card(card)
            self.deck.draw_card(card)

            # Perform card actions
            card_action = card.get_action()
            if card_action == "skip":
                self.next_turn()
            elif card_action == "draw_two":
                next_player = self.players[self.current_turn]
                for _ in range(2):
                    next_player.draw_card(self.deck)
                self.next_turn()
            elif card_action == "reverse":
                self.reverse_direction()
                self.next_turn()
            elif card_action == "wild":
                # Implement color selection logic
                pass
            elif card_action == "wild_draw_four":
                # Implement color selection logic
                next_player = self.players[self.current_turn]
                for _ in range(4):
                    next_player.draw_card(self.deck)
                self.next_turn()
            else:
                self.next_turn()
        else:
            print("Invalid card!")

