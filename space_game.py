import pygame, sys
from classes import *
from game_functions import *
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("UFO invasion")
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    #alien = Alien(ai_settings, screen)
    create_fleet(ai_settings, screen, aliens)
    running = True
    while running:
        check_typed_keys(ship, ai_settings,screen, bullets)
        ship.ship_position()
        
        update_screen(ai_settings, screen, ship, aliens, bullets)
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        

        
        
run_game()

