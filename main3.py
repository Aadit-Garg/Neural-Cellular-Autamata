import pygame
import numpy as np
import vars
from vars import *

pygame.init()
main_screen = pygame.display.set_mode((900,640))
panel = pygame.Surface((260,640))
screen = pygame.Surface(vars.screen_size)
font = pygame.font.SysFont('Monospace',24)
running = True

FPS = 60
clock = pygame.time.Clock()


def generate_space():
    base = np.random.randint(0,256, grid_size, dtype=np.uint8)
    rgb_array = np.stack((base,base,base), axis = -1)

    small_surf = pygame.surfarray.make_surface(rgb_array)
    pygame.transform.scale(small_surf, screen_size, screen)
    return base

def get_neighbour(base,x,y):
    padding_grid = np.pad(base, pad_width=1, model = 'wrap')
    patch = padding_grid[x:x+3,y:y+3]
    vector = patch.flatten()
    return vector
    
panel.fill((150,150,150))

while running:
    clock.tick(FPS)

    text_surf = font.render(f"FPS:{clock.get_fps():.2f}", True, (10,50,150))
    # pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.KEYDOWN:
            base = generate_space()
            get_neighbour(base,20,20)

    main_screen.blit(panel,(0,0))
    main_screen.blit(screen,(260,0))
    main_screen.blit(text_surf,(10,10))

    pygame.display.flip()


pygame.quit()