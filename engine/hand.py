class Hand:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def get_cards(self):
        return self.cards

    def get_card_count(self):
        return len(self.cards)

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])



