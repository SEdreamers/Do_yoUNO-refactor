import socket
import threading
import json
from game.gamelogic import GameLogic
from engine.player import Player
class Server:
    def __init__(self, host, port, model, screen, event_manager):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, int(port)))
        self.model = model
        self.screen = screen
        self.event_manager = event_manager
        self.sock.listen(1)
        self.game_logic = GameLogic(self.screen, self.model, self.event_manager)
        self.clients = []

    def send_game_state(self):
        hands = []
        for player in self.game_logic.players:
            hand = [card.__str__() for card in player.hand]
            hands.append(hand)
        state = {
            'name': [player.name for player in self.game_logic.players],
            'deck': self.game_logic.deck.to_list(),  # Assuming your Deck class has a serialize method
            'players': hands,
            'turn_num': '0',
            'direction': '1'
        }
        data = self.serialize_data(state)
        self.broadcast(data)

    def broadcast(self, msg):
        for client in self.clients:
            client.sendall(msg)

    def handle_client(self, client):
        msg = client.recv(1024)
        msg = json.loads(msg.decode('utf-8'))
        self.event_manager.emit_type(msg['event'], msg['card'])
        print(msg)
        self.broadcast(msg)

    def start(self):
        print("Server started...")
        while True:
            client, addr = self.sock.accept()
            print("server_working")
            self.clients.append(client)
            # self.game_logic.players.append("")
            print(client.getpeername())

            threading.Thread(target=self.handle_client, args=(client,)).start()

    def serialize_data(self, data):
        return json.dumps(data).encode('utf-8')

    def deserialize_data(self, data):
        return json.loads(data.decode('utf-8'))
