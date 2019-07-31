import pygame

def quit_function():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()