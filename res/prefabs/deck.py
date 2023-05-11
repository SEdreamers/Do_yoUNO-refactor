import random
from res.prefabs.card import Card


class Deck:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        colors = ["red", "green", "blue", "yellow"]
        values = [str(i) for i in range(0, 10)]
        skill_values = ["skip", "reverse", "draw2", "draw4"]
        colorless_values = ["wild", "wild_draw2", "wild_draw4"]

        deck = [Card(self.model, self.screen, value, color) for value in values for color in colors] + \
               [Card(self.model, self.screen, skill_value, color) for skill_value in skill_values for color in colors]

        # Add wild and wild_draw_four cards
        for _ in range(3):
            for colorless in colorless_values:
                deck.append(Card(self.model, self.screen, colorless, 'black'))
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def play_card(self, card):
        self.cards.append(card)
        # self.cards.insert(0, card)

    def get_top_card(self):
        return self.cards[-1]
