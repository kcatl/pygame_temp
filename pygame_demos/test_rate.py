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
sprite = pygame.image.load('qq.jpg')
clock = pygame.time.Clock()

x = 0
speed = 250

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


    screen.blit(background, (0,0))
    screen.blit(sprite, (x, 100))
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    if x > 720:
        x -= 720

    pygame.display.update()
