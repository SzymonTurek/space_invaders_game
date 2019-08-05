import pygame, sys
from classes import *
from game_functions import *



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Zobmie invasion")
    ship = Ship(screen)
    
    

    running = True
    while running:
        check_typed_keys(ship)
        update_screen(ai_settings, screen, ship)
        
        
run_game()

