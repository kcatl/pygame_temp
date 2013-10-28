__author__ = 'Administrator'
background_image_file = 'background.bmp'
screen_size = (800, 600)
message = 'this is a message from python console'

import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode(screen_size, 0, 32)

font = pygame.font.SysFont('arial', 80)
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y = (screen_size[1] - text_surface.get_height()) / 2
