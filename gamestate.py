from res.prefabs.deck import Deck
from engine.player import Human, Computer


class GameState:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.current_turn = 0
        self.direction = 1  # 1 for forward, -1 for reverse

    def add_player(self, player):
        self.players.append(player)

    def add_ai_player(self):
        ai_player = Computer("AI Player")
        self.players.append(ai_player)

    def next_turn(self):
        self.current_turn = (self.current_turn + self.direction) % len(self.players)

    def reverse_direction(self):
        self.direction *= -1

    def play_card(self, player, card):
        # Implement the logic to play a card
        # ...
        pass