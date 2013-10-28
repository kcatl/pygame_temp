__author__ = 'Administrator'
import pygame
from sys import exit
from pygame.locals import *

pygame.init()
imag = 'background.bmp'
screensize = (800,600)
screen = pygame.display.set_mode(screensize, 0, 32)
background = pygame.image.load(imag)

x,y = 0,0
move_x, move_y = 0, 0
fullscreen = False
while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -2
                elif event.key == K_RIGHT:
                    move_x = 2
                elif event.key == K_UP:
                    move_y = -2
                elif event.key == K_DOWN:
                    move_y = 2
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen :
                        screen = pygame.display.set_mode(screensize,FULLSCREEN,32)
                    else:
                        screen = pygame.display.set_mode(screensize,0, 32)


            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    move_x = 0
                elif event.key == K_UP or event.key == K_DOWN:
                    move_y = 0

        if x < 0:
            x = 0
        elif x > 720:
            x = 720
        elif y < 0:
            y =0
        elif y > 530:
            y = 530
        else:
            x += move_x
            y += move_y

        screen.fill((255,255,255))
        screen.blit(background, (x, y))
        pygame.display.update()
