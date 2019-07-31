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
        quit_function()
        screen.fill(ai_settings.bg_color)
        ship.draw_ship()
        pygame.display.flip()

run_game()

