
class Player:
    def __init__(self, name, model, screen):
        self.name = name
        self.screen = screen
        self.hand = []

    def play_card(self, card):
        self.hand.remove_card(card)

    def draw_card(self, deck):
        card = deck.draw_card()
        self.hand.add_card(card)

    def deal_cards(self, deck, num_cards):
        for _ in range(num_cards):
            card = deck.draw_card()
            self.hand.append(card)

    def get_hand(self):
        return self.hand.get_cards()

    def __str__(self):
        return self.name

    def count_cards(self):
        return len(self.hand.cards)


class Computer(Player):
    def __init__(self, name, model, screen):
        super().__init__(name, model, screen)

    def make_move(self, game_state):
        # Implement the logic for the computer to make a move based on the game state
        pass


class Human(Player):
    def __init__(self, name, model, screen):
        super().__init__(name, model, screen)

    def make_move(self, game_state):
        # Implement the logic for the human to make a move based on the game state
        # This can be done through input from the GameUI
        pass
