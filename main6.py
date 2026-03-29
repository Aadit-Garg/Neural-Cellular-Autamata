import pygame
import numpy as np
import vars
# from cython import *
from vars import *

pygame.init()
main_screen = pygame.display.set_mode((900,640))
panel = pygame.Surface((260,640))
screen = pygame.Surface(vars.screen_size)
font = pygame.font.SysFont('Monospace',24)
running = True

w1 = np.random.randn(9,16)*0.1
w2 = np.random.randn(16,1)*0.1

FPS = -1
clock = pygame.time.Clock()


def generate_space(base = np.random.randint(0,256, grid_size, dtype=np.uint8)):
    
    rgb_array = np.stack((base,base,base), axis = -1)

    small_surf = pygame.surfarray.make_surface(rgb_array)
    pygame.transform.scale(small_surf, screen_size, screen)
    return base

def get_neighbour(base,x,y):
    padding_grid = np.pad(base, pad_width=((1,1),(1,1)), mode = 'wrap')
    patch = padding_grid[x:x+3,y:y+3]
    vector = patch.flatten()
    # print(vector)

    return vector

def forward_pass(vector, w1,w2):
    hidden = np.dot(vector,w1)
    hidden_activated = np.maximum(0,hidden)
    output = np.dot(hidden_activated,w2)
    # output = np.clip(output,0,255)
    return output
    # print(output)
panel.fill((150,150,150))
new_grid = np.random.randint(0,256, grid_size, dtype=np.uint8)
while running:

    clock.tick(FPS)

    text_surf = font.render(f"FPS:{clock.get_fps():.2f}", True, (10,50,150))
    # pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            w1 = np.random.randn(9,16)*0.1
            w2 = np.random.randn(16,1)*0.1

    
    base = generate_space(new_grid)
    new_grid = base.copy()
    
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            
            # A. Get what the cell sees
            vector = get_neighbour(base, x, y)
            
            # B. Get AI's prediction
            delta = forward_pass(vector, w1, w2)
            
            # C. The Delta Update: Current State + Prediction
            # delta[0] because the output shape is (1,)
            new_val = base[x, y] + delta[0]*0.1
            # D. Clamp to valid colors and save to the NEW grid
            new_grid[x, y] = np.clip(new_val, 0, 255)
                
    main_screen.blit(panel,(0,0))
    main_screen.blit(screen,(260,0))
    main_screen.blit(text_surf,(10,10))

    pygame.display.flip()


pygame.quit()