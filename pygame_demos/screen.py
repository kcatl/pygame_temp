__author__ = 'Administrator'
import pygame
from sys import exit
from pygame.locals import *
pygame.init()

screensize = (800,600)
screen = pygame.display.set_mode(screensize, 0, 32)
caption = pygame.display.set_caption('hello world')
font = pygame.font.SysFont('arial', 16)
font_height = font.get_linesize()
event_text  = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-screensize[1]/font_height:]
    screen.fill((255,255,255))


    if event.type == QUIT:
        sys.exit()
        pygame.quit()
    y = screensize[1] - font_height
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (0,0,0)), (0,y))
        y -= font_height

    pygame.display.update()

