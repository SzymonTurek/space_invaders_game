import pygame

def check_typed_keys(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    #screen.fill(ai_settings.bg_color)
    ship.draw_ship()
    pygame.display.flip()
    screen.blit(ai_settings.bg, (-300, -200))