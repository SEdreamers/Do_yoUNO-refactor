from engine.sprites import Sprite


class Card(Sprite):
    def __init__(self, model, screen, value, color):
        if model.color_blind_mode:
            image_path = f'res/images/cards/color_blind_mode/{color}_{value}.png'
        else:
            image_path = f'res/images/cards/default_mode/{color}_{value}.png'
        super().__init__(model, screen, image_path, 0, 0, model.screen_width / 11, model.screen_height / 7)
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.color}_{self.value}"

    def __repr__(self):
        return self.__str__()

    def is_playable_on(self, other_card):
        return self.color == other_card.color or self.value == other_card.value or self.is_wild()

    def is_wild(self):
        return self.value == "wild" or self.value == "wild_draw4" or self.value == "wild_draw2"

    def get_action(self):
        if self.value in ["skip", "reverse", "draw2", "draw4", "wild", "wild_draw2", "wild_draw4"]:
            return self.value
        else:
            return None

    @classmethod
    def from_str(cls, model, screen, data):
        color, value = data.split('_')
        return cls(model, screen, value, color)

    # update when color_blind changes
    def update_mode(self):
        pass
