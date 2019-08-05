import pygame, sys

def check_typed_keys(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = True
            
            elif event.type == pygame.KEYUP:
                #if event.type == pygame.K_RIGHT:
                    ship.moving_right = False
                    ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    #screen.fill(ai_settings.bg_color)
    ship.draw_ship()
    pygame.display.flip()
    screen.blit(ai_settings.bg, (-300, -200))