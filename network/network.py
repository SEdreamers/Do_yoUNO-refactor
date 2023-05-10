import socket

class Network:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_server_socket(self):
        # Create a server socket and return it
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        return server_socket

    def create_client_socket(self):
        # Create a client socket and return it
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client_socket

    def send_message(self, sock, message):
        # Send a message over the socket
        # ...
        pass

    def receive_message(self, sock):
        # Receive a message from the socket
        # ...
        pass
