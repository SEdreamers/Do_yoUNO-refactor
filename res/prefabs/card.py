from engine.sprites import Sprite


class Card(Sprite):
    def __init__(self, model, value, color, x, y, width, height):
        if self.model.color_blind_mode:
            image_path = f'res/images/cards/color_blind_mode/{color}_{value}'
        else:
            image_path = f'res/images/cards/default_mode/{color}_{value}'
        super().__init__(image_path, model, x, y, width, height)
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

    # update when color_blind_mode changes
    def update(self):
        pass