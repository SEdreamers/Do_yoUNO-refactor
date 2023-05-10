from network.client import Client
from models.model import Model
from network.server import Server
model = Model()

# server = Server("192.168.35.246", 5555)
# server.start()

client = Client("192.168.35.246", 5555, model, None)
data = {"event_type": "receive", "card": "red_5"}
client.connect()
client.send_data(data)