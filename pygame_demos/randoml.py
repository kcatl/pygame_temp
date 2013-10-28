__author__ = 'Administrator'
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    random_col = (randint(0,255), randint(0, 255), randint(0, 255))
    screen.lock()

    for _ in range(100):
        rand_pos = (randint(0, 799), randint(0, 599))
        screen.set_at(rand_pos, random_col)

    screen.unlock()
    pygame.display.update()
