import pygame, sys

class Settings():

    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        #self.bg_color = (230, 230, 230)
        self.bg = pygame.image.load("images/space-bg.png")
       

    


class Ship():   
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("images/space-ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom  
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

     
    def ship_position(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
        elif self.moving_left == True and self.rect.left > 0:
            self.rect.centerx -= 5 
        elif self.moving_up == True and self.rect.top >0 :
            self.rect.centery -= 5 
        elif self.moving_down == True and self.rect.bottom < self.screen_rect.bottom :
            self.rect.centery += 5 

        


    
    