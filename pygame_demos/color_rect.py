__author__ = 'Administrator'
import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    x,y = pygame.mouse.get_pos()

    screen.fill((x/10, y/10, 0))
    if pygame.mouse.get_pressed()[0]:
        pygame.display.set_caption("the color test is ---->  %s"%x)
    else:
        pygame.display.set_caption('no color selected')
    pygame.display.update()