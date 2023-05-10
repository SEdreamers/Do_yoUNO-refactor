import socket
import threading
import json

class Server:
    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.server.bind((ip, port))
        self.clients = []
        # self.deck
        # self.game

    def start(self):
        self.server.listen()
        print(f"Server is listening on {self.ip}:{self.port}")

        while True:
            conn, addr = self.server.accept()
            print(f"New connection from {addr}")

            self.clients.append(conn)
            client_thread = threading.Thread(target=self.handle_client, args=(conn,))
            client_thread.start()

    def handle_client(self, conn):
        connected = True

        while connected:
            try:
                data = conn.recv(1024)
                if data:
                    self.process_data(json.loads(data.decode()), conn)
                else:
                    connected = False
            except:
                connected = False

        self.clients.remove(conn)
        conn.close()

    def process_data(self, data, sender):
        if "event_type" not in data:
            print("Invalid message format")
            return

        print(f"Received message: {data['event_type']}")
        self.broadcast({"type": "text", "event_type": f"From client: {data['event_type']}"}, sender)

        # elif data["type"] == "game_action":
        #     action = data["action"]
        #     # Process the game action, update the game state, and broadcast the changes
        #     # e.g., self.game.perform_action(action)
        #     # self.broadcast({"type": "game_update", "state": self.game.state}, sender)

    def broadcast(self, data, sender=None):
        for client in self.clients:
            if client != sender:
                client.send(json.dumps(data).encode())
