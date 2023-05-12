import pygame
import socket
import json
from game.gameui import GameUI
from res.prefabs.card import Card
from res.prefabs.deck import Deck
from engine.player import Player
import threading

class Client:
    def __init__(self, host, port, model, screen, event_manager, name):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = int(port)
        self.sock.connect((self.host, self.port))
        self.name = name
        print(f"Client started on {self.host}:{self.port}")
        self.running = False
        # Initialize pygame and the game display here...
        self.model = model
        self.screen = screen
        self.event_manger = event_manager
        self.game_ui = None
        self.initialize_game_state()
        self.game_thread = threading.Thread(target=self.game_loop)
        self.game_thread.daemon = True

    def game_loop(self):
        while self.running:
            print("2222")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if self.game_ui.back_card.collidepoint(x, y):
                            data = {'event': 'back_card'}
                            send_data = self.serialize_data(data)
                            self.sock.send(send_data)
                        # Check if any card in player's hand is clicked
                        for card in reversed(self.game_ui.players[0].hand):
                            if card.rect.collidepoint(x, y):
                                if self.game_ui.deck.cards[0].is_playable_on(card):
                                    data = {'event': 'play_card', 'card': card.__str__()}
                                    send_data = self.serialize_data(data)
                                    self.sock.send(send_data)
                                    break

            self.receive_update()
            # Draw the current game state to the screen...
            self.game_ui.draw()

    def send_action(self, action):
        self.sock.send(self.serialize_data((self.player, action)))

    def receive_update(self):
        data = self.sock.recv(1024)
        state = self.deserialize_data(data)
        self.handle_update(state)

    def handle_update(self, state):
        if state['event'] == 'play_card':
            card = state['card']
            real_card = self.game_ui.deck.find_card(card)
            self.game_ui.players[self.game_ui.current_turn].hand.remove(real_card)
            self.game_ui.deck.play_card(real_card)
        elif state['event'] == 'back_card':
            card = self.game_ui.deck.draw_card()
            self.game_ui.players[self.game_ui.current_turn].hand.append(card)

    def initialize_game_state(self):
        data = self.sock.recv(1024)
        msg = self.deserialize_data(data)
        print(msg)
        deck = Deck.from_list(self.model, self.screen, msg['deck'])
        print(type(deck))
        players = []
        for player_data in msg['players']:
            hand = [Card.from_str(self.model, self.screen, card) for card in player_data]
        player = Player(msg['name'][0])
        player.hand = hand
        players.append(player)
        self.game_ui = GameUI(self.model, self.screen, self.event_manger, deck, players,  int(msg['turn_num']),
                              int(msg['direction']))
        print("11111")
        self.game_ui.draw()

    def start_game(self):
        self.running = True
        self.game_thread.start()

    def serialize_data(self, data):
        return json.dumps(data).encode('utf-8')

    def deserialize_data(self, data):
        return json.loads(data.decode('utf-8'))

