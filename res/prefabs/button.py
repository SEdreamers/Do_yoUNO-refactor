import pygame

from engine.button import Button
from game.gameui import GameUI
from game.gamestate import GameState
from scenes.story import Story
import scenes.settings as sett


class SinglePlayer(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)
        self.model = model
        self.screen = screen

    def on_clicked(self):
        game_logic = GameState(self.model, self.screen)
        game_logic.add_human_player("Lou")
        game_logic.add_ai_player("comp1")
        for player in game_logic.players:
            player.deal_cards(game_logic.deck, 5)
        players = game_logic.players.copy()
        top_card = game_logic.draw_card()
        game = GameUI(self.model, self.screen, top_card, players, 0, 1)
        game.run()


class MultiPlayer(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)
        self.model = model
        self.screen = screen

    def on_clicked(self):
        game = GameUI(self.model, self.screen)
        game.run()

class StoryMode(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        story = Story(self.model)
        story.run()


class Settings(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        settings = sett.Settings(self.model, self.screen)
        settings.run()


class Exit(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        pass


class Blind(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)
    def on_clicked(self):
        self.model.color_blind_mode = not self.model.color_blind_mode
        self.model.save_data()


class Default(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen,x, y, width, height, font, color)
        self.screen = screen

    def on_clicked(self):
        self.model.screen_width = 800
        self.model.screen_height = 600
        self.model.color_blind_mode = False
        self.model.background_volume = 0.3
        self.model.total_volume = 0.3
        self.model.player_numbers = 3
        self.model.save_data()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))


class Back(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        pass


class Size(Button):
    def __init__(self, text, model, screen, size, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)
        self.size = size
        self.screen = screen
        self.size_list = [(400, 300), (600, 450), (800, 600), (1000, 750)]

    def on_clicked(self):
        self.model.screen_width = self.size_list[self.size - 1][0]
        self.model.screen_height = self.size_list[self.size - 1][1]
        self.model.save_data()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))


