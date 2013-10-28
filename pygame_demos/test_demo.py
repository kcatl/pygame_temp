__author__ = 'Administrator'
import pygame
from pygame.locals import *
from sys import exit
import random
from random import randint

pygame.init()
screensize = (800, 600)

screen = pygame.display.set_mode(screensize, 0, 32)
caption = pygame.display.set_caption('test demo for motivation')
background = pygame.image.load('background.jpg')
sprite = pygame.image.load('ps.png')
x = 0
y = 0
move_x = 5
move_y = 5
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


    screen.blit(background, (0,0))
    screen.blit(sprite, (x, y))
    x += move_x
    if x > 720.:
        move_x = -move_x
        x += move_x
    elif x < 0:
        move_x = -move_x
        x += move_x

    y += move_y
    if y > 520.:
        move_y = -move_y
        y += move_y
    elif y < 0:
        move_y = -move_y
        y += move_y

    pygame.display.update()
