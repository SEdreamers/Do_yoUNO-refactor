import pygame

from engine.event import EventManager
from engine.button import Button
from game.gameui import GameUI
from game.gamelogic import GameLogic
from scenes.story import Story
import scenes.settings as sett
from engine.player import Human
from scenes.multiplay.multi import Multi
from scenes.multiplay.client_scene import ClientScene
from scenes.multiplay.server_scene import ServerScene
from game.play import MultiPlay
class SinglePlayer(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)
        self.model = model
        self.screen = screen

    def on_clicked(self):
        event_manager = EventManager()
        game_logic = GameLogic(self.model, self.screen, event_manager)
        game_logic.add_human_player("Lou")
        game_logic.add_ai_player("comp1")
        game_logic.add_ai_player("comp2")
        for player in game_logic.players:
            player.deal_cards(game_logic.deck, 5)
        players = game_logic.players.copy()

        game_ui = GameUI(self.model, self.screen, event_manager, game_logic.deck, players, 0, 1)

        running = True
        human_made_move = False  # Declare this outside the while loop
        computers_played = 0  # Track the number of computers that have played
        computer_event = pygame.USEREVENT + 1
        computer_turn_delay = 2000  # 2 seconds in milliseconds

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and isinstance(players[game_logic.current_turn], Human):
                    if event.button == 1:
                        event_manager.emit_event(event)
                        human_made_move = True
                        computers_played = 0
                        pygame.time.set_timer(computer_event, computer_turn_delay)  # schedule the computer turn
                elif event.type == computer_event and not isinstance(players[game_logic.current_turn], Human):
                    if human_made_move:
                        players[game_logic.current_turn].play_turn(game_logic, game_ui)
                        print("computer_played")
                        computers_played += 1
                        if computers_played % (len(players) - 1) == 0:
                            human_made_move = False
                        pygame.time.set_timer(computer_event, computer_turn_delay)
                game_ui.draw()


class MultiPlayer(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)
        self.model = model
        self.screen = screen

    def on_clicked(self):
        multi = Multi(self.model, self.screen)
        multi.run()


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


class ServerPlay(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        server_scene = ServerScene(self.model, self.screen)
        server_scene.run()


class ClientPlay(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        client_scene = ClientScene(self.model, self.screen)
        client_scene.run()

class GameStart(Button):
    def __init__(self, text, model, screen, x, y, width, height, font, color):
        super().__init__(text, model, screen, x, y, width, height, font, color)

    def on_clicked(self):
        pass








