import json

class Model:
    def __init__(self):
        self.game_data_path = "models/game_data.json"
        self.color_blind_mode = False
        self.screen_width = 800
        self.screen_height = 600
        self.total_volume = 0.3
        self.background_volume = 0.3
        self.player_numbers = 3
        self.load_data()

    def load_data(self):
        try:
            with open(self.game_data_path, 'r') as game_file:
                file_content = game_file.read()
                if not file_content:
                    # If the file is empty, create default data
                    self.save_data()
                else:
                    try:
                        data = json.loads(file_content)
                        self.color_blind_mode = data['color_blind_mode']
                        self.screen_width = data['screen_width']
                        self.screen_height = data['screen_height']
                        self.total_volume = data['total_volume']
                        self.background_volume = data['background_volume']
                        self.player_numbers = data['player_numbers']
                    except json.JSONDecodeError:
                        # If the JSON is invalid, create default data
                        self.save_data()
        except FileNotFoundError:
            self.save_data()

    def save_data(self):
        data = {
            'color_blind_mode': self.color_blind_mode,
            'screen_width': self.screen_width,
            'screen_height': self.screen_height,
            'total_volume': self.total_volume,
            'background_volume': self.background_volume,
            'player_numbers': self.player_numbers 
        }
        with open(self.game_data_path, 'w') as game_file:
            json.dump(data, game_file)
