import pygame
from pygame.locals import *
import sys
pygame.init()
displaysurf = pygame.display.set_mode((400,300))
pygame.display.set_caption('hello world')

#the while loop part
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

