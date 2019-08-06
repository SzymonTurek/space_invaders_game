import pygame, sys
from bullet import Bullet



def check_typed_keys(ship,ai_settings, screen, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_UP:
                    ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    if len(bullets) < ai_settings.bullets_allowed:
                        new_bullet = Bullet(ai_settings, screen, ship)
                        bullets.add(new_bullet)
                elif event.key == pygame.K_q:
                    sys.exit()
            
            elif event.type == pygame.KEYUP:
                    ship.moving_right = False
                    ship.moving_left = False
                    ship.moving_up = False
                    ship.moving_down = False


def update_screen(ai_settings, screen, ship, alien, bullets ):
    ship.draw_ship()
    alien.blitme()
    pygame.display.flip()
    screen.blit(ai_settings.bg, (-300, -200))
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    