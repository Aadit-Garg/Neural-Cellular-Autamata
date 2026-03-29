import pygame
import numpy as np
import vars
from vars import *

pygame.init()
screen = pygame.display.set_mode(vars.screen_size)
running = True
pixel_size = m.Vector2(screen_size.x / grid_size.x, screen_size.y / grid_size.y)

FPS = 60
clock = pygame.time.Clock()

