import pygame, sys
from classes import *
from game_functions import *
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Zobmie invasion")
    ship = Ship(screen)
    bullets = Group()
    

    running = True
    while running:
        check_typed_keys(ship, ai_settings,screen, bullets)
        ship.ship_position()
        
        update_screen(ai_settings, screen, ship, bullets)
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        #print(len(bullets))
        

        
        
run_game()

