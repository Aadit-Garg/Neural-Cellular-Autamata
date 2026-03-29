import pygame
import numpy as np
import vars
from vars import *
from scipy import signal

kernel = np.array([[1,1,1],
                [1,1,1],
                [1,1,1]]) / 9

kernel2 = np.array([[-1, -1, -1],
                    [-1,  8, -1],
                    [-1, -1, -1]])

pygame.init()
main_screen = pygame.display.set_mode((1220,640))
panel = pygame.Surface((260,640))
screen = pygame.Surface(vars.screen_size)
screen2 = pygame.Surface((320,320))
screen3 = pygame.Surface((320,320))
font = pygame.font.SysFont('Monospace',24)
running = True

FPS = 60
clock = pygame.time.Clock()

def get_by_3(array, kernel,screen):
    arr = np.clip(signal.convolve2d(array, kernel, mode='same', boundary='fill', fillvalue=0), 0, 255).astype(np.uint8)
    render_filter(arr, screen)

def render_filter(arr, surface):
    rgb_array = np.stack((arr,arr,arr), axis=-1)
    small_surf = pygame.surfarray.make_surface(rgb_array)
    pygame.transform.scale(small_surf,(320,320), surface)

def generate_space():
    base = np.random.randint(0,256, grid_size, dtype=np.uint8)
    rgb_array = np.stack((base,base,base), axis = -1)

    small_surf = pygame.surfarray.make_surface(rgb_array)
    pygame.transform.scale(small_surf, screen_size, screen)
    return base

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
            get_by_3(base, kernel, screen2)
            get_by_3(base, kernel2, screen3)

    main_screen.blit(panel,(0,0))
    main_screen.blit(screen,(260,0))
    main_screen.blit(screen2,(900,0))
    main_screen.blit(screen3,(900,320))
    main_screen.blit(text_surf,(10,10))

    pygame.display.flip()


pygame.quit()