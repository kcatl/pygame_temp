import sys, pygame
from pygame.locals import *

pygame.init()
displaysurf = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('demo004.py')
displaysurf.fill((255,255,255))
pygame.draw.line(displaysurf,(255,23,100),(60,60),(120,60),3)
pygame.draw.line(displaysurf,(200,100,24),(120,60),(60,120),3)
pygame.draw.line(displaysurf,(100,20,40),(60,120),(120,120),3)
pygame.draw.circle(displaysurf,(55,55,255),(120,120),20,0)
pygame.draw.ellipse(displaysurf,(20,20,20),(120,120,40,80),1)
pygame.draw.circle(displaysurf,(21,12,34),(320,120),55,1)
pygame.draw.rect(displaysurf,(230,234,21),(120,120,100,60),4)
while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

