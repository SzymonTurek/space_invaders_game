import pygame, sys
from bullet import Bullet
from alien import Alien



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


def update_screen(ai_settings, screen, ship, aliens, bullets ):
    ship.draw_ship()
    aliens.draw(screen)
    pygame.display.flip()
    screen.blit(ai_settings.bg, (-300, -200))
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
    # Create an alien and place it in the row.
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

    