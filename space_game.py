import pygame, sys


class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


class Ship():   
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("images/space-ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom  
    
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)




def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Zobmie invasion")
    ship = Ship(screen)
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.draw_ship()
        pygame.display.flip()

run_game()

