import socket
import json


class Client:
    def __init__(self, ip, port, model, screen):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.game = GameUI(model, screen)

    def connect(self):
        try:
            self.sock.connect((self.ip, self.port))
            return True
        except socket.error as e:
            print(str(e))
            return False

    def send_data(self, data):
        try:
            self.sock.sendall(json.dumps(data).encode())
        except socket.error as e:
            print(str(e))

    def receive_data(self):
        try:
            data = self.sock.recv(2048).decode()
            return json.loads(data)
        except socket.error as e:
            print(str(e))

    def load_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    def modify_and_save_json(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
