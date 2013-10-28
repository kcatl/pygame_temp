#message for action
__author__ = 'Administrator'
screen_size = (800, 600)
message = 'this is a message from the python console  '
background_image_filename = 'background.jpg'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode(screen_size, 0, 32)

font = pygame.font.SysFont('arial', 80)
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y = (screen_size[1] - text_surface.get_height()) / 2
fullscreen = False
background = pygame.image.load(background_image_filename)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode(screen_size, FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode(screen_size, 0, 32)



    screen.blit(background, (0, 0))

    x -= 3
    if x < -text_surface.get_width():
        x = 0
    y -= 2
    if y < -text_surface.get_height():
        y = screen_size[1]

    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x + text_surface.get_width(), y))
    pygame.display.update()

