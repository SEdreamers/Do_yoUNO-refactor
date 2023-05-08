from engine.game_object import GameObject

class Card(GameObject):
    def __init__(self, value, color, position, components=None):
        super().__init__(name, position, components)
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.color}_{self.value}"

    def __repr__(self):
        return self.__str__()

    def is_playable_on(self, other_card):
        return self.color == other_card.color or self.value == other_card.value or self.is_wild()

    def is_wild(self):
        return self.value == "wild" or self.value == "wild_draw_four"

    def get_action(self):
        if self.value in ["skip", "reverse", "draw2", "draw4", "wild", "wild_draw2", "wild_draw4"]:
            return self.value
        else:
            return None
    def on_clicked(self):
        # 함수 정의
        pass