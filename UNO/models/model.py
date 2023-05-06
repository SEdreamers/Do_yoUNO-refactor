import json


class Model:
    def __init__(self, data_file='game_data.json'):
        self.data_file = data_file
        self.color_blind_mode = False
        self.screen_width = 800
        self.screen_height = 600
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as game_file:
                data = json.load(game_file)
                self.color_blind_mode = data['color_blind_mode']
                self.screen_width = data['screen_width']
                self.screen_height = data['screen_height']
        except FileNotFoundError:
            self.save_data()

    def save_data(self):
        data = {
            'color_blind_mode': self.color_blind_mode,
            'screen_width': self.screen_width,
            'screen_height': self.screen_height
        }
        with open(self.data_file, 'w') as game_file:
            json.dump(data, game_file)