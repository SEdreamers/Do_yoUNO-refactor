import random
from engine.sprites import Sprite
from res.prefabs.card import Card


class Deck(Sprite):
    def __init__(self, model, screen, image_path,  x, y, width, height):
        super().__init__(model, screen, image_path,  x, y, width, height)
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
            deck.append(Card(self.model, self.screen, 'wild', 'black'))
            deck.append(Card(self.model, self.screen, 'wild_draw2', 'black'))
            deck.append(Card(self.model, self.screen, 'wild_draw4', 'black'))

        return deck

    def shuffle(self):
        random.shuffle(self.cards)
