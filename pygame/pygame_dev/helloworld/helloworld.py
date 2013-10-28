import pygame
from pygame.locals import *
from sys import exit

pygame.init()

background = pygame.image.load('background.jpg')
mousepic = pygame.image.load('cat.png')

screen = pygame.display.set_mode((480,360), 0, 32)
caption = pygame.display.set_caption('hello world.py')
#x,y = 0, 0
#move_x,move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
#        if event.type == KEYDOWN:
#            if event.type == K_LEFT:
#                move_x = -1
#            elif event.type == K_RIGHT:
#                move_x = 1
#            elif event.type == K_UP:
#                move_y = 1
#            elif event.type == K_DOWN:
#                move_y = -1
#        elif event.type == KEYUP:
#            if event.type == K_LEFT:
#                move_x = 0
#            elif event.type == K_RIGHT:
#                move_x = 0
#            elif event.type == K_UP:
#                move_y = 0
#            elif event.type == K_DOWN:
#                move_y = 0
#    x += move_x
#    y += move_y
#
   # screen.fill((0,0,0))

    x, y = pygame.mouse.get_pos()
    x -= 35.5
    y -= 30
    pygame.mouse.set_visible(False)

    screen.blit(mousepic, (x,y))

    pygame.display.update()
