import pygame
class Game:
    def __init__(self):
        self.running = True 
    
    def start():
        while self.running:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_game() 
                    self.running = False
        
