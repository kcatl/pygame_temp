__author__ = 'Administrator'
import pygame
from sys import exit
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
screen.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    rand_color = (randint(0,255), randint(0,255), randint(0, 255))
    for _ in range(100):
        rand_pos = (randint(0,799), randint(0, 599))
        screen.set_at(rand_pos, rand_color)

    pygame.display.update()