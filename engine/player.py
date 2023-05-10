from hand import Hand


class Player:
    def __init__(self, name, model, screen, deck):
        self.name = name
        self.screen = screen
        self.hand = Hand(model, screen, deck)

    def get_hand(self):
        return self.hand

    def count_cards(self):
        return len(self.hand.cards)


class Human(Player):
    def __init__(self):
        super().__init__()


class Computer(Player):
    def __init__(self):
        super().__init__()