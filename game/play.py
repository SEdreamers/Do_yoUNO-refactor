class Play:
    def __init__(self, game_state):
        self.game_state = game_state

    def play(self):
        pass


class SinglePlay(Play):
    def __init__(self, game_state, game_ui):
        super().__init__(game_state)
        self.game_ui = game_ui

    def play(self):
        self.game_state.single_play("Human Player")
        self.game_ui.run()


class MultiPlay(Play):
    def __init__(self, game_state, game_ui, client):
        super().__init__(game_state)
        self.game_ui = game_ui
        self.client = client

    def play(self):
        self.client.connect()
        self.game_ui.run()
