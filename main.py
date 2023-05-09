from scenes.lobby import Lobby
from models.model import Model

if __name__ == '__main__':
    model = Model()
    UNO = Lobby(model)
    UNO.run()
