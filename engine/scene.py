import pygame
from engine.event_manager import EventManager


class Scene:
    def __init__(self, model):
        pygame.init()
        self.model = model
        self.event_manager = EventManager()
        # Subscribe event handlers
        self.event_manager.subscribe(pygame.MOUSEBUTTONDOWN, self.on_mouse_button_down)
        self.event_manager.subscribe(pygame.KEYDOWN, self.on_key_down)

    def run(self, event):
        # read event and create event object
        pass

    def draw(self, screen, title, button_list, menu_flag, background_color, transparent_color, default_color):
        screen.fill(background_color)
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Update button colors based on menu_flag and mouse position
        for idx, but in enumerate(button_list[1:]):
            but.color = transparent_color \
                if but.rect.collidepoint(mouse_pos) or menu_flag == idx else default_color
        # Draw buttons
        title.draw(screen)
        for but in button_list:
            but.draw(screen)

        pygame.display.flip()

    def change(self):
        # scene 바꿔주기
        pass

    def on_mouse_button_down(self, event):
        pass

    def on_key_down(self):
        pass
