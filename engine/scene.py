import pygame
from engine.event import EventManager


class Scene:
    def __init__(self, model, screen):
        pygame.init()
        self.model = model
        self.screen = screen
        self.event_manager = EventManager()
        # Subscribe event handlers
        self.event_manager.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_button_down)
        self.event_manager.subscribe(pygame.KEYDOWN, self.on_key_down)

    def run(self, event):
        # read event and create event object
        pass

    def draw(self, title, button_list, menu_flag, background_color, transparent_color, default_color):
        self.screen.fill(background_color)
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Update button colors based on menu_flag and mouse position
        for idx, but in enumerate(button_list[1:]):
            but.color = transparent_color \
                if but.rect.collidepoint(mouse_pos) or menu_flag == idx else default_color
        # Draw buttons
        title.draw(self.screen)
        for but in button_list:
            but.draw(self.screen)

        pygame.display.flip()

    def change(self):
        # scene 바꿔주기
        pass

    def on_mouse_button_down(self, event):
        pass

    def on_key_down(self, event):
        pass
