import pygame
import numpy as np
import vars
from vars import *

pygame.init()
screen = pygame.display.set_mode(vars.screen_size)
running = True

FPS = 60
clock = pygame.time.Clock()


def generate_space():
    base = np.random.randint(0,256, grid_size, dtype=np.uint8)
    rgb_array = np.stack((base,base,base), axis = -1)

    small_surf = pygame.surfarray.make_surface(rgb_array)
    return pygame.transform.scale(small_surf, screen_size, screen)

while running:

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.KEYDOWN:
            generate_space()

    pygame.display.flip()


pygame.quit()