import random
from UNO.engine.game_object import Listener
from card import Card

class Deck(Listener):
    def __init__(self):
        super().__init__()
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        colors = ["red", "green", "blue", "yellow"]
        values = [str(i) for i in range(0, 10)]
        skill_values = ["skip", "reverse", "draw2", "draw4"]
        colorless_values = ["wild", "wild_draw2", "wild_draw4"]

        deck = [Card(value, color) for value in values for color in colors] + \
               [Card(skill_value, color) for skill_value in skill_values for color in colors]

        # Add wild and wild_draw_four cards
        for _ in range(3):
            deck.append(Card('wild', 'black'))
            deck.append(Card('wild_draw2', 'black'))
            deck.append(Card('wild_draw4', 'black'))

        return deck

    def shuffle(self):
        random.shuffle(self.cards)
