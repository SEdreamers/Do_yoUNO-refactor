import random
class Player:
    def __init__(self, name, model, screen):
        self.name = name
        self.model = model
        self.screen = screen
        self.hand = []

    def deal_cards(self, deck, num_cards):
        for _ in range(num_cards):
            card = deck.draw_card()
            self.hand.append(card)


    def __str__(self):
        return self.name

    def count_cards(self):
        return len(self.hand.cards)

    def serialize(self):
        return {
            'name': self.name,
            'hand': [card.__str__() for card in self.hand]
        }


class Computer(Player):
    def __init__(self, name, model, screen):
        super().__init__(name, model, screen)
        self.colors = ['red', 'green', 'blue', 'yellow']

    def choose_card_to_play(self, top_card):
        # Simple AI: play the first card that is playable
        for card in self.hand:
            if card.is_playable_on(top_card):
                if card.get_action() == 'wild' or card.get_action() == 'wild_draw4' or \
                        card.get_action() == 'wild_draw2':
                    card.color = random.choice(self.colors)
                return card
        # If no playable card is found, return None
        return None

    def play_turn(self, game_logic, game_ui):
        top_card = game_logic.deck.get_top_card()

        # Decide which card to play
        card_to_play = self.choose_card_to_play(top_card)
        if card_to_play is not None:
            game_logic.on_play_card(None, card_to_play)
        else:
            # If no playable card was found, draw a card
            game_logic.on_draw_card(None)
        game_ui.on_game_state_updated(game_logic.deck, game_logic.players, game_logic.current_turn,
                                      game_logic.direction)

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
